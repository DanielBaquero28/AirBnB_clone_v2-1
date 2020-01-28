#!/usr/bin/python3
""" Importing moduls¡es required for index """
from api.v1.views import app_views
from json import jsonify


@app.route('/status')
def status_appviews():
    """ Checks app_view status """
    return (jsonify({"status": "OK"}))
