def get_nutrition_prompt(food_items, requirements):
  prompt = f"""
  You are an expert in nutritional analysis and decision-making. You are tasked to analyze the user's nutritional requirements and the food items provided.
  Below are the food items with their ingredients:

  {food_items}

  The user has provided the following nutritional requirements:
  {requirements}

  Analyze the food items and return ONLY the IDs of the products that fully satisfy ALL the user's requirements. Format your response as a JSON array of IDs, such as: [2, 3].
  """

  return prompt