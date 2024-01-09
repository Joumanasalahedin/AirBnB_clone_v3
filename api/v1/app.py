#!/usr/bin/python3
"""AirBnB Clone App"""

from flask import Flask, jsonify
from flask_cors import CORS
from os import getenv
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def error_404(exception):
    """Handles 404 errors
    Returns JSON response"""
    error = {
        "error": "Not found"
    }

    data = jsonify(error)
    data.status_code = 404

    return (data)


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(getenv("HBNB_API_PORT", 5000))

    app.run(host=host, port=port, threaded=True)
