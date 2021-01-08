import json

from flask import Flask, request, render_template
from flask import jsonify

app = Flask(__name__)

with open('test.json', 'r') as testfile:
    data = testfile.read()


@app.route('/')
def hello_world():
    hello = 'Hello World!'
    html = render_template('index.html', title='HELLO', hello=hello)
    return html


objs = json.loads(data)

@app.route('/todo/getall', methods=['GET'])
def getall():
    html = render_template('getall.html', title='DATA', objs=objs)
    return html


@app.route('/todo/create', methods=['GET', 'POST'])
def create():
    return 'Create new task'


@app.route('/todo/update', methods=['GET', 'PATCH'])
def update():
    return 'Update Task'


@app.route('/todo/delete', methods=['GET', 'DELETE'])
def delete():
    return 'Delete task'


if __name__ == "__main__":
    app.run(debug=True)
