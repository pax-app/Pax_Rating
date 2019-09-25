from flask import request, jsonify, Blueprint

review_blueprint = Blueprint('review', __name__)


@review_blueprint.route('/reviews/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })
