from database_singleton import Singleton
from flask import request, jsonify
from project.api.models import Review, Service

db = Singleton().database_connection()


class Utils:
    def createFailMessage(self, message):
        response_object = {
            'status': 'fail',
            'message': '{}'.format(message)
        }
        return response_object

    def createSuccessMessage(self, message):
        response_object = {
            'status': 'success',
            'message': '{}'.format(message)
        }
        return response_object

    def commit_to_database(self, model):
        db.session.add(model)
        db.session.flush()
        db.session.commit()