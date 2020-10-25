from flask import request, json
from flask_jwt_extended import create_access_token

from api import app, users, bcrypt


@app.route('/user/signup', methods=["POST"])
def user_signup():
    data = request.get_json(force=True)
    user = users.find_one({"email": data["email"]})
    if user is None:
        hashed_pw = bcrypt.generate_password_hash(data["password"]).decode("UTF-8")
        user = {
                "email": data["email"],
                "password": hashed_pw,
                "username": data['username'],
                "contact": data['contact']
                }
        users.insert_one(user)
        response = json.jsonify({
                "result": "ok",
            })

        return response, 201
    else:
        response = json.jsonify({
            "results": "user_exist"
        })
        return response
