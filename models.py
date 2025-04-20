import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

def train_model(X, y):
    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression()
    model.fit(X_vec, y)

    with open("saved_models/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)
    with open("saved_models/classifier.pkl", "wb") as f:
        pickle.dump(model, f)

def classify_email(text):
    with open("saved_models/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    with open("saved_models/classifier.pkl", "rb") as f:
        model = pickle.load(f)

    X_vec = vectorizer.transform([text])
    return model.predict(X_vec)[0]
