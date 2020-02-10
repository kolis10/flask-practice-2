from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    date_of_birth = db.Column(db.String(10))
    email = db.Column(db.String(120))

    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "first name": self.first_name,
            "last name": self.last_name,
            "date of birth": self.date_of_birth,
            "email": self.email
        }
# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }