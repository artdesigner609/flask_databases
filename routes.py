from typing import Literal

from flask import render_template, request
from models import Person


def register_routes(app, db) -> None:
    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            people = Person.query.all()
            # return str(people)
            return render_template('index.html', people=people)
        elif request.method == 'POST':
            pass

    @app.route('/add', methods=['POST'])
    def add_person() -> Literal['Person added successfully!']:
        name: str = request.form['name']
        age: int = request.form['age']
        job: str = request.form['job']

        new_person = Person(name=name, age=age, job=job)
        db.session.add(new_person)
        db.session.commit()

        return 'Person added successfully!'

    @app.route('/delete/<pid>', methods=['DELETE'])
    def delete(pid) -> str:

        # run query to delete a person with specific pid
        Person.query.filter(Person.pid == pid).delete()

        # comit the changes to the db
        db.session.commit()

        # fetch all person from db and show them on html template
        people = Person.query.all()
        return render_template('index.html', people=people)
