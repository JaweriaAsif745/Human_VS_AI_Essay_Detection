# 🧠 Human vs AI Essay Classifier

A Flask-based web app that detects whether an essay is **AI-generated** or **human-written** using machine learning and natural language processing (NLP).

## 🚀 Features

* 🔍 Classifies essays as **Human** or **AI-generated**
* 📝 Simple and clean web interface built with Flask
* 📊 Machine Learning model trained on text features
* ⚡ Fast predictions with scikit-learn & NLP tools

## 🛠️ Tech Stack

* **Backend**: Flask
* **ML Libraries**: Scikit-learn, Naive Bayes, NLTK, Textstat
* **Visualization**: Matplotlib, Seaborn, WordCloud
* **Data Handling**: Pandas, NumPy

🎨 Web Interface
📝 Input Page

Users can paste or type an essay into the text box.

🤖 AI Essay

<img width="818" height="422" alt="input" src="https://github.com/user-attachments/assets/f6f6d5e9-ff33-410f-87c3-7c697e4143e0" />

✅ Human Essay

<img width="780" height="421" alt="human_text" src="https://github.com/user-attachments/assets/3f05b04a-b578-4688-807b-e62bedf60fc6" />


📊 Output Page

The system shows prediction, confidence scores, and reasoning.

✅ Human Essay Prediction

<img width="612" height="217" alt="positive output" src="https://github.com/user-attachments/assets/975514f5-c840-44ba-bb0f-71c4120a9305" />

🤖 AI Essay Prediction

<img width="610" height="221" alt="outpt" src="https://github.com/user-attachments/assets/dfabc878-e795-4826-9831-a7f0c7c5e0e5" />


## 📂 Project Structure

 ```bash
Human-vs-AI-Classifier/
│── backend/
│   ├── models/
│   │   ├── naive_bayes.pkl
│   │   └── tfidf.pkl
│   ├── utils/
│   │   └── preprocessing.py
│   └── app.py
│
│── frontend/
│   ├── static/
│   │   ├── images/
│   │   │   └── back-Pic.jpg
│   │   ├── style.css
│   │   └── script.js
│   └── templates/
│       ├── index.html
│       └── result.html
│
│── notebook/
│   └── Human_Vs_AI_Prediction_Model.ipynb
│
│── requirements.txt
└── README.md
 ```

## ⚙️ Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/JaweriaAsif745/Human_VS_AI_Essay_Detection.git
   cd Human-vs-AI-Classifier
   ```
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:

   ```bash
   python app.py
   ```
4. Open in browser:

   ```
   http://127.0.0.1:5000/
   ```

## 🎯 Future Improvements

* ✅ Improve model accuracy with deep learning (Transformers)
* ✅ Add plagiarism detection
* ✅ Deploy on cloud (Heroku / Render / AWS)

## 🤝 Contributing

Pull requests are welcome! If you’d like to improve the project, feel free to fork and submit changes.

## 📜 License

This project is licensed under the **MIT License**.

---

🔥 *"Built to explore the thin line between human creativity and artificial intelligence."*

