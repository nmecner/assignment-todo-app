from flask import Flask, render_template
from wtforms import Form, StringField, validators
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient('mongodb://mongo:27017').todos
ToDoCollection = client.todo_items



@app.route('/')
def hello_world():


    return "hello world"

app.route('/dashboard')
def get_tasks():
    all_tasks = ToDoCollection.find()

    return render_template('index.html', todos=all_tasks)

@app.route('/add')
def add_task(doc):
    class NewTaskForm(Form):
        body = StringField('body', [validators.Length(min=4, max=70))
        due_date = StringField('due_date', [validators.Length(min=4, max=20))

    new_task = ToDoCollection.insertOne(doc)
    return render_template('added.html', new_task=new_task)


# class ArticleForm(Form):
#     title = StringField('Title', [validators.Length(min=1, max=200)])
#     body = TextAreaField('Body', [validators.Length(min=30)])

#change status
# x should be either done or undone
@app.route('/edit')
def update_status(id, x):
    task = ToDoCollection({id(id)}, {$set:{"status":"x"}});
    return render_template('edit.html', task=task)

@app.route('/overwrite')
def update_item_text(input):
    updated_task = ToDoCollection.update({id()}, {input});
    return render_template('edit.html', task=updated_task)

@app.route('/delete')
def delete_task():

#
# # add a task
# @app.route('/user-tasks', method=['POST'])
# def add():
#     db.todos.insert_one(
#         {
#         "body": body,
#         "dueDate": due
#         "category": category,
#         "status": status
#     })
#     return 'task added'
#
# # fetch all
# @app.route('/user-tasks', method='GET')
# def fetch_tasks():
#     return db.todos.find()
#
#
# # change status
# # x should be either done or undone
# @app.route('/edit', method='PUT')
# def update_status(x):
#     db.todos.update({id(o)}, {$set:{"status":"x"}});
#     return "task updated"
#
#
#
# # delete
# @app.route('/delete', method='DELETE')
# def delete_task():
#     request_data = request.get_json()
#     if




    # def delete_user():
    #     request_data = request.get_json()
    #
    #     if 'userEmail' in request_data:
    #         Database.delete_user(user_email=request_data['userEmail'])
    #     elif 'userId' in request_data:
    #         Database.delete_user(user_id=request_data['userId'])
    #     else:
    #         return jsonify({
    #             "status": "failed",
    #             "message": "you need to specify either the userEmail or userId"
    #         })
    #
    #     return jsonify({
    #         "status": "ok",
    #     })
    #
    #




# overwrite



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')