# flask_databases
In this repository we will learn how to interact with Flask and Databases.

### what is modes.py file?
this is a file that is used to connect python classes to the database. we don't have database in pytohn, so we hvae to create a class, that then with the help object relation mapping(orm) connects pyton class with the database such as SQlAlchemy or MySQL or PostgreSQL.

For example we have a Persona class in python(model.py). It has its own attributes like Name, age, salary etc. So when we need to update those attributes in the database we will use `models.py` file to interact with DB.

So when we create a class in `models.py` we will import it into the app file, and when we create db instance in the app file we will import it into the `models.py` file.

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