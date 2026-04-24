# Flask Databases with NeuralNine
[Course Video](https://youtu.be/oQ5UfJqW5Jo?si=sMXtZA_Dm79WR7Nn&t=7211)

In this repository we will learn how to interact with Databses in Flask application. Here we will use SQLAlchemy as our Database.

### what is modes.py file?
this is a file that is used to connect python classes to the database. we don't have database in python, so we have to create a class, then with it's help object relation mapping(ORM), we connect python class with the database such as SQlAlchemy or MySQL or PostgreSQL.

For example we have a Person class in python(model.py). It has its own attributes like Name, age, salary etc. So when we need to update those attributes in the database we will use `models.py` file to interact with DB and update our Db structure.

So, when we create a class in `models.py` we will import it into the app file, and then we create db instance in the app file, then we will import it into the `models.py` file.

we can create tables in the db and connect them with our app or we can create it in out `models.py` file.

### only do onces first time
```bash
flask db init
```
### and when we add any model, change db or do any change
```bash
flask db migrate
```
```bash
flask db upgrade
```