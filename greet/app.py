
from flask import Flask

app = Flask(__name__)

@app.get('/welcome')
def say_welcome():
    """Return "welcome" greeting"""

    html = "<html><body><h1><welcome</h1></body></html>"
    return html

@app.get('/welcome/home')
def say_welcome_home():
    """Return "welcome home" greeting"""

    html = "<html><body><h1><welcome home</h1></body></html>"
    return html

@app.get('/welcome/back')
def say_welcome_back():
    """Return "welcome back" greeting"""

    html = "<html><body><h1><welcome back</h1></body></html>"
    return html

    # make sure you're in your venv/ before you open your code