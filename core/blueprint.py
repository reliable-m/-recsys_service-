from flask import Blueprint, current_app, request, jsonify, render_template
from flask_cors import CORS, cross_origin
import os
import logging
import datetime

from .controller import *

blueprint = Blueprint(
    'blueprint', __name__)

UPLOAD_FOLDER = current_app.config['UPLOAD_FOLDER']


@blueprint.route("/recommend", methods=['POST'], endpoint='recommend', strict_slashes=False)
def generate_recommendations():
    data = request.json
    print(data)

    file_path = UPLOAD_FOLDER + "/" + data['filename']
    print(file_path)
    document_text = recommend_content(file_path)
    current_app.logger.info(document_text)

    return jsonify({
        "document_text": document_text
    })
