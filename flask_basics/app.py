# from project import create_app
from flask import Flask, redirect, url_for, render_template, request

class Todo:
    id = 0
    def __init__(self,title):
        Todo.id += 1
        self.id = Todo.id
        self.title = title
        self.complete = False

todo_list = []


# app = create_app()
app = Flask(__name__)

@app.route('/google')
def google():
    return redirect('https://www.google.com',)

@app.route('/<name>')
@app.route('/')
def index(name=None):
    return render_template('index.html',myname=name)

@app.route('/apiv2/home')
def home():
    print('I am from home')
    return redirect(url_for('index'))

@app.route('/user/<name>')
def user(name):
    return "This user name is "+name

@app.route('/todo')
def todo():
    return render_template('todo.html',todo_list=todo_list)

@app.route('/todo/add',methods=['POST'])
def add_todo():
    title = request.form["title"]
    todo = Todo(title)
    todo_list.append(todo)
    return redirect(url_for('todo'))

@app.route('/todo/update/<int:id>')
def update_todo(id):
    for todo in todo_list:
        if todo.id == id:
            todo.complete = True
            break
    return redirect(url_for('todo'))


if __name__ == "__main__":
    app.run()