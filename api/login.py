from api import app, users, bcrypt
from flask import request, json
from flask_jwt_extended import create_access_token, jwt_optional, get_jwt_identity


@app.route('/user/login', methods=["POST"])
@jwt_optional
def user_login():
    current_user = get_jwt_identity()
    if current_user:
        return current_user
    else:
        data = request.get_json(force=True)
        user = users.find_one({"email": data["email"]})
        if user is None:
            response = json.jsonify({
                "result": "user_not_found"
            })
            return response
        if bcrypt.check_password_hash(user["password"], data["password"]):
            response = json.jsonify({
                "result": "ok",
                "token": create_access_token(identity=data["email"])
            })
            return response, 200
        response = json.jsonify({
            "result": "wrong_pass!"
        })
        return response
