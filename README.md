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


## ⚙️ Installation

**1. Clone the repository**
```
git clone https://github.com/yourusername/Password-Strength-AI.git
cd Password-Strength-AI
```

**2. Create a virtual environment (recommended)**
```
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

**3. Install dependencies**
```
pip install -r requirements.txt
```

## 🧠 Training the Model

Before running the app, you need to generate data and train the model.

**1. Generate dataset**
```
python make_data.py
```

**2. Train the AI model**
```
python train.py
```

This will create a file model.pkl that the app uses for predictions.

## 🌐 Running the Web App

Start the Flask app:
```
python app.py
```

Open your browser at http://127.0.0.1:5000/ and test your passwords.

## 📊 Example Output

 - Input: `12345` → Weak, crack time < 1 second
 - Input: `H3ll0_World!` → Medium, crack time ~1 month
 - Input: `Th!sIsAV3ryStr0ngP@ssw0rd123` → Strong, crack time ~100+ years

## 🛠️ Technologies Used

 - Python 3.9+
 - Flask – Web framework
 - scikit-learn – Machine Learning model
 - pandas / numpy – Data handling


## 📌 Future Improvements

🔹 Real-time analysis as you type
🔹 Better datasets for stronger AI predictions
🔹 Add visualization of crack time distribution
🔹 Deploy online (Heroku, Render, or Vercel)

