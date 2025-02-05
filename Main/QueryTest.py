import streamlit as st
import requests
import re

# Set the page title and description
st.title("Life Advice Coach: Dr. James")
st.write("Enter your life advice question below, and receive a concise answer.")

# Define the base prompt with instructions for the model
base_prompt = (
    "You are a life advice coach named Dr. James. Below you wil receive a question from a client. You need to first address them and say that you are here to help."
    "Provide concise advice to their issue in three sentences that only addresses the client. Your advice should be clear, actionable, and empathetic."
    "Do not include any reasoning or thinking. Only produce the final answer after the word \"Advice:\"."
)

# Create a text input for the user question
user_question = st.text_input("Enter your question:")

# When the button is clicked, build the prompt and call the API
if st.button("Get Advice"):
    if user_question:
        # Combine the base prompt with the user's question
        full_prompt = f"{base_prompt}\nQuestion: {user_question}\nAdvice:"

        # Define the API endpoint and headers
        url = "http://localhost:11434/v1/completions"
        headers = {"Content-Type": "application/json"}

        # Create the data payload for the API request
        data = {
            "model": "deepseek-r1:7b",
            "prompt": full_prompt,
            "max_tokens": 250,
            "temperature": 0.4
        }

        # Make the POST request and handle the response
        try:
            response = requests.post(url, headers=headers, json=data)
            result = response.json()

            # Extract the generated text from the first choice
            raw_text = result["choices"][0]["text"]

            # Optionally, remove any <think> tags or extra formatting
            clean_text = re.sub(r'</?think>', '', raw_text).strip()

            advice = clean_text.split("Advice:")[1]

            # Display the advice to the user
            st.subheader("Advice from Dr. James:")
            st.write(advice)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question.")
