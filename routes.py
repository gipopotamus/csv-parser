from flask import Blueprint, request, jsonify
import os
import csv

bp = Blueprint('routes', __name__)

UPLOAD_FOLDER = 'uploads'


@bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = file.filename
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return 'File uploaded successfully.'


@bp.route('/files', methods=['GET'])
def get_files():
    if os.path.exists(UPLOAD_FOLDER):
        files = os.listdir(UPLOAD_FOLDER)
        return {'files': files}
    else:
        return 'No files found.', 404


@bp.route('/data', methods=['GET'])
def get_data():
    filename = request.args.get('filename')

    if filename is None:
        return 'No filename provided.', 400

    file_path = os.path.join(UPLOAD_FOLDER, filename)

    if os.path.exists(file_path):
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

            filter_column = request.args.get('filter_column')
            filter_value = request.args.get('filter_value')
            sort_columns = request.args.getlist('sort_columns')

            if filter_column and filter_value:
                data = [row for row in data if row.get(filter_column) == filter_value]

            if sort_columns:
                data = sorted(data, key=lambda row: [row.get(column) for column in sort_columns])

            return {'data': data}
    else:
        return 'File not found.', 404



@bp.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return 'File deleted successfully.'
    else:
        return 'File not found.', 404
