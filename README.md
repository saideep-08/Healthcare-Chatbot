# Healthcare Chatbot Project

This is a basic healthcare chatbot built with Python, Flask, and a simple intent classification model. Follow the steps in this project to develop a basic conversational chatbot that can detect intents and respond to user queries.

### Setup
- Install dependencies with `pip install -r app/requirements.txt`
- Run the app with `python app/app.py`

### Project Structure
- `data/`: Contains training data for intents
- `models/`: Stores trained models
- `src/`: Source code for preprocessing, training, and prediction
- `app/`: Flask app and front-end

### Usage
Send POST requests to `/predict` endpoint to get intent predictions.
