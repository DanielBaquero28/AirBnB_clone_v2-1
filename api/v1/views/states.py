#!/usr/bin/python3
""" Handles all default RestFul API actions """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models.state import State
from models import storage


@app_views.route('/states', strict_slashes=False)
@app_views.route('/states/<state_id>', strict_slashes=False)
def all_states(state_id=None):
    """ Retrieves the list of State objects """
    list_state = []
    if state_id is None:
        for state in storage.all('State').values():
            list_state.append(state.to_dict())
        return jsonify(list_state)
    elif storage.get('State', state_id):
        return storage.get('State', state_id).to_dict()
    else:
        abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def retrieve_delete_state(state_id=None):
    """ Retrieves and deletes states by id """
    if request.method == 'DELETE' and state_id is not None:
        states_storage = storage.get('State', state_id)
        storage.delete(states_storage)
        storage.save()
        return jsonify({}), 200
    else:
        abort(404)


@app_views.route('/states/', strict_slashes=False, methods=['POST'])
def post_states():
    """ Creates a new State object """
    dict_request = request.get_json()
    if dict_request:
        if 'name' in dict_request:
            state = State(**dict_request)
            state.save()
            return jsonify(state.to_dict()), 201
        else:
            abort(400, {"error": "Missing name"})
    else:
        abort(400, {"error": "Not a JSON"})


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
