from flask import Blueprint, jsonify, request

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses') 

@courses_bp.route('/', methods=['GET'])
def get_courses():
    return jsonify({})

@courses_bp.route('/<int:course_id>', methods=['GET'])
def get_course(course_id):
    return jsonify({})

@courses_bp.route('/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    return jsonify({})

@courses_bp.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    return jsonify({})

def make_response_json(data, status_code):
    load = {
        'status': 'success',
        'data': data
    }
    return jsonify(load), status_code

@courses_bp.route('/', methods=['POST'])
def create_course():
    if not request.is_json:
        return make_response_json({'error': 'Content-Type must be application/json'}, 400)
    req_data = request.get_json()
    if not req_data or 'name' not in req_data or 'code' not in req_data or 'credits' not in req_data:
        return make_response_json({'error': 'Invalid request data'}, 400)
    return make_response_json({'message': 'Course created successfully'}, 201)

