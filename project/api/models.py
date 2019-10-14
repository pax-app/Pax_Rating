from database import db
from project import create_app
from Flask import current_app
import enum


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

    def __init__(self, review_id, charisma_rate, commentary, evaluator_id, evaluated_id):
        self.review_id = review_id
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
