from flask import Flask, request, math
from operations import add, sub, mult, div

app = Flask(__name__)

@app.get('/add')
def get_form():

    return """
      <form method="POST">
        <input name="a">
        <input name="b">
        <button>submit</button>
      </form>
    """

@app.get('/sub')
def get_form():

    return """
      <form method="POST">
        <input name="a">
        <input name="b">
        <button>submit</button>
      </form>
    """

@app.get('/mult')
def get_form():

    return """
      <form method="POST">
        <input name="a">
        <input name="b">
        <button>submit</button>
      </form>
    """

@app.get('/div')
def get_form():

    return """
      <form method="POST">
        <input name="a">
        <input name="b">
        <button>submit</button>
      </form>
    """


@app.post('/domath')
def do_math():

    a = request.args["a"]
    b = request.args["b"]

    return