from typing import Literal

from flask import render_template, request
from models import Person


def register_routes(app, db) -> None:
    @app.route('/')
    def index() -> str:
        people = Person.query.all()
        return render_template('index.html', people=people)

    @app.route('/add', methods=['POST'])
    def add_person() -> Literal['Person added successfully!']:
        name: str = request.form['name']
        age: str = request.form['age']
        job: str = request.form['job']

        new_person = Person(name=name, age=age, job=job)
        db.session.add(new_person)
        db.session.commit()

        return 'Person added successfully!'
