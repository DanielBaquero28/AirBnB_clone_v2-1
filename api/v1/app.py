#!/usr/bin/python3
""" Starting my API """
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import make_response


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage():
    """ Calls storage.close() method """
    storage.close()


@app.errorhandler(404)
def handling_error_404():
    """ Handles error 404 """
    return (make_response(jsonify({"error": "Not found"}), 404))

if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST"), port=getenv("HBNB_API_PORT"),
            threaded=True)
