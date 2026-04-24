from app import db


class Person(db.Model):
    __tablename__: str = 'people'
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f'Name: {self.name}, Age : {self.age}, Job: {self.job}'
