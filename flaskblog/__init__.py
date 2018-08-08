from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config




db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()

login_manager.login_view = 'login' #this is the function name of route
login_manager.login_message_category = 'info';

# db.create_all() will generate all the database tables
# db.drop_all() will remove all the database table







def create_app(config_class=Config):
  app = Flask(__name__)
  app.config.from_object(config_class)

  db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)

  # from flaskblog import routes  # this need after app initialized :)  now remove for blueprint
  from flaskblog.users.routes import users
  from flaskblog.posts.routes import posts
  from flaskblog.main.routes import main

  app.register_blueprint(users)
  app.register_blueprint(posts)
  app.register_blueprint(main)

  return app
  