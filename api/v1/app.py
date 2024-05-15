#!/usr/bin/python3

"""creates a flask app, and registers the blueprint app.view
flask instance"""

from os import getenv
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_engine(exception):
    """closes the storage"""
    storage.close()


@app.errorhandler(404)
def page_not_found(error):
    """returns a 404 page"""
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = int(getenv('HBNB_API_PORT', 5000))
    app.run(host=HOST, port=PORT, threaded=True, debug=True)
