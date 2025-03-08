from langchain_core.prompts import PromptTemplate

insertion_prompt = PromptTemplate.from_template("""
You are an expert nutritionist. Based on the provided nutrient data, generate a **clear, engaging, and informative** description of the food item.

### **Food Details**
- **Name:** {name}
- **Nutrient Profile:** {nutrients}

### **What to Include in the Description**  
✅ **Macronutrient Breakdown**:  
   - Explain the **main macronutrients** (**proteins, fats, carbs**) and their **role in the body** (e.g., muscle growth, energy, metabolism).  
   - Highlight any **notable ratios** (e.g., "high-protein, low-fat" or "carb-heavy meal").  
✅ **Health Benefits**:  
   - Describe how this food **supports health goals** (e.g., **muscle recovery, weight loss, energy, heart health, digestion**).  
   - If relevant, warn about **high levels of unhealthy nutrients** (e.g., saturated fats, sugar, sodium).  
✅ **Key Vitamins & Minerals**:  
   - Mention any **important micronutrients** (e.g., calcium, iron, potassium) and how they benefit health.  
✅ **Dietary Suitability & Restrictions**:  
   - Indicate whether this food is **suitable for** **high-protein, keto, low-carb, vegan, gluten-free diets**.  
   - Highlight **potential allergens** (e.g., dairy, gluten, nuts).  
✅ **Best Use Cases & Consumption Timing**:  
   - Suggest **ideal consumption times** (**pre/post-workout, breakfast, snack, dinner**).  
   - If relevant, mention **cooking methods or pairing suggestions** (e.g., "Best served with vegetables for a balanced meal").  
✅ **Flavor & Texture (If Relevant)**:  
   - Briefly describe the food’s **taste and texture** if useful for the description.  

📌 **Write in a clear, engaging, and natural tone.**  
📌 **Keep it concise (5-6 sentences max).**  
📌 **Use only the provided nutrient data—do not invent or assume values.**  
📌 **Avoid technical jargon—make it understandable for everyday users.**
                                        
### **Description Example**
Mac and Cheese is a protein-rich dish (39.26g), making it a great option for muscle recovery and post-workout meals.
With 151.61g of carbohydrates, it provides quick energy, while 115.81g of fats (including 67.97g saturated fat) offer sustained fuel.
It is high in calcium (0.648g) and vitamin D (42 IU), promoting strong bones, but contains a significant amount of sodium (40.598g), which may be a concern for those with high blood pressure.
Not suitable for vegan or dairy-free diets, as it contains cheese, milk, and butter.
Best enjoyed as a comforting dinner or post-workout recovery meal, especially when paired with fiber-rich vegetables.

""")


simple_query_refinement_prompt = PromptTemplate.from_template(""""
"You are an expert in food and nutrition. Your task is to refine a **short and simple food-related query** into a **clear, structured format optimized for similarity search.**

### **User Query**
- **Original Query:** {query}

### **How to Refine the Query**
✅ **Reword the query to be precise, but do not change its meaning.**  
✅ **Use structured nutrition-related terminology** (e.g., "high-protein", "low-carb", "rich in fiber").  
✅ **Expand vague queries with necessary context** (e.g., "healthy snacks" → "nutritious low-calorie snacks high in fiber").  
✅ **Avoid unnecessary words or explanations**—keep it focused for search optimization.  

---

### **📌 Example Transformations**
| **Original Query**  | **Refined Query** |
|--------------------|------------------|
| "high protein food"  | "Foods rich in protein for muscle recovery." |
| "low-carb meal"  | "Nutritious meals low in carbohydrates and high in fiber." |
| "best food for energy"  | "Foods high in complex carbohydrates and proteins for sustained energy." |
| "vegan protein sources"  | "Plant-based protein-rich foods for vegans." |
| "low-fat breakfast"  | "Healthy breakfast options with low fat and high fiber." |

---

### **🚀 Refined Query Output:**  
- **Return only the refined query**, without extra explanation or formatting.
""")


complex_query_refinement_prompt = PromptTemplate.from_template(""""
"You are an expert nutritionist and food scientist. The user has asked a **complex question about food, health, or diet.** Your task is to **analyze the query, extract key constraints, and refine it into a structured format optimized for similarity search.**

---

### **User Query**
- **Original Query:** {query}

### **How to Refine the Query**
✅ **Identify the user’s primary goal** (e.g., weight loss, muscle building, energy, digestion, heart health).  
✅ **Extract all relevant nutrient constraints** (e.g., high protein, low fat, under 500 kcal, sugar-free).  
✅ **If the query involves comparisons**, simplify it into a **search-friendly format** (e.g., "compare chicken and fish" → "best lean protein sources for muscle growth").  
✅ **Avoid unnecessary explanations—just refine the query into a concise, structured format for retrieval.**  

---

### **📌 Example Transformations**
| **Original Query**  | **Refined Query** |
|--------------------|------------------|
| "Best food for diabetics with high protein and low sugar"  | "High-protein foods with low sugar content suitable for diabetics." |
| "Compare chicken and salmon for bodybuilding"  | "Best high-protein lean meats for muscle growth." |
| "Meal plan for weight loss and heart health"  | "Low-calorie, heart-healthy meals rich in fiber and healthy fats." |
| "What are some vegan foods that are good for energy?"  | "High-energy plant-based foods with complex carbohydrates." |
| "What foods should I avoid for high blood pressure?"  | "Foods high in sodium to avoid for blood pressure control." |

---

### **🚀 Refined Query Output:**  
- **Return only the refined query**, without extra explanation or formatting.
""")

rerank_query_prompt = PromptTemplate.from_template(
    """
You are a world-class nutrition expert. The user query is: "{user_query}"

Below is a JSON array of food items. Each item includes:
- "item_id": A unique identifier.
- "name": The food's name.
- Detailed nutritional metrics such as "Proteins", "Lipids/Fats", "Carbohydrates", "Energy/Calories", and other key nutrients.
- - A detailed description of the nutrient profile and the benefits of the food.

```json
{food_items}
```

Your task is to:
1. Analyze the nutritional data for each food item in the context of the user query.
2. Rank the food items from best to worst based on how well they meet the nutritional needs implied by the query.
3. Exclude any items that do not match the user's nutitional requirements.
4. Skip any items that are not relevant to the nutritional requirments of the query.
5. Return only a JSON array containing the "item_id"s of the food items in ranked order (best match first). Do not include any extra text.

For example, if the best matches are items with IDs 1, 3, and 2 and 2 is not matching the user's requirement, your output should be:
[1, 3]
"""
)
