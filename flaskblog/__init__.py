import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'b7eceba8acfddfdbde122bb16f221846'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # /// means relative path from this file
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #this is the function name of route
login_manager.login_message_category = 'info';

# db.create_all() will generate all the database tables
# db.drop_all() will remove all the database table


app.config['MAIL_SERVER'] = 'smtp.googleemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAL_PASS')

mail = Mail(app)




from flaskblog import routes  # this need after app initialized :)