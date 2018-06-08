# -*- coding: UTF-8 -*-

# Filename : server.py
# author by : WeiQi

from flask import Flask, jsonify

app = Flask(__name__)

tasks = {
    'limit': 1000,
    'subscribed': [],
    'others': [{
        'id': 1,
        'title': u'Buy groceries',
        "thumbnail": "http://pic3.zhimg.com/0e71e90fd6be47630399d63c58beebfc.jpg",
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False},
        {
        'id': 2,
        'title': u'Learn Python',
        "thumbnail": "http://pic4.zhimg.com/2c38a96e84b5cc8331a901920a87ea71.jpg",
        'description': u'Need to find a good Python tutorial on the web',
        'done': False},
        {
        'id': 3,
        'title': u'Learn Python',
        "thumbnail": "http://pic4.zhimg.com/2c38a96e84b5cc8331a901920a87ea71.jpg",
        'description': u'Need to find a good Python tutorial on the web',
        'done': False},
        {
        'id': 4,
        'title': u'Buy groceries',
        "thumbnail": "http://pic3.zhimg.com/0e71e90fd6be47630399d63c58beebfc.jpg",
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False},
        {
        'id': 5,
        'title': u'Learn Python',
        "thumbnail": "http://pic4.zhimg.com/2c38a96e84b5cc8331a901920a87ea71.jpg",
        'description': u'Need to find a good Python tutorial on the web',
        'done': False}]
}

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    # return jsonify({'tasks': tasks})
    return jsonify(tasks)

@app.before_request
def before_request():
    global price_data

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8080)