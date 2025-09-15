from flask import Flask, request, render_template, jsonify
import joblib
import re
import numpy as np
from utils.preprocessing import preprocess_text, extract_advanced_features

# Flask app
app = Flask(__name__, template_folder="../frontend/templates", static_folder="../frontend/static")

# Load models
import joblib
nb_model = joblib.load("models/naive_bayes.pkl")
tfidf = joblib.load("models/tfidf.pkl")

# Home
@app.route("/")
def home():
    return render_template("index.html")

# Predict
@app.route("/predict", methods=["POST"])
def predict():
    text = request.form.get("essay")

    if not text:
        return jsonify({"error": "No text provided"}), 400
    

    # Preprocess
    clean_text = preprocess_text(text)

    # tf_idf
    text_tfidf = tfidf.transform([clean_text]).toarray()

    # Liguistic Features
    ling_feats = extract_advanced_features(text)
    ling_feats = np.array([list(ling_feats.values())])

    # Combine
    final_features = np.hstack([text_tfidf, ling_feats])

    # Predict
    pred = nb_model.predict(final_features)[0]
    proba = nb_model.predict_proba(final_features)[0]

    label = "Human Written"  if pred == 0 else "AI-generated"

    # Simplae explanation 
    explanation = {
        "avg_word_len": ling_feats[0][0],
        "vocab_richness": ling_feats[0][1],
        "stopword_ratio": ling_feats[0][9],
        "reason": "AI tends to have shorter avg words & higher repetition" if pred == 1 else "Human essays show richer vocab & varied sentence structure"
    }

    return jsonify({
        "prediction": label,
        "confidence_human" : round(proba[0]*100, 2),
        "confidence_ai": round(proba[1]*100, 2),
        "explanation": explanation
    })


if __name__ == "__main__":
    app.run(debug=True)