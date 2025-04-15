# Use official Python image
FROM python:3.11-slim

# Declare build arguments
ARG GROQ_API_KEY
ARG GEMINI_API_KEY
ARG PINECONE_API_KEY
ARG NUTRITION_API_KEY
ARG NUTRITION_API_URL
ARG MISTRAL_API_KEY

# Set environment variables
ENV GROQ_API_KEY=${GROQ_API_KEY}
ENV GEMINI_API_KEY=${GEMINI_API_KEY}
ENV PINECONE_API_KEY=${PINECONE_API_KEY}
ENV NUTRITION_API_KEY=${NUTRITION_API_KEY}
ENV NUTRITION_API_URL=${NUTRITION_API_URL}
ENV MISTRAL_API_KEY=${MISTRAL_API_KEY}

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . .

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
