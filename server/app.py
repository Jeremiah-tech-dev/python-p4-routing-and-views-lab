#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<text>')
def print_text(text):
    print(text)
    return text


@app.route('/count/<int:n>')
def count(n):
    if n <= 0:
        return ''
    return '\n'.join(str(i) for i in range(n)) + '\n'


@app.route('/math/<x>/<op>/<y>')
def math_operation(x, op, y):
    try:
        if op == 'div':
            a = float(x)
            b = float(y)
            result = a / b
        else:
            a = int(x)
            b = int(y)
            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '%':
                result = a % b
            else:
                return 'Invalid operation', 400
    except (ValueError, ZeroDivisionError):
        return 'Error', 400

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
