#!/usr/bin/python3
""" Importing moduls¡es required for index """
from api.v1.views import app_views
from json import jsonify
from models import storage


@app.route('/status')
def status_appviews():
    """ Checks app_view status """
    return (jsonify({"status": "OK"}))


@app.route('/stats')
def func_stats():
    """
    Creates and endpoint that retrieves the number of each objects by type
    """
    models = ['User', 'State', 'Review', 'Place', 'City', 'Amenity']
    stats = {}
    for item in models:
        stats['item'] = storage.count(item)
    return (jsonify(stats))
