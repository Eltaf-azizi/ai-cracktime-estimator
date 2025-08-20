<h1 align="center">AI Cracktime Estimator (AI Twist)</h1>

An AI-powered tool that predicts how long it would take to crack a given password.
This project uses machine learning to estimate crack time based on password features such as length, complexity, and character variety.
It includes a Flask web app with a simple UI to test password strength in real-time.



## 🚀 Features

 - ✅ AI model trained on a synthetic password dataset
 - ✅ Predicts estimated crack time for any password
 - ✅ Flask-powered web interface
 - ✅ Password strength categories (Weak / Medium / Strong)
 - ✅ Simple & lightweight (scikit-learn + Flask)

## 📂 Project Structure
    Password-Strength-AI/
    │── app.py              # Flask web app
    │── train.py            # Model training script
    │── make_data.py        # Generate synthetic dataset
    │── model.pkl           # Saved ML model (generated after training)
    │── requirements.txt    # Dependencies
    │── README.md           # Project documentation
