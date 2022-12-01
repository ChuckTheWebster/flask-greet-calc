from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


OPERATIONS = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}



@app.get('/math/<operation>')
def do_operation(operation):

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = OPERATIONS[operation](a,b)

    return f"{result}"


@app.get('/add')
def do_add():

    a = int(request.args["a"])
    b = int(request.args["b"])

    result = add(a, b)

    return f"{result}"

@app.get('/sub')
def do_sub():

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)

    return f"{result}"

@app.get('/mult')
def do_mult():

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)

    return f"{result}"

@app.get('/div')
def do_div():

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)

    return f"{result}"



    # return """
    #   <form method="POST">
    #     <input name="a">
    #     <input name="b">
    #     <button>submit</button>
    #   </form>
    # """


# @app.post('/domath')
# def do_math():

#     a = request.args["a"]
#     b = request.args["b"]

#     return