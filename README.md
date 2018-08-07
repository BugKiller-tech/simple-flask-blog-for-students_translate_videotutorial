

Memory by learning this series by the hkg328!

```
export FLASK_APP=flaskblog.py    # in windows we need to do it set FLASK_APP=flaskblog.py
export FLASK_DEBUG=1

flask run
```


or
```
python3 flaskblog.py
```

```
pip3 install flask-wtf
```


made secret key by running this in python terminal to genreate random string
```
import secrets
secrets.token_hex(16)
```


> to use orm effect let's use sqlalchemy especially flask-sqlalchemy for flask.
``` 
pip install flask-sqlalchemy
```


> flask sqlachemy circular import problem

when we divide the  models to separate file
that will make soem problem

main file, we import the model
then in model file we import the db(db=SQLAchemy())
that will make the circular problem


To avoid this problem, we can change the import like this
```
from __main__ import db
```
This will make problem can not find db.
to fix this, we can make ```db = SQLAchemy()``` first , and then import the models.
but this is ugly solution!

What is the solution? The solution is to make our app as package.


> Install flask-bcrypt to encrypt the user password
```
pip install flask-bcrypt
```

> Install flask-login 
```
pip install flask-login
```


> install package called pillow to resize the image
```
pip install Pillow
```

> To send reset password token email, we'll use the extension called "flask-mail"
```
pip instal flask-mail
```