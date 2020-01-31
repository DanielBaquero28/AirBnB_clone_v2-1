#!/usr/bin/python3
""" Starting my API """
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import make_response

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def handling_error_404():
    """ Handles error 404 """
    return (make_response(jsonify({"error": "Not found"}), 404))


@app.teardown_appcontext
def close_storage(_):
    """ Calls storage.close() method """
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", '0.0.0.0')
    port = getenv("HBNB_API_PORT", '5000')
    app.run(host, port, threaded=True)
