from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tjavwaac:5YiFypiknAL3wu7ox1occfnXnCecuKjL@trumpet.db.elephantsql.com/tjavwaac'
db = SQLAlchemy(app)

from application import routes # Routes works with app and if this line is at the top, routes will never find app. Therefore needs to be at the bottom.
