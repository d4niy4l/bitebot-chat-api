import google.generativeai as genai
from flask import current_app


def get_model():
  API_KEY = current_app.config['GOOGLE_GEMINI_KEY']
  genai.configure(api_key=API_KEY)
  model = genai.GenerativeModel('gemini-1.5-flash')
  return model
