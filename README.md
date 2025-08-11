# 🎯 Pitch Perfect - Cricket Win Predictor

## 📌 Overview
**Pitch Perfect** is a data-driven cricket win prediction app that analyzes historical match data, player performance metrics, and match conditions to calculate the probability of a team winning or losing.  
Built with **Python** and **Streamlit**, the app delivers real-time insights, personalized predictions, and interactive simulations for cricket fans, coaches, commentators, and industry professionals.

---

## 👥 Actors & Users
- **End User/Fan** → View match predictions and stats to enhance their cricket viewing experience.
- **Coach/Team Management** → Analyze opposition strengths and weaknesses to make strategic decisions.
- **Media/Commentators** → Use predictions to enrich pre-match and live commentary.
- **Sponsors** → Leverage predictions for targeted marketing and promotional activities.

---


## 🛠️ Tech Stack

### **Frontend**
- **Streamlit** → For building an interactive, visually appealing, and responsive web interface.

### **Backend**
- **Python** → Core language for data analysis & ML model implementation.
- **Pandas**, **NumPy** → Data manipulation and numerical computation.
- **Scikit-learn** → Machine learning modeling and evaluation.

---

## 📂 Dataset
- **Name:** ODI_Match_Totals (2013–2019)
- **Description:** Total scores, match outcomes, and team stats from ODI cricket matches.
- **Purpose:** Train and validate ML models for win prediction.

---

## ⚙️ Code Flow / How It Works

1. **Data Collection** → Gather ODI match data (2013–2019).
2. **Data Preprocessing** → Handle missing values, encode categorical data.
3. **Train-Test Split** → Separate training and testing datasets.
4. **Model Training** → Use Support Vector Classifier (SVC) for outcome prediction.
5. **Evaluation** → Measure accuracy, precision, recall, and F1-score.
6. **Prediction** → Generate probability of win/loss for given inputs.
7. **UI Development** → Build with Streamlit for easy interaction.
8. **Deployment** → Host on a local/online server.
9. **Monitoring & Updates** → Continuously improve accuracy with fresh data.

---


# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
