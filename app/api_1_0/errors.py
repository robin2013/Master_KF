from flask import jsonify


def forbidden(message):
    response = jsonify({'error': 'forbidden', 'message': message})
    response.status_Code = 403
    return  response