from api import app,users


@app.route('/user/login')
def user_login():
    return 'Hello World!'
