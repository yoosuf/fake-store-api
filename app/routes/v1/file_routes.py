import os
from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from app.models import File
from app.extensions import db

file_bp = Blueprint('files', __name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt', 'docx'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@file_bp.route('/', methods=['GET'])
def get_files():
    files = File.query.all()
    return jsonify([file.as_dict() for file in files])


@file_bp.route('/<int:id>', methods=['GET'])
def get_file(id):
    file = File.query.get_or_404(id)
    return jsonify(file.as_dict())


@file_bp.route('/', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({"error": "No file part"}), 400

    files = request.files.getlist('files')
    if not files or len(files) == 0:
        return jsonify({"error": "No selected files"}), 400

    saved_files = []

    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            new_file = File(
                originalname=file.filename,
                filename=filename,
                location=file_path
            )
            db.session.add(new_file)
            db.session.commit()
            saved_files.append(new_file.as_dict())
        else:
            return jsonify({"error": f"File type not allowed for file {file.filename}"}), 400

    return jsonify(saved_files), 201


@file_bp.route('/<int:id>', methods=['PUT'])
def update_file(id):
    file = File.query.get_or_404(id)
    data = request.get_json()
    for key, value in data.items():
        setattr(file, key, value)
    db.session.commit()
    return jsonify(file.as_dict())


@file_bp.route('/<int:id>', methods=['DELETE'])
def delete_file(id):
    file = File.query.get_or_404(id)
    db.session.delete(file)
    db.session.commit()
    return '', 204
