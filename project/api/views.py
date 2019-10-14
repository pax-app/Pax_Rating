from flask import request, jsonify, Blueprint
from project.api.models import Review, Service
from sqlalchemy import exc
from database import db


review_blueprint = Blueprint('review', __name__)
service_blueprint = Blueprint('service', __name__)


def createFailMessage(message):
    response_object = {
        'status': 'fail',
        'message': '{}'.format(message)
    }
    return response_object


def createSuccessMessage(message):
    response_object = {
        'status': 'success',
        'message': '{}'.format(message)
    }
    return response_object


@review_blueprint.route('/reviews/average/<evaluated_id>', methods=['GET'])
def get_users_review_average(evaluated_id):
    response = {}

    try:
        reviews = Review.query.filter_by(evaluated_id=int(evaluated_id))

        if not reviews:
            return jsonify(createFailMessage('Review not found for this user')), 404

        user_average = 0
        review_quantity = 0

        for review in reviews:
            user_average += float(review.charisma_rate)
            review_quantity += 1

        user_average = user_average / review_quantity

        response = {
            'status': 'success',
            'user_id': evaluated_id,
            'user_review_average': user_average
        }

    except ValueError:
        return jsonify(createFailMessage('User not found')), 404

    return jsonify(response), 200
