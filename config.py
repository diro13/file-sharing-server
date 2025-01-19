import os

class Config:
    SECRET_KEY = 'whatareyouding'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///secure_file_sharing.db'  # SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'hello'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'yourgmail.com'  # Replace with your email
    MAIL_PASSWORD = 'mailpassword'  # Replace with your app-specific password
    UPLOAD_FOLDER = 'uploads/'
