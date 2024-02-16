from flask import Flask, render_template,request, redirect,url_for #imports necessary modules from Flask

app = Flask(__name__, template_folder="templates") # this line creates a Flask application instance

todos = [] # create empty list for to-do.

# this  function renders the index.html template and passes the todos list to the template.
@app.route('/')
def index():
    return render_template("index.html", todos=todos)

# this function retrieves the task and date from the form data, appends a new task item to the todos list, and redirects the user back to the home page.
@app.route('/add', methods=["POST"])
def add():
    todo = request.form['todo']
    dateoftask = request.form['dateoftask']
    todos.append({"task": todo, "done": False, "date": dateoftask})
    return redirect(url_for("index"))

# this route is used for editing to-do items.
# this function updates the task of the to-do item with the new task and then redirects the user back to the home page.
@app.route('/edit/<int:index>', methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)

# this route is used for marking to-do items as done.
# this function is executed when the user toggles the done status of the to-do item at the specified index
@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))

# this route is used for deleting to-do items.
# this function is executed when the user deletes the to-do item at the specified index from the todos list.
@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for("index"))

# start the application.
if __name__ == '__main__':
    app.run(debug=True)