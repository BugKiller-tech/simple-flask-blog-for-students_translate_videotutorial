from flask import render_template, request, flash, redirect, url_for

from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import Post, User

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
  return render_template('home.html', posts=posts, title='Home page')

@app.route("/about")
def about():
  return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
  form = RegistrationForm()

  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
  form = LoginForm()
  
  if form.validate_on_submit():
    if form.email.data == 'test@gmail.com' and form.password.data == '111111':
      flash(f'Successfully logged in ', 'success')
      return redirect(url_for('home'))  # here 'home' must be the function name
    else:
      flash(f'The credential you entered is wrong', 'danger')

  return render_template('login.html', title='Login', form=form)



