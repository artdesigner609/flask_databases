from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# create a database object, so we can import it into models
db = SQLAlchemy()
migrate = Migrate()

# here with this function we create an applicaiton and returns its as a object.
# it means the app will not always run, when we import this app.py file


def create_app() -> Flask:
    app = Flask(__name__, template_folder='templates',
                static_folder='static', static_url_path='/')
    # here we will configure the string of the database, means where we are going to connect to?So, if it's not exist, it will create it.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask_tut_db'
    # then run flask db migrate - flask db upgrade
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    # migrate.init_app(app, db)

    from routes import register_routes
    register_routes(app, db)

    migrate = Migrate(app, db)

    return app
