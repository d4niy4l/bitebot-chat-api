from flask import Blueprint, request, jsonify
from app.emotion_analyzer.emotion_analyzer import emotion_analyzer

get_emotion = Blueprint('get_emotion', __name__)

@get_emotion.route('/emotion/calculate', methods = ['POST'])
def get_emotion_handler():
    data = request.get_json()
    text = data.get('text', '')
    if(text == ''):
        return jsonify({'message': 'No text provided', 
                        'emotion': None, 
                        'success': False }), 400
    
    emotion = emotion_analyzer(text)
    return jsonify({
        'emotion': emotion, 
        'message': 'Emotion calculated successfully',
        'success': True
        }), 200