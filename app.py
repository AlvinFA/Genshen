from flask import Flask
from flask_admin import Admin

app = Flask(__name__)
admin = Admin(app)

@app.route('/')
def hello_world():
	return 'Hello World!'

if __name__ == '__main__':
	app.run()
