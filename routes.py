from flask import render_template, request
from models import Person

def register_routes(app, db):
    @app.route('/')
    def index():
        people = Person.query.all()
        return render_template('index.html', people=people)

    @app.route('/add', methods=['POST'])
    def add_person():
        name = request.form['name']
        age = request.form['age']
        job = request.form['job']

        new_person = Person(name=name, age=age, job=job)
        db.session.add(new_person)
        db.session.commit()

        return 'Person added successfully!'