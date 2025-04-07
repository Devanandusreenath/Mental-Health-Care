import nltk
import json
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import numpy as np
import base64
import pickle

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load Data from JSON File
with open('KB.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Extract patterns and responses
patterns = []
tags = []
responses_dict = {}

for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])
        if 'responses' in intent:
            responses_dict[intent['tag']] = intent['responses']
        else:
            responses_dict[intent['tag']] = ["I'm sorry, I don't have a response for that."]
    # responses_dict[intent['tag']] = intent['responses']

# Text Preprocessing Function
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_tokens)

# Preprocess patterns
preprocessed_patterns = [preprocess_text(p) for p in patterns]

# Feature Extraction
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_patterns)
y = np.array(tags)

# Train Model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Convert the trained model and vectorizer into a JSON-compatible format
model_data = {
    "vectorizer": base64.b64encode(pickle.dumps(vectorizer)).decode('utf-8'),
    "model": base64.b64encode(pickle.dumps(model)).decode('utf-8'),
    "responses": responses_dict
}

# Save Model to JSON File
with open('chatbot_model.json', 'w', encoding='utf-8') as json_file:
    json.dump(model_data, json_file, indent=4)
