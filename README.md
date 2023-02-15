# flask-ngrok2-pageprinter

Based on [flask-ngrok](https://github.com/gstaff/flask-ngrok) and [flask-ngrok2](https://github.com/MohamedAliRashad/flask-ngrok2)
The successor for [flask-ngrok](https://github.com/gstaff/flask-ngrok) for making demo Flask apps from personal machine with added auth token functionality to build indipendent full stack apps within jupyer notebook and google collab. notebooks.

## Compatability
Python 3.6+ is required.

## Installation

```bash
pip install git+https://github.com/Davz33/flask-ngrok2-pageprinter
```

## Quickstart
1. Import with ```from flask_ngrok2_pp import run_with_ngrok```
2. Add `run_with_ngrok(app,logpath,auth_token)` to make your Flask app available upon running  
3. At server start, the log at logpath will contain the ngrok tuttel address. You can then json.load-it and make use of it for http/https request within jupyter notebooks.

To make full sense of this package, you will hav to run the following as python command from a .py external script.
```python
# flask_ngrok_example.py
from flask import Flask
from flask_ngrok2_pp import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app, logpath=LOGPATH, auth_token=authtoken)  # Start ngrok when app is run

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
```
Then, in your jupyer notebook, you can use `json.load()` to pull the active tunnel address.
