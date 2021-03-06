from api import app, users, bcrypt
from flask import request, json
from flask_jwt_extended import create_access_token


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
                "result": {
                            "username": user["username"],
                            "email": user["email"]
                            },
                "token": create_access_token(identity=user["email"])
            })

        return response, 200
    else:
        response = json.jsonify({
            "results": "User Already Exists, Try another email or forget password"
        })
        return response
