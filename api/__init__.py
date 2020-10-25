from flask import Flask, json
from pymongo import MongoClient
from werkzeug.security import safe_str_cmp
from werkzeug.exceptions import HTTPException, BadRequest, InternalServerError, NotFound
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"


@app.errorhandler(InternalServerError)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description
    })
    response.content_type = "application/json"
    return response


@app.errorhandler(NotFound)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description
    })
    response.content_type = "application/json"
    return response


client = MongoClient('mongodb://localhost:27017/')
db = client['e-commerce-beta']
users = db['users']
products = db['products']

bcrypt = Bcrypt(app)

jwt = JWTManager(app)

from api import login
from api import signup
