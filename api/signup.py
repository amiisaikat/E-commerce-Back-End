from api import app, users, bcrypt
from flask import request, json
from flask_jwt_extended import create_access_token


@app.route('/user/signup')
def user_signup():
    data = request.get_json(force=True)
    user = users.find_one({'email': data['email']})
    if user is None:
        hashedpw = bcrypt.generate_password_hash(data['password'])
        user = {
                'email': data['email'],
                'password': hashedpw,
                'username': data['username'],
                'contact': data['contact']
                }
        users.insert_one(user).inserted_id()
        response = json.jsonify({
            "result": "ok",
            "token": create_access_token(identity=data["email"])})
        return response, 200
    else:
        response = json.jsonify({
            'results': 'User Already Exists, Try another email or forget password'
        })
        return response
