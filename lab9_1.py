from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"


@app.route('/<opt>/<int:a>/<int:b>')
def arithmetic(opt, a, b):
    if opt == 'add':
        ans = a + b
        return f'<h3>{a} + {b} = {ans}</h3>'
    elif opt == 'sub':
        ans = a - b
        return f'<h3>{a} - {b} = {ans}</h3>'
    elif opt == 'mul':
        ans = a * b
        return f'<h3>{a} * {b} = {ans}</h3>'
    elif opt == 'div':
        if b == 0:
            return '<h3>Error: Division by zero</h3>'
        ans = a / b
        return f'<h3>{a} / {b} = {ans}</h3>'
    else:
        return '<h3>Error: Invalid operation</h3>'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
