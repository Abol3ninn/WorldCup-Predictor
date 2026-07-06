# 🌍 FIFA World Cup 2026 Match & Tournament Predictor

A machine learning project that predicts the outcomes of FIFA World Cup 2026 matches and simulates the remaining tournament to estimate the World Cup champion.

The project uses historical international football match data to train machine learning models capable of predicting match outcomes (Home Win, Draw, Away Win). The trained model is then used to simulate the knockout stage of the tournament from the current bracket.

---

## 🚀 Project Goals

- Predict the outcome of FIFA World Cup 2026 matches.
- Compare different machine learning algorithms.
- Simulate the remaining knockout tournament.
- Predict the most likely FIFA World Cup 2026 champion.
- Build a complete end-to-end machine learning pipeline.

---

## 📊 Dataset

Historical international football match results were used as the training dataset.

Main dataset:

- International football results (1872–2026)

The dataset contains:

- Match date
- Home team
- Away team
- Home goals
- Away goals
- Neutral venue indicator
- Tournament information

Only matches played before each prediction date are used to avoid data leakage.

---

## 🧠 Machine Learning Pipeline

```
Historical Match Results
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Training Dataset
        │
        ▼
Machine Learning Model
(Logistic Regression & XGBoost)
        │
        ▼
Future Match Prediction
        │
        ▼
Tournament Simulation
        │
        ▼
Predicted World Cup Champion
```

---

## ⚙️ Feature Engineering

For every match, statistics are generated using only matches played before the prediction date.

Current features include:

- Average goals scored (last 10 matches)
- Average goals conceded (last 10 matches)
- Win rate (last 10 matches)
- Goal difference
- Number of career matches played
- Neutral venue indicator

These features are generated independently for both teams.

---

## 🤖 Models

Two machine learning models were trained and compared.

### Logistic Regression

Used as the baseline model.

### XGBoost

Used as the final prediction model due to its better performance on structured tabular data.

---

## 📈 Model Evaluation

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

Example:

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 56.5% |
| XGBoost | *Coming Soon* |

---

## 🏆 Tournament Simulation

After training, the model predicts the remaining knockout matches.

The simulator automatically:

- predicts Round of 16 matches
- advances winners
- predicts Quarterfinals
- predicts Semifinals
- predicts the Final
- predicts the FIFA World Cup Champion

---

## 📁 Project Structure

```
WorldCup-Predictor/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── models/
│
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_baseline_model.ipynb
│   ├── 04_model_improvement.ipynb
│   ├── 05_tournament_simulation.ipynb
│
├── results/
│
├── src/
│
├── requirements.txt
│
└── README.md
```

---

## 💻 Technologies

- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Matplotlib
- Jupyter Notebook
- Joblib

---

## 📌 Future Improvements

Planned improvements include:

- FIFA World Ranking integration
- Elo Rating integration
- Team statistics dataset
- Hyperparameter tuning
- Monte Carlo tournament simulation
- Probability distribution for tournament winner
- Live Football API integration
- Interactive Streamlit web application

---

## 📷 Example Prediction

| Match | Home Win | Draw | Away Win | Prediction |
|--------|----------|------|----------|------------|
| Brazil vs Norway | 51.9% | 8.3% | 39.8% | Brazil |

---

## 👨‍💻 Author

Ahmed Abol3nin

Computer Science Student

Technische Hochschule Ulm

Interested in Artificial Intelligence, Machine Learning and Data Science.

---
