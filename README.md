# Fake Job Posting Detection Using RNN

## 📌 Project Overview

This project uses Deep Learning and Natural Language Processing (NLP) to analyze job posting text and predict its category using a Recurrent Neural Network (RNN).

The goal is to help identify potentially fraudulent job advertisements and support safer job searching.

## 🎯 Objectives

- Analyze job descriptions using NLP techniques.
- Preprocess text data for deep learning.
- Train an RNN model to classify job postings.
- Predict the class of a job posting entered by a user.
- Build an interactive web application using Streamlit.

## 🛠️ Technologies Used

- **Python** — Programming language
- **Pandas & NumPy** — Data manipulation
- **TensorFlow / Keras** — Deep learning model
- **NLP** — Text preprocessing and tokenization
- **Scikit-learn** — Data preparation and model evaluation
- **Streamlit** — Interactive web application
- **Jupyter Notebook** — Model development and experimentation

## 📂 Project Structure

```text
Fake-Job-Posting-Detection/
│
├── RNN.ipynb
├── fake_job_postings.csv
├── fake_app.py
├── rnn_model.keras
├── tokenizer.pkl
├── README.md
└── requirements.txt
```

*Note: Update the filenames and dataset extension to match your actual files.*

## ⚙️ How It Works

1. **Data Collection:** Load a dataset containing job posting information and labels.
2. **Data Preprocessing:** Clean and prepare the job description text.
3. **Tokenization:** Convert words into numerical sequences.
4. **Padding:** Standardize input sequences to a fixed length of 50 tokens.
5. **Model Training:** Train an RNN-based neural network using an embedding layer, SimpleRNN layer, dropout, and dense layers.
6. **Prediction:** Process user-entered job descriptions and predict the output class.
7. **Deployment:** Use Streamlit to provide a simple interface for testing job postings.

## 🧠 Model Architecture

The trained neural network contains:

- Embedding Layer
- SimpleRNN Layer
- Dropout Layer
- Dense Layer with ReLU activation
- Output Dense Layer with 5 classes

The model learns patterns in job posting text to predict one of five output classes. The meaning of each class depends on the original dataset labels and must be mapped accordingly.

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Fake-Job-Posting-Detection
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Launch the Streamlit application

```bash
streamlit run fake_app.py
```

### 4. Test a job posting

- Open the local Streamlit URL displayed in your terminal.
- Paste a job description into the text area.
- Click **Analyze Job Posting**.
- Review the predicted class and model score.

## 📊 Model Evaluation

The model should be evaluated using appropriate classification metrics, including:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

For fraud detection, recall for the fraudulent class is especially important because missed fraudulent postings can expose job seekers to risk.

*Add your actual evaluation results here after testing the model.*

## 💡 Future Improvements

- Improve text preprocessing and feature selection.
- Compare RNN performance with LSTM and GRU models.
- Add a clear mapping from predicted class indices to original labels.
- Display class-specific confidence scores.
- Evaluate performance on unseen job postings.
- Deploy the Streamlit application online.

## ⚠️ Limitations

- Predictions depend on the training dataset and model performance.
- A prediction is not proof that a job posting is genuine or fraudulent.
- Unseen wording, new scam techniques, and dataset bias may affect results.
- The model's output classes must be interpreted using the original label mapping.

Always verify job offers through official company websites, and never pay upfront fees to secure employment.

## 👩‍💻 Author

**Shrushti Shelgave**

Computer Science Graduate | Aspiring Data Analyst | Machine Learning Enthusiast

## 📄 License

This project is intended for educational and portfolio purposes. Add an appropriate license if you plan to distribute the code publicly.
