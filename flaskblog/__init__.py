from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'b7eceba8acfddfdbde122bb16f221846'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # /// means relative path from this file
db = SQLAlchemy(app)

# db.create_all() will generate all the database tables
# db.drop_all() will remove all the database table



from flaskblog import routes  # this need after app initialized :)