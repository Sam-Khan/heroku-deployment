from flask import Flask, jsonify, request

app = Flask(__name__)


todo_list = [
    {'task_id':'123', 'task_name': 'write email',
    'task_desc':'loream epsum for task'},
    {'task_id':'124', 'task_name': 'write code',
    'task_desc':'loream epsum for task'},
    {'task_id':'125', 'task_name': 'write something',
    'task_desc':'loream epsum for task'}
]

@app.route("/")
def main():
    documentation = """
    get tasks [GET] : <server>/todo/api/v1/tasks \n
    add task [POST] : <server>/todo/api/v1/<task_id>/task \n
    search task [GET]  : <server>/todo/api/v1/<task_id>/task
    """
    return documentation, 200

@app.route("/todo/api/v1/tasks")
def list_tasks():
    return jsonify(todo_list), 200

@app.route("/")
def landing_page():
    return '<h1>This is the Samreens  API.</h1>'


@app.route( "/todo/api/v1/<task_id>/task", methods=['GET'])
def search_task(task_id):
    # search task based using task_id
    if request.method == 'GET':
        tasks = [task for task in todo_list if task['task_id'] == task_id]
        if not tasks:
            tasks = {'error':'task id not found'}
        return jsonify(tasks), 200


@app.route( "/todo/api/v1/task/add", methods=['POST'])
def add_task():
    # search task based using task_id
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        todo_list.append(data)
        return jsonify(todo_list), 200
    else:
        return {'error':'invalid request'}, 401


@app.route( "/todo/api/v1/task/<task_id>/delete", methods=['DELETE'])
def delete_task(task_id):
    # search task based using task_id
    if request.method == 'DELETE':
        task_id = str(task_id)
        print(f'task to delete: {task_id}')
        task_index = delete_task_by_id(task_id)
        if not task_index:
            return jsonify({'info': f'task_id: {task_id} not found'}), 200
        return jsonify(todo_list), 200
    else:
        return {'error':'invalid request'}, 401


def delete_task_by_id(task_id):
    task_index = [index for index,dict in enumerate(todo_list) if dict['task_id'] == task_id]
    if task_index:
        todo_list.pop(task_index[0])
    return task_index
