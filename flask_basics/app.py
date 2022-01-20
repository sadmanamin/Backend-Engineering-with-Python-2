# from project import create_app
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
import os


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config.from_object

app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

cache = Cache(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    complete = db.Column(db.Boolean)

    def __init__(self,title,complete=False):
        self.title = title
        self.complete = complete

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/todo')
def todo():
    val = cache.get('todo_data')
    print(val)
    if val is not None:
        return val     
    todos = Todo.query.all()
    cache.set('todo_data',str(todos))
    # return render_template('todo.html',todo_list=todos)
    return str(todos)

@app.route('/todo/add',methods=['POST'])
def add_todo():
    title = request.form["title"]
    # todo = Todo(title)
    # todo_list.append(todo)
    todo = Todo(title)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('todo'))

@app.route('/todo/update/<int:id>')
def update_todo(id):
    # for todo in todo_list:
    #     if todo.id == id:
    #         todo.complete = True
    #         break
    todo = Todo.query.filter_by(id=id).first()
    todo.complete = True
    db.session.commit()
    return redirect(url_for('todo'))

@app.route("/todo/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo"))

@app.route('/todo/bulkadd')
def todo_bulkadd():

    for i in range(0,10000):
        todo = Todo('test'+str(i))
        db.session.add(todo)
    db.session.commit()
    return 'Done'


@app.route('/cache/<country>/<capital>')
def cache_set(country, capital):

    cache.set(country,{'country':capital})
    return 'Done'

@app.route('/cache/<country>')
def cache_get(country):
    resp = cache.get(country)
    print(resp)
    if resp is not None:
        return cache.get(country)
    else:
        return 'None'


if __name__ == "__main__":
    app.run()