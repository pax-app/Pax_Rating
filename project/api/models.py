from database import db
from project import create_app
from Flask import current_app


class Review(db.Model):
    __tablename__ = 'REVIEW'


class Service(db.Model):
    __tablename__ = 'SERVICE'
