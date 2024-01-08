#!/usr/bin/python3
"""Index"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    """status route"""
    return jsonify(status="OK")


@app_views.route('/stats', method=["GET"], strict_slashes=False)
def stats():
    """number of each object by type"""
    data = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }

    stats = jsonify(data)
    stats.status_code = 200

    return stats
