import requests
import json
import re

# Define the API endpoint and headers
url = "http://localhost:11434/v1/completions"
headers = {"Content-Type": "application/json"}

# Define your base prompt
base_prompt = "You are a life advice coach named Dr James. Please provide thoughtful, practical advice in a pargraph or less."

# Ask the user for their question
user_question = input("Enter your question for the life advice coach: ")

# Combine the base prompt with the user's question
# You can format it as you like—here, we're appending the question after the context.
full_prompt = f"{base_prompt}\nQuestion: {user_question}\nAdvice:"

# Create the data payload
data = {
    "model": "deepseek-r1:1.5b",
    "prompt": full_prompt,
    "max_tokens": 100,
    "temperature": 0.7
}

# Make the POST request
response = requests.post(url, headers=headers, json=data)

# Convert the response to a dictionary using .json()
result = response.json()

# Extract the text from the response
text = result["choices"][0]["text"]
clean_text = re.sub(r'</?think>', '', text).strip()

if "Advice:" in clean_text:
    final_answer = clean_text.split("Advice:")[-1].strip()
else:
    final_answer = clean_text

print(clean_text)