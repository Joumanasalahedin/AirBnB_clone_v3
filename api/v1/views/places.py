#!/usr/bin/python3
"""Place objects for RESTful API actions"""

from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.place import Place


@app_views.route("/cities/<city_id>/places", methods=[' GET'],
                 strict_slashes=False)
def places(city_id):
    """retrieves all Place objects by city"""
    place_list = []
    city = storage.get("City", city_id)
    if not city:
        abort(404)
    for place in city.places:
        place_list.append(place.to_dict())

    return jsonify(place_list)


@app_views.route("/places/<place_id>", methods=['GET'],
                 strict_slashes=False)
def place_by_id(place_id):
    """retrieves a Place object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route("places/<place_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """Deletes a Place object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()

    return jsonify({})


@app_views.route("cities/<city_id>/places", methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """creates place route"""
    json_place = request.get_json()
    if json_place is None:
        abort(400, 'Not a JSON')
    if not storage.get("City", city_id):
        abort(404)
    if "user_id" not in json_place:
        abort(400, 'Missing user_id')
    if not storage.get("User", json_place["user_id"]):
        abort(404)
    if "name" not in json_place:
        abort(400, 'Missing name')

    json_place["city_id"] = city_id

    new_place = Place(**json_place)
    new_place.save()
    resp = jsonify(new_place.to_json())
    resp.status_code = 201

    return resp


@app_views.route("/places/<place_id>", method=["PUT"],
                 strict_slashes=False)
def update_place(place_id):
    """updates place object by ID"""
    json_place = request.get_json()

    if json_place is None:
        abort(400, 'Not a JSON')

    place = storage.get(Place, place_id)

    if place is None:
        abort(404)

    for key, val in json_place.items():
        if key not in ["id", "created_at", "updated_at", "user_id", "city_id"]:
            setattr(place, key, val)

    place.save()

    return jsonify(place.to_json())
