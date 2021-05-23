from flask import Flask
from flask_admin import Admin

app = Flask(__name__)
admin = Admin(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/welcome')
def welcome():
    return '你好世界!'

if __name__ == '__main__':
    app.run()


