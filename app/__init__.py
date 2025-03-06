from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'sakjdhfkewjdgkjasfhkljhweqoiuryhsdjkfbdsmnkfdskjfh'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Duy%402003@localhost/hoteldb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)
login = LoginManager(app=app)