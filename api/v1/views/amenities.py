#!/usr/bin/python3
"""  Cities RestFul API """

from flask import Blueprint, jsonify, abort, request
from models import storage
from models.amenity import Amenities

import json


def init_amenities():
    from api.v1.views import app_views

    @app_views.route('/amenities', methods=['GET'])
    def get_all_amenities():
        """ Get all amenities"""
        if storage.get("Amenities") is not None:
            amenities = []
            for amenity in storage.all("Amenities").values():
                amenities.append(amenity.to_dict())
            return jsonify(amenities)
        else:
            abort(404)

    @app_views.route('/amenities/<amenity_id>', methods=['GET'])
    def get_amenity(amenity_id):
        """ Get amenity """
        amenity = storage.get("Amenity", str(amenity_id))
        if amenity is not None:
            return jsonify(city.to_dict())
        abort(404)

    @app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
    def delete_amenity(amenity_id):
        """ Delete amenity """
        if amenity_id is not None:
            if storage.get("Amenity", str(amenity_id)) is not None:
                storage.delete(storage.get("Amenity", str(amenity_id)))
            else:
                abort(404)
        return jsonify({}), 200

    @app_views.route('/amenities', methods=['POST'])
    def create_amenity():
        """ Create states """
        if not request.json:
            return jsonify({"error": "Not a Json"}), 400
        if 'name' not in request.json:
            return jsonify({"error": "Missing name"}), 400
        amenity = Amenity(**request.get_json())
        storage.new(amenity)
        return jsonify(storage.get("amenity", amenity.id).to_dict()), 201

    @app_views.route('/amenities/<amenity_id>', methods=['PUT'])
    def update_amenities(amenity_id):
        """ Update amenities """
        if storage.get("Amenity", str(city_id)) is None:
            abort(404)
        if not request.json:
            return jsonify({"error": "Not a Json"}), 400
        amenity = storage.get("Amenity", str(amenity_id))
        for key, value in request.json.items():
            setattr(amenity, key, value)
        storage.save()
        return jsonify(storage.get("Amenity", city.city_id).to_dict()), 200