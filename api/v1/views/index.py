#!/usr/bin/python3
"""Index"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status", strict_slashes=False)
def status():
    '''
        return JSON of OK status
    '''
    json_dict = {"status": "OK")
    return jsonify(json_dict)


@app_views.route("/stats", strict_slashes=False)
def stats:
    '''
        return counts of all classes in storage
    '''
    stats = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }
    return jsonify(stats)
