import os
import socket

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Flask : This is from Las Vegas 2019 - v1.0'

@app.route("/hostname")
def return_hostname():
    return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)


@app.route('/fib/<int:number>')
def index(number=1):
    return "Python Fib("+ str(number) + "): " + str(fib(number))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
