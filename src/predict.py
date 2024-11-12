import joblib

def load_model():
    model = joblib.load('../models/intent_model.h5')
    vectorizer = joblib.load('../models/vectorizer.pkl')
    return model, vectorizer

model, vectorizer = load_model()

def predict_intent(text):
    X = vectorizer.transform([text])
    return model.predict(X)[0]
