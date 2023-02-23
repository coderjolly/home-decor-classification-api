from flask import Blueprint, request, Response, redirect, url_for
import tensorflow as tf
from utils import classificationModel
import json, os
from werkzeug.utils import secure_filename
from config import ROOT_PATH

classify_api = Blueprint('classification', __name__)

@classify_api.route('/classification', methods=['GET', 'POST'])
def classification():
    
    if request.method == 'POST':
        file = request.files['file']
        print("*********************************************************")
        filename = "test.jpg"
        dir_path = os.path.join(ROOT_PATH, filename)
        file.save(os.path.join(dir_path))

        classified_value = classificationModel(dir_path)
        return Response(json.dumps(classified_value), mimetype='application/json', status=200)
