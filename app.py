from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from models import db
from routes.ops_user import ops_user
from routes.client_user import client_user
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)
mail = Mail(app)

app.register_blueprint(ops_user, url_prefix='/ops')
app.register_blueprint(client_user, url_prefix='/client')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
