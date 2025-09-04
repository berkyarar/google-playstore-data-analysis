# Google Play Store Data Cleaning & Analysis

This project cleans and analyzes **Google Play Store application data** (`17-googleplaystore.csv`).  
The aim is to preprocess raw data, handle missing values, and generate meaningful insights about app categories,
installs, and ratings.

---

## 📌 Features

- **Data Cleaning**
    - Convert `Reviews`, `Size`, `Installs`, and `Price` into numeric values
    - Remove special characters (`+`, `,`, `$`)
    - Handle missing and inconsistent values (`Varies with device`, `NaN`)
    - Convert `Last Updated` into datetime format
    - Remove duplicate apps
- **Exploratory Data Analysis (EDA)**
    - KDE plots for numeric features
    - Count plots for categorical features
    - Heatmaps and correlations
- **Category & App Insights**
    - Total installs per category
    - Top 5 apps within selected categories
    - Highest rated apps (rating = 5.0)
- **Feature Engineering**
    - Target encoding for `Genres` based on average installs

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/username/google-play-analysis.git
   cd google-play-analysis

## 📂 Dataset

- File: `17-googleplaystore.csv`
- Source: Publicly available Google Play Store dataset (Kaggle / educational use)

## 📌 Note

This project is for **educational purposes**.  
