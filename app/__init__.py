from flask import Flask

def create_app():
    app = Flask(__name__)
    from app.routes import get_emotion
    app.register_blueprint(get_emotion)

    return app