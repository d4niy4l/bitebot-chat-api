import re

NUTRIENT_REGEXES = {
    "Carbohydrates": r"\b(carbohydrates?|carbs?)\b",
    "Energy/Calories": r"\b(calories?|energy|kcal)\b",
    "Lipids/Fats": r"\b(fats?|lipids?)\b",
    "Proteins": r"\b(proteins?)\b",
    "Iron": r"\b(iron)\b",
    "Calcium": r"\b(calcium)\b",
    "Fiber": r"\b(fiber)\b",
    "Potassium": r"\b(potassium)\b",
    "Sodium": r"\b(sodium)\b",
    "Cholesterol": r"\b(cholesterol)\b",
    "Sugar": r"\b(sugars?)\b",
      "Trans Fat": r"\b(trans\s?fat|fatty\sacids,\stotal\strans)\b",
    "Saturated Fat": r"\b(saturated\s?fat|fatty\sacids,\stotal\ssaturated)\b",
    "Monounsaturated Fat": r"\b(monounsaturated\s?fat|fatty\sacids,\stotal\smonounsaturated)\b",
    "Polyunsaturated Fat": r"\b(polyunsaturated\s?fat|fatty\sacids,\stotal\spolyunsaturated)\b",
    "Vitamins": r"\bvitamin\s?([A-Z])\b", 
}

def classify_nutrient_regex(text):
    for nutrient, regex in NUTRIENT_REGEXES.items():
        match = re.search(regex, text, re.IGNORECASE)
        if match:
            if nutrient == "Vitamins":
                return f"Vitamin {match.group(1)}"  
            return nutrient

    return text
