from api import app


@app.route('/user/signup')
def user_signup():
    return 'Hello World!'
