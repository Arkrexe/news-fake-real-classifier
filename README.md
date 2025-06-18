# 📰 News Article Fake/Real Classifier

This project classifies a news article as **Real** or **Fake** using machine learning and natural language processing (NLP).

## 📌 Problem Statement

Fake news spreads misinformation and impacts society. To combat this, we built a machine learning model that detects whether a news article is fake or real based on its content.

---

## 📁 Dataset

We used the **"Fake.csv"** and **"True.csv"** datasets from Kaggle.

- `Fake.csv` → Articles labeled as fake
- `True.csv` → Articles labeled as real

---

## 🛠️ Tech Stack & Tools Used

- Python
- Jupyter Notebook
- Scikit-learn
- NLTK
- Streamlit
- Pandas, NumPy

---

## ⚙️ How It Works

1. **Data Loading:** Combined `True.csv` and `Fake.csv` with a `label` column.
2. **Preprocessing:** Lowercased, removed punctuation, and stopwords.
3. **TF-IDF Vectorization:** Converted text to numerical features.
4. **Model Training:** Used Logistic Regression on 80/20 train-test split.
5. **Web App:** Streamlit app allows users to input any news article and get predictions instantly.

---

## 📦 Installation & Execution

```bash
# Clone the repository
git clone https://github.com/your-username/news-fake-real-classifier

# Navigate to project folder
cd news-fake-real-classifier

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

## 📂 Dataset Download

Due to GitHub file size limitations, you can download the datasets here:

- [Download True.csv (Google Drive)](https://drive.google.com/file/d/1oGe0PQYLwJ_6YAmTamAWIarL3lzv1B5R/view?usp=sharing)
- [Download Fake.csv (Google Drive)](https://drive.google.com/file/d/1E5RgxD_r4CYbMZJp69y-W39sewgEvAEg/view?usp=sharing)
