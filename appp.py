from flask import Flask, render_template, request, jsonify
import json
import random
import base64
import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from googletrans import Translator

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Load Model from JSON File
with open('chatbot_model.json', 'r', encoding='utf-8') as json_file:
    model_data = json.load(json_file)

# Decode and Load Model and Vectorizer
vectorizer = pickle.loads(base64.b64decode(model_data["vectorizer"].encode('utf-8')))
model = pickle.loads(base64.b64decode(model_data["model"].encode('utf-8')))
responses_dict = model_data["responses"]

# Initialize Flask app
app = Flask(__name__)

# Initialize the Translator
translator = Translator()

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_tokens)

def chatbot_response(user_input):
    preprocessed_input = preprocess_text(user_input)
    user_input_vector = vectorizer.transform([preprocessed_input])
    predicted_tag = model.predict(user_input_vector)[0]
    response = random.choice(responses_dict[predicted_tag])
    return response

@app.route("/")
def index():
    return render_template('cchatbot.html')

@app.route('/get_greeting', methods=['GET'])
def get_greeting():
    return "Hello, I'm a chatbot! How can I assist you today?"

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    target_language = request.form.get("lang", "en")  # Default to English if no language is specified

    # Get the response from the chatbot model
    response = chatbot_response(msg)

    # Translate the response to the target language
    try:
        translated_response = translator.translate(response, src='en', dest=target_language).text
    except Exception as e:
        print("Translation error:", e)
        translated_response = "Sorry, I couldn't translate the response."

    return jsonify({"response": translated_response})

if __name__ == '__main__':
    app.run(debug=True)
