import os

class Config:
  SECRET_KEY = 'b7eceba8acfddfdbde122bb16f221846'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # /// means relative path from this file

  # we can do this like this
  # in the bash_profile
  #export SECRET_KEY='b7eceba8acfddfdbde122bb16f221846'
  #export SQLALCHEMY_DATABASE_URI='sqlite:///site.db'

  # and then here, instead of direct input the value like above, we can do it like below.
  # SECRET_KEY = os.environ.get('SECRET_KEY')
  # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')


  MAIL_SERVER = 'smtp.googleemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get('EMAIL_USER')
  MAIL_PASSWORD = os.environ.get('EMAL_PASS')