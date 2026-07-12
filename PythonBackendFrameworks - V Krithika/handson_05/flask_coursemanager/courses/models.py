from app import db

class Department(db.Model):
    __tablename__ = 'departments'
    name = db.Column(db.String(50), primary_key=True)
    head_of_dept = db.Column(db.String(50))
    budget = db.Column(db.Numeric(10, 2))
    courses = db.relationship('Course', back_populates='department')
    students = db.relationship('Student', back_populates='department')

    def __repr__(self):
        return f"<Department Name: {self.name}>"
    
    def to_dict(self):
        return {
            'name': self.name,
            'head_of_dept': self.head_of_dept,
            'budget': str(self.budget)
        }

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    code = db.Column(db.String(10), unique=True)
    credits = db.Column(db.Integer)
    department_name = db.Column(db.String(50), db.ForeignKey('departments.name'))
    department = db.relationship('Department', back_populates='courses')
    enrollments = db.relationship('Enrollment', back_populates='course')

    def __repr__(self):
        return f"<Course Name: {self.name}>"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'credits': self.credits,
            'department_name': self.department_name
        }
    
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    department_name = db.Column(db.String(50), db.ForeignKey('departments.name'))
    department = db.relationship('Department', back_populates='students')
    enrollment_year = db.Column(db.Integer)

    enrollments = db.relationship('Enrollment', back_populates='student')

    def __repr__(self):
        return f"<Student Name: {self.first_name} {self.last_name}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'department_name': self.department_name,
            'enrollment_year': self.enrollment_year
        }

class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    student = db.relationship('Student', back_populates='enrollments')
    course = db.relationship('Course', back_populates='enrollments')
    enrollment_date = db.Column(db.Date, default=db.func.current_date())
    grade = db.Column(db.String(2), nullable=True)

    __table_args__ = (
        db.UniqueConstraint('student_id', 'course_id', name='uq_student_course'),
    )

    def __repr__(self):
        return f"<Enrollment Student: {self.student} - Course: {self.course}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'enrollment_date': str(self.enrollment_date),
            'grade': self.grade
        }
    
