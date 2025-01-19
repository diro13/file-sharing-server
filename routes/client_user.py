from flask import Blueprint, request, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from models import User, File, db
from utils.encryption import decrypt_url
from utils.auth import hash_password, verify_password
from flask_mail import Message
from flask_mail import Mail
import os

client_user = Blueprint('client_user', __name__)

@client_user.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    email = data['email']
    password = hash_password(data['password'])
    new_user = User(email=email, password_hash=password, role='client', email_verified=False)
    db.session.add(new_user)
    db.session.commit()

    secure_url = encrypt_url(email)
    # Send verification email
    msg = Message('Verify your email', sender='your_email@gmail.com', recipients=[email])
    msg.body = f"Click the link to verify your email: {secure_url}"
    mail.send(msg)

    return jsonify({'message': 'User created successfully. Verify email to proceed.'}), 201

@client_user.route('/verify-email', methods=['GET'])
def verify_email():
    encrypted_email = request.args.get('token')
    email = decrypt_url(encrypted_email)

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'Invalid token'}), 400

    user.email_verified = True
    db.session.commit()
    return jsonify({'message': 'Email verified successfully'}), 200

@client_user.route('/download/<filename>', methods=['GET'])
@jwt_required()
def download_file(filename):
    current_user = get_jwt_identity()
    if current_user['role'] != 'client':
        return jsonify({'message': 'Unauthorized'}), 403

    file = File.query.filter_by(file_name=filename).first()
    if not file:
        return jsonify({'message': 'File not found'}), 404

    return send_from_directory('uploads', filename)

@client_user.route('/list-files', methods=['GET'])
@jwt_required()
def list_files():
    current_user = get_jwt_identity()
    if current_user['role'] != 'client':
        return jsonify({'message': 'Unauthorized'}), 403

    files = File.query.all()
    file_list = [{'file_name': file.file_name, 'secure_url': file.secure_url} for file in files]
    return jsonify(file_list), 200
