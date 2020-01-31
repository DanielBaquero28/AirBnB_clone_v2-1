#!/usr/bin/python3
""" Handles all default RestFul API actions """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.base_model import BaseModel
from models.state import State
from models import storage


@app_views.route('/states', strict_slashes=False, methods=['GET'])
def all_states():
    """ Retrieves the list of State objects """
    list_state = []
    states = states.all('State').values()
    for state in states:
        state_list.append(state.to_json())
    return (jsonify(state_list))


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE'])
def retrieve_delete_state(state_id):
    """ Retrieves and deletes states by id """
    states_storage = storage.get('State', state_id)
    if states_storage is None:
        abort(404)
    if request.method == 'DELETE':
        storage.delete(states_storage)
        storage.save()
        return (jsonify({}), 200)


@app_views.route('/states/', strict_slashes=False, methods=['POST'])
def post_states():
    """ Creates a new State object """
    dict_request = request.to_json()
    if not request.is_json:
        abort(400, {"error": "Not a JSON"})
    if "name" not in dict_request.keys():
        abort(400, {"error": "Missing name"})
    state = State(name=dict_request['name'])
    state.save()
    return (jsonify(state.to_json()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_states(state_id):
    """ Updates State objects """
    states_storage = storage.get('State', state_id)
    if not states_storage:
        abort(404)
    dict_request = request.to_json()
    if "name" not in dict_request.keys():
        abort(400, {"error": "Not a JSON"})
    states_storage = states_storage.to_json()
    keys = ['id', 'created_at', 'updated_at']
    states_storage.update({key: value for (key, value) in dict_request.items()
                           if key not in keys})
    storage.save()
    return (jsonify(states_storage), 200)
