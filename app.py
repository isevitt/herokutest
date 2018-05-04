from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']


@app.route('/page')
def index():
	return 'This is my app'

if __name__ == "__main__":
	app.run()
