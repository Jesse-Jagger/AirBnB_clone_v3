#!/usr/bin/python3
"""creates a flask app, app_views"""

from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """returns status"""
    response = jsonify({"status": "OK"})
    return jsonify({"status": "OK"})
