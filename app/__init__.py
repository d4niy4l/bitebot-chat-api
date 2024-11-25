from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv();
    app = Flask(__name__)
    app.debug = True
    app.config['GOOGLE_GEMINI_KEY'] = os.getenv('GOOGLE_GEMINI_KEY')
    
    from app.routes.calculate_emotion import get_emotion
    app.register_blueprint(get_emotion)

    from app.routes.nutution import get_nutrition
    app.register_blueprint(get_nutrition)

    return app