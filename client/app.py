from flask import Flask, request, render_template
import users
import todos

app = Flask(__name__)

users_api = users.Users()
todos_api = todos.Todos()

@app.route('/')
@app.route('/users')
def index():
    users = users_api.get_users()
    return render_template('index.html', users=users)

@app.route('/todos')
def get_todos():
    todos = todos_api.get_todos()
    return render_template('todos.html', todos=todos)

@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    user = users_api.get_user_by_id(user_id)
    return render_template('user.html', user=user)

@app.route('/todos/<int:todo_id>')
def get_todo_by_id(todo_id):
    todo = todos_api.get_todo_by_id(todo_id)
    return render_template('todo.html', todo=todo)



@app.route('/todos/new')
def new_todo():
    return render_template('create_todo.html')

@app.route('/todos', methods=['POST'])
def create_todo():
    title = request.form['title']
    completed = request.form['completed']
    user_id = request.form['user_id']
    todo = {
        'title': title,
        'completed': completed,
        'userId': user_id
    }
    todos_api.create_todo(todo)
    return 'Tarefa criada'


@app.route('/users/new')
def new_user():
    return render_template('create_user.html')
    

@app.route('/users', methods=['POST'])
def create_user():
    name = request.form['name']
    username = request.form['username']
    email = request.form['email']
    user = {
        'name': name,
        'username': username,
        'email': email
    }
    users_api.create_user(user)
    return 'Usuario criado'
    

if __name__ == '__main__':
    app.run(debug=True, port=5001)