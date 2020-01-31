#!/usr/bin/python3
""" Importing moduls¡es required for index """
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """ Checks app_view status """
    return jsonify({'status':'OK'})


@app_views.route('/stats')
def stats():
    """
    Creates and endpoint that retrieves the number of each objects by type
    """
    models = ['User', 'State', 'Review', 'Place', 'City', 'Amenity']
    stats = {}
    for item in models:
        stats['item'] = storage.count(item)
    return (jsonify(stats))
