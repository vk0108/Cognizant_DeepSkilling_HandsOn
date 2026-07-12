from flask import Blueprint, jsonify, request
from app import db
from courses.models import Course, Student, Enrollment

courses_bp = Blueprint('courses', __name__, url_prefix='/api/courses') 

@courses_bp.route('/', methods=['GET'])
def get_courses():
    courses = db.session.execute(db.select(Course)).scalars().all()
    return jsonify([course.to_dict() for course in courses]), 200

@courses_bp.route('/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    if not course:
        return jsonify({'error': 'Course not found'}), 404
    return jsonify(course.to_dict()), 200

@courses_bp.route('/<int:course_id>/students', methods=['GET'])
def get_course_students(course_id):
    enrolled_students = db.session.query(Student).join(Enrollment).filter(Enrollment.course_id == course_id).all()
    if not enrolled_students:
        return jsonify({'error': 'No students found for this course'}), 404
    return jsonify([student.to_dict() for student in enrolled_students]), 200
    

@courses_bp.route('/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    req_data = request.get_json()
    if not req_data or 'name' not in req_data or 'code' not in req_data or 'credits' not in req_data:
        return jsonify({'error': 'Invalid request data'}), 400

    course.name = req_data['name']
    course.code = req_data['code']
    course.credits = req_data['credits']
    db.session.commit()
    return jsonify(course.to_dict()), 200

@courses_bp.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({'message': 'Course deleted successfully'}), 200

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
    course = Course(name=req_data['name'], code=req_data['code'], credits=req_data['credits'])
    db.session.add(course)
    db.session.commit()
    return make_response_json(course.to_dict(), 201)

