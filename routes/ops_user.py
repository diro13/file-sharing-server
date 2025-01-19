from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.utils import secure_filename
from models import File, db
from utils.encryption import encrypt_url
import os

ops_user = Blueprint('ops_user', __name__)
ALLOWED_EXTENSIONS = {'pptx', 'docx', 'xlsx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@ops_user.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    current_user = get_jwt_identity()
    if current_user['role'] != 'ops':
        return jsonify({'message': 'Unauthorized'}), 403

    file = request.files.get('file')
    if not file or not allowed_file(file.filename):
        return jsonify({'message': 'Invalid file type'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join('uploads', filename)
    file.save(file_path)

    secure_url = encrypt_url(f'/download/{filename}')
    new_file = File(file_name=filename, file_type=file.filename.split('.')[-1],
                    uploaded_by=current_user['id'], secure_url=secure_url)
    db.session.add(new_file)
    db.session.commit()

    return jsonify({'message': 'File uploaded successfully', 'secure_url': secure_url}), 201
