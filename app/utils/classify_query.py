import re

PATTERN_WEIGHTS = {
    r"(high|low|less|more|rich in|under|above)\s+(protein|fat|carbs|fiber|sodium|calories|iron|potassium|vitamin)": 1,  
    r"\b\d+\s?(g|mg|kcal)\b": 1,
    r"\b(best|healthy|good)\s+(snack|food|meal|drink)": 1,  

  
    r"\b(meal plan|diet plan|nutrition plan|balanced diet)\b": 3,  
    r"\b(avoid|exclude|without|free from)\s+\w+": 2,  
    r"\b(compare|which is better|alternative to)\b": 3,  
    r"\b(combination of|balance of|mix of)\b": 3,  
    r"\b(suitable for|ideal for|recommended for|good for)\s+\w+": 2,  

 
    r"\b(carbohydrates?|carbs?)\b": 1,  
    r"\b(calories?|energy|kcal)\b": 1,  
    r"\b(fats?|lipids?)\b": 1,  
    r"\b(proteins?)\b": 1,  

  
    r"\b(iron)\b": 2,  
    r"\b(calcium)\b": 2,  
    r"\b(fiber)\b": 1,  
    r"\b(potassium)\b": 2,  
    r"\b(sodium)\b": 2,  
    r"\b(cholesterol)\b": 2,  
    r"\b(sugars?)\b": 1,  

    
    r"\b(trans\s?fat|fatty\sacids,\stotal\strans)\b": 3,  
    r"\b(saturated\s?fat|fatty\sacids,\stotal\ssaturated)\b": 3,  
    r"\b(monounsaturated\s?fat|fatty\sacids,\stotal\smonounsaturated)\b": 3,  
    r"\b(polyunsaturated\s?fat|fatty\sacids,\stotal\spolyunsaturated)\b": 3,  

   
    r"\b(vitamin\s?([A-Z]))\b": 4,
}

THRESHOLD = 4 

def classify_query(query: str) -> str:
    """Classifies a query as 'simple' or 'complex' using a weighted regex-based heuristic."""
    
    query = query.lower().strip()
    score = 0

    for pattern, weight in PATTERN_WEIGHTS.items():
        if re.search(pattern, query):
            score += weight

    if score == 0:
        return "complex"

    if score < THRESHOLD:
        return "simple"
    return "complex"

