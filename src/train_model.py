import json
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents data
with open('../data/intents.json') as f:
    data = json.load(f)

# Prepare data for training
texts = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        texts.append(pattern)
        labels.append(intent['tag'])

# Vectorize the text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train a model (logistic regression)
model = LogisticRegression()
model.fit(X, labels)

# Save the model and vectorizer
joblib.dump(model, '../models/intent_model.h5')
joblib.dump(vectorizer, '../models/vectorizer.pkl')

print("Model and vectorizer saved!")
