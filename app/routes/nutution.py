from flask import Blueprint, request, jsonify, current_app
from app.prompts.nutrition_guide_prompt import get_nutrition_prompt
from app.models.gemini_flash.model import get_model 
import json

get_nutrition = Blueprint('get_nutrition', __name__)

@get_nutrition.route('/nutrients/calculate', methods = ['POST'])
def get_nutrients_handler():
    data : str = request.get_json()
    
    product_items : str = data.get('product_items', '')
    
    if(product_items == ''):
        return jsonify({'message': 'No product list provided', 
                        'emotion': None, 
                        'success': False }), 400
    
    requirements = data.get('requirements', '')

    if(requirements == ''):
        return jsonify({'message': 'No requirements provided', 
                        'emotion': None, 
                        'success': False }), 400
    
    prompt = get_nutrition_prompt(product_items, requirements)
    
    model = get_model()

    response = model.generate_content(prompt)
    # Extract and clean the JSON array
    raw_response = response.text.strip()  # Remove leading/trailing whitespace
    try:
        # Remove code block markers and parse JSON
        clean_response = raw_response.strip("```json\n").strip("```")
        product_ids = json.loads(clean_response)  # Convert to Python list
        print("Matching Product IDs:", product_ids)
    except json.JSONDecodeError as e:
        print("Failed to decode response:", raw_response)
        print("Error:", e)

   

    return jsonify({
        'response': product_ids, 
        'message': 'Nutrients calculated successfully',
        'success': True
        }), 200

    
    

