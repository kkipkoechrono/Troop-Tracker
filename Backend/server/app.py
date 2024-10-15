from flask import Flask
from modules import db
from flask_migrate import Migrate
app = Flask(__name__)




#configuring database uri
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///military.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialising the database
db.init_app(app)
migrate = Migrate(app,db)


@app.route('/')
def index():
    return "Welcome to TroopTracker "

if __name__ == "__main__":
    app.run(port=5555, debug=True)