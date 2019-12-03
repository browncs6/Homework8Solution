#!/usr/bin/python3

from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'Blah blah blah'

todo_list = []

class AddForm(FlaskForm):
    name = StringField('Task Name', validators=[DataRequired()])
    notes = StringField('Task Notes')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def main_page():
    form = AddForm(method="POST")
    if form.validate_on_submit():
        name = form.name.data
        notes = form.notes.data
        form.name.data = ''
        form.notes.data = ''
        todo_list.append((name, notes))
    print("LOADING MAIN PAGE")
    print(todo_list)
    return render_template('todo.html', todo_list=todo_list, form=form)

@app.route('/remove', methods=['POST'])
def remove_todo():
    print(request.form)
    print(request.form.getlist("boxes"))
    boxes = request.form.getlist("boxes")
    if len(boxes) > 0:
        indices_to_remove = []
        for index in boxes:
            indices_to_remove.append(int(index))
        indices_to_remove.sort()
        indices_to_remove.reverse()
        for i in indices_to_remove:
            del todo_list[i]
    return redirect("/", code=302)


app.run()
