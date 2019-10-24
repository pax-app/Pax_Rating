import enum
from database import db
from database_singleton import Singleton

db = Singleton().database_connection()

class Review(db.Model):
    __tablename__ = 'REVIEW'

    review_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    charisma_rate = db.Column(db.Enum('1', '2', '3', '4', '5'), nullable=False)
    commentary = db.Column(db.String(300), nullable=False)
    evaluator_id = db.Column(
        db.Integer, nullable=False)
    evaluated_id = db.Column(
        db.Integer, nullable=False)

    def __init__(self, charisma_rate, commentary, evaluator_id, evaluated_id):
        self.charisma_rate = charisma_rate
        self.commentary = commentary
        self.evaluator_id = evaluator_id
        self.evaluated_id = evaluated_id

    def to_json(self):
        return {
            'review_id': self.review_id,
            'charisma_rate': self.charisma_rate,
            'commentary': self.commentary,
            'evaluator_id': self.evaluator_id,
            'evaluated_id': self.evaluated_id
        }


class Service(db.Model):
    __tablename__ = 'SERVICE'

    review_service_id = db.Column(
        db.Integer, primary_key=True, autoincrement=True)
    service_rate = db.Column(db.Enum('1', '2', '3', '4', '5'), nullable=False)
    evaluator_id = db.Column(
        db.Integer, nullable=False)
    evaluated_id = db.Column(
        db.Integer, nullable=False)
    review_id = db.Column(
        db.Integer, db.ForeignKey('REVIEW.review_id'))

    def __init__(self, service_rate, evaluator_id, evaluated_id, review_id):
        self.service_rate = service_rate
        self.evaluator_id = evaluator_id
        self.evaluated_id = evaluated_id
        self.review_id = review_id

    def to_json(self):
        return {
            'review_id': self.review_id,
            'review_id': self.review_id,
            'evaluator_id': self.evaluator_id,
            'evaluated_id': self.evaluated_id,
            'review_id': self.review_id
        }
