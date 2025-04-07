🔧 Features
💬 Intent-based response generation

🔍 Natural language preprocessing (tokenization, stopword removal)

✨ TF-IDF vectorization for feature extraction

🧠 Intent classification using Logistic Regression

🌐 Multilingual response translation with googletrans

🖥️ Real-time chat via a Flask web app

🎨 Styled front-end using custom CSS

📁 Project Structure
graphql
Copy
Edit
├── KB.json                 # Knowledge base with patterns and responses
├── chatbot_model.json      # Trained model, TF-IDF vectorizer, and responses
├── chatbot_train.py        # Script to train and save the chatbot model
├── app.py                  # Flask backend for the chatbot
├── templates/
│   └── cchatbot.html       # Front-end chat interface (HTML)
├── static/
│   └── style.css           # Custom CSS for chatbot UI
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
📚 How to Train the Chatbot
Create or modify the KB.json file in this format:

json
Copy
Edit
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": ["Hi", "Hello", "Hey there"],
      "responses": ["Hi!", "Hello!", "Hey! How can I help you?"]
    },
    ...
  ]
}
Run the training script:

bash
Copy
Edit
python chatbot_train.py
This generates the chatbot_model.json file containing the trained model and response data.

🚀 Running the Web App
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Then start the server:

bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000/ in your browser to interact with the chatbot.

🌐 Multilingual Support
The chatbot supports translating its responses to different languages.
Just pass a language code (like hi, fr, es, etc.) along with the message.

💻 Web Interface
The chat interface is built with HTML and styled using a CSS file (static/style.css).
You can customize the look and feel of your chatbot by editing this file.

📦 Requirements
nltk

scikit-learn

flask

googletrans==4.0.0-rc1

numpy

Install them with:

bash
Copy
Edit
pip install -r requirements.txt
🛠️ Future Enhancements
Use deep learning for better intent recognition

Add voice support (text-to-speech/speech-to-text)

Enable chat context and conversation history

Deploy to cloud platforms (Heroku, Render, etc.)
