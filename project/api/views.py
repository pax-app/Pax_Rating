from flask import request, jsonify, Blueprint
from project.api.models import Review, Service
from sqlalchemy import exc
from database_singleton import Singleton
from project.api.utils.creation_utils import Utils 


review_blueprint = Blueprint('review', __name__)
service_blueprint = Blueprint('service', __name__)
db = Singleton().database_connection()
utils = Utils()

@review_blueprint.route('/create_review', methods=['POST'])
def add_service_review():
    post_data = request.get_json()

    if not post_data:
        return jsonify(utils.createFailMessage('Wrong JSON')), 400

    service_review = post_data.get('service_review')

    charisma_rate = service_review.get('charisma_rate')
    service_rate = service_review.get('service_rate')
    commentary = service_review.get('commentary')
    evaluator_id = service_review.get('evaluator_id')
    evaluated_id = service_review.get('evaluated_id')

    try:
        review = Review(charisma_rate, commentary, evaluator_id,
                  evaluated_id)
        utils.commit_to_database(review)
        service = Service(service_rate, evaluator_id, evaluated_id, review.review_id)
        utils.commit_to_database(service)
        return jsonify(utils.createSuccessMessage('A review was created!')), 201

    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(utils.createFailMessage('Wrong JSON')), 400


@review_blueprint.route('/average/<evaluated_id>', methods=['GET'])
def get_users_review_average(evaluated_id):
    response = {}

    try:
        reviews = Review.query.filter_by(evaluated_id=int(evaluated_id))

        if not reviews:
            return jsonify(utils.createFailMessage('Review not found for this user')), 404

        user_average = 0.0
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
        return jsonify(utils.createFailMessage('User not found')), 404

    return jsonify(response), 200


@service_blueprint.route('/average/<evaluated_id>', methods=['GET'])
def get_provider_service_review_average(evaluated_id):
    response = {}

    try:
        service_reviews = Service.query.filter_by(
            evaluated_id=int(evaluated_id))

        if not service_reviews:
            return jsonify(utils.createFailMessage('Service review not found for this provider')), 404

        provider_average = 0.0
        service_review_quantity = 0

        for service_review in service_reviews:
            provider_average += float(service_review.service_rate)
            service_review_quantity += 1

        if service_review_quantity == 0:
            return jsonify(utils.createFailMessage('Insufficient service reviews')), 400
        provider_average = provider_average / service_review_quantity

        response = {
            'status': 'success',
            'provider_id': evaluated_id,
            'provider_service_review_average': provider_average
        }

    except ValueError:
        return jsonify(utils.createFailMessage('Provider not found')), 404

    return jsonify(response), 200
