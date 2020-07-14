from flask import Flask, jsonify, request
from managers import create_task, list_task, delete_task

app = Flask(__name__)


@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works! {changed from clone2 and then again to create conflict!}'})


@app.route('/task', methods=['POST'])
def addTask():
    task_name = request.form['task_name']
    task_desc = request.form['task_desc']

    message = create_task(task_name, task_desc)

    return jsonify({'message': message})


@app.route('/task/list', methods=['GET'])
def listTask():

    message = list_task()

    return jsonify({'task': message})


@app.route('/task/delete/<int:task_id>', methods=['DELETE'])
def daleteTask(task_id):

    message = delete_task(task_id)

    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(debug=True, port=8001)
