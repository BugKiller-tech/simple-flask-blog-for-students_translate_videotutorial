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