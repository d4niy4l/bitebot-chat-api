import httpx
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from app.config import NUTRITION_API_KEY, NUTRITION_API_URL
from .regexes import classify_nutrient_regex
from .unit_convertor import unit_convertor

EXPECTED_UNITS = {
    "Proteins": "G",  # Grams
    "Lipids/Fats": "G",  # Grams
    "Carbohydrates": "G",  # Grams
    "Energy/Calories": "KCAL",  # Kilocalories

    # Macronutrients
    "Sugar": "G",  # Grams
    "Fiber": "G",  # Grams
    "Cholesterol": "G",  # Grams
    "Trans Fat": "G",  # Grams
    "Saturated Fat": "G",  # Grams
    "Monounsaturated Fat": "G",  # Grams
    "Polyunsaturated Fat": "G",  # Grams

    # Minerals
    "Calcium": "G",  # Grams
    "Iron": "G",  # Grams
    "Potassium": "G",  # Grams
    "Sodium": "G",  # Grams

    # Vitamins (IU-based and Gram-based)
    "Vitamin A": "IU",  # International Units
    "Vitamin D": "IU",  # International Units
    "Vitamin C": "G",  # Grams
    "Thiamin": "G",  # Grams (Vitamin B1)
    "Riboflavin": "G",  # Grams (Vitamin B2)
    "Niacin": "G",  # Grams (Vitamin B3)
    "Folic acid": "G"  # Grams (Vitamin B9)
}


async def get_nutrition_data(ingredient : str):

    """
    This function fetches the nutrition data of the ingredient from the Nutrition API.
    Returns the nutrition data of the ingredient.
    Macro-nutrients are classified as per the regexes and the other nutrients are classified
    as "other".
    """
    with httpx.Client() as client:
        response = client.get(
            f"{NUTRITION_API_URL}",
            params={"api_key": NUTRITION_API_KEY, "query": ingredient}
        )
        if response.status_code == 200:
            data = response.json()
            nutrients = {}
            nutrition_data = data.get("foods", [])[0].get("foodNutrients", [])
            print("Size of nutrition data: ", len(nutrition_data))
            for nutrient in nutrition_data:
                nutrient_name = nutrient.get("nutrientName")
                nutrient_value = nutrient.get("value")
                nutrient_unit = nutrient.get("unitName")
                classified_nutrient = classify_nutrient_regex(nutrient_name)
                if isinstance(nutrient_value, float) or isinstance(nutrient_value, int):
                    standard_unit_value, standard_unit = unit_convertor(nutrient_value, nutrient_unit)
                else:
                    standard_unit_value, standard_unit = 0, nutrient_unit if nutrient_unit == "KCAL" else "G"
                nutrients[classified_nutrient] = {
                    "value": standard_unit_value,
                    "unit": standard_unit
                }
            return nutrients   
        else:
            raise HTTPException(
                status_code=response.status_code,
                detail=response.json()
            )   
        

