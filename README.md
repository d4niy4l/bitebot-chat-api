# BITE BOT CHAT API

The chat api for bitebot (The project for SDA Fall 2024)

## Stuff used

### MODEL USED FOR EMOTION ANALYSIS

**Emotion English DistilRoBERTa-base**
</br>
<https://huggingface.co/j-hartmann/emotion-english-distilroberta-base>

### MODEL USED FOR NUTRITIONAL ANALYSIS

**Google Gemini 1.5 Flash**
</br>
<https://ai.google.dev/gemini-api/docs?_gl=1%2A1xt7cso%2A_ga%2AMzA4MTY4OTg1LjE3MzI1NDE4NjY.%2A_ga_P1DBVKWT6V%2AMTczMjU3MDI2NC4zLjEuMTczMjU3MTc4OC41MS4wLjExMTI5MDgwNzE>.

## API SCHEMA

### Calculate Emotion

**Endpoint:** `/emotion/calculate`

**Method:** `POST`

**Request Body:**

```json
{
  "text": "Your text here"
}
```

**Response Body:**

```json
{
  "emotion": "Emotion result",
  "message": "Emotion calculated successfully",
  "success": true
}
```

### Calculate Nutrients

**Endpoint:** `/nutrients/calculate`

**Method:** `POST`

**Request Body:**

```json
{
  "product_items": "List of product items with ingredients",
  "requirements": "Nutritional requirements"
}
```

**Response Body:**

```json
{
  "response": [1, 2, 3],
  "message": "Nutrients calculated successfully",
  "success": true
}
```

#### Sample Request Body:

```json

{
  "requirements": "high protein",
  "product_items": "1. Apple Pie: Apples, sugar, flour, butter, cinnamon.\n2. Chicken Salad: Chicken, lettuce, mayonnaise, celery, grapes.\n3. Vegan Smoothie: Bananas, almond milk, spinach, chia seeds, protein powder."
}

```
