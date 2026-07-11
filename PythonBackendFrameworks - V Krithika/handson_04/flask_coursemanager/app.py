from flask import Flask, app, jsonify
from config import Config
from courses.routes import courses_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(courses_bp)
    return app

if __name__ == '__main__':
    app = create_app()

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
    app.run(debug=False)
