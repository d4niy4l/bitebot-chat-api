"""
This module contains the function to convert the unit of the nutrient value to grams.
"""
def unit_convertor(value: float, unit: str) -> float:
    if unit == "MG" or unit == "mg":
        return value / 1000, "G"
    elif unit == "G" or unit == "g":
        return value, "G"
    elif unit == "kg" or unit == "KG":
        return value * 1000, "G"
    elif unit == "µg" or unit == "UG":
        return value / 1000000, "G"
    elif unit == "KCAL" or unit == "kcal":
        return value, "KCAL"
    return value, unit
    
