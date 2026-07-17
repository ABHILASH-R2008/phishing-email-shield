# 🚨 AI Phishing & Spam Shield

An intelligent, full-stack web application that leverages Machine Learning and Natural Language Processing (NLP) to proactively detect malicious phishing URLs and deceptive email spam before users fall victim to social engineering attacks.

## 🚀 Features
- **URL Analysis:** Uses a Decision Tree Classifier to scan link characteristics like raw IP structures, deceptive `@` symbol masking, and anomalous lengths.
- **Email Filtering:** Utilizes a Naive Bayes algorithm coupled with a text vectorizer to perform dynamic word-frequency scanning on email text.
- **Real-Time Web UI:** Features a responsive, dark-mode user interface powered by a Flask backend API to deliver instant safety verdicts.

## 🛠️ Tech Stack
- **Languages:** Python, JavaScript, HTML5, CSS3
- **Machine Learning / Data Science:** Scikit-Learn, Pandas, NumPy
- **Backend Framework:** Flask, Gunicorn