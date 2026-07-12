from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    from courses.routes import courses_bp

    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(courses_bp)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from courses import models
        db.create_all()

    @app.errorhandler(404)
    def error_404(error):
        message = {
            "success": False,
            "error": 404,
            "name": "Not Found",
            "message": "The requested URL was not found on the server."
        }
        return jsonify(message), 404

    @app.errorhandler(500)
    def error_500(error):
        message = {
            "success": False,
            "error": 500,
            "name": "Internal Server Error",
            "message": "The server encountered an internal error and was unable to complete your request."
        }
        return jsonify(message), 500

    return app
