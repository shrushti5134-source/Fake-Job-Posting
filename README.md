# Fake Job Posting Detection Using RNN

A Natural Language Processing and Deep Learning project that analyzes job posting text and classifies advertisements as **Genuine** or **Fraudulent** using a Recurrent Neural Network (RNN).

## Project Overview

Online job platforms can contain misleading or fraudulent job advertisements. This project explores how Natural Language Processing (NLP) and deep learning can help identify potentially fraudulent postings by analyzing their textual content.

The project includes a trained RNN model and an interactive Streamlit application where users can enter a job description and view its predicted class.

## Objectives

- Analyze job descriptions using NLP techniques.
- Clean and preprocess textual data.
- Convert text into numerical sequences using tokenization.
- Train an RNN model for binary text classification.
- Predict whether a job posting is genuine or fraudulent.
- Build an interactive application using Streamlit.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming |
| Pandas & NumPy | Data handling |
| TensorFlow / Keras | Deep learning |
| NLP | Text preprocessing |
| Scikit-learn | Data preparation and evaluation |
| Streamlit | Interactive application |
| Jupyter Notebook | Model development |

## Dataset Overview

The dataset contains **17,880 job postings**.

| Class | Number of records |
|---|---:|
| Genuine postings | 17,014 |
| Fraudulent postings | 866 |
| Total | 17,880 |

The dataset is imbalanced, with substantially fewer fraudulent postings than genuine ones. This is an important consideration when evaluating the model.

## Model Development

The project follows these steps:

1. **Data Preparation:** Load and inspect the job posting dataset.
2. **Text Preprocessing:** Clean and prepare the job description text.
3. **Tokenization:** Convert text into numerical sequences.
4. **Padding:** Standardize the input sequences to a length of 300 tokens.
5. **Model Training:** Train an RNN-based deep learning model.
6. **Prediction:** Classify job descriptions into genuine or fraudulent categories.
7. **Application:** Use Streamlit to provide an interactive prediction interface.

## Model Architecture

The RNN model uses the following layers:

- Embedding Layer
- SimpleRNN Layer
- Dropout Layer
- Dense Layer with ReLU activation
- Output Layer for binary classification

## Model Performance

The best recorded model accuracy during development was **95.16%**.

**Evaluation note:** Accuracy alone is not sufficient to establish fraud-detection performance, particularly because the dataset is imbalanced. Class-wise precision, recall, F1-score and a confusion matrix should also be evaluated before drawing conclusions about the model's ability to detect fraudulent postings.

## Project Structure

```text
Fake-Job-Posting/
│
├── RNN.ipynb
├── fake_app.py
├── rnn_model.keras
├── tokenizer.pkl
├── requirements.txt
└── README.md
```

## Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/shrushti5134-source/Fake-Job-Posting.git
cd Fake-Job-Posting
```

### 2. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run fake_app.py
```

### 5. Make a prediction

- Open the local URL displayed in the terminal.
- Enter or paste a job description.
- Submit it for analysis.
- View the predicted classification.

## Future Improvements

- Evaluate the model using precision, recall and F1-score.
- Analyze the confusion matrix and fraudulent-class recall.
- Explore class-imbalance handling techniques.
- Compare RNN performance with LSTM and GRU models.
- Improve text preprocessing and feature engineering.
- Deploy the application online.

## Limitations

- Predictions depend on the quality and coverage of the training dataset.
- Dataset imbalance can affect the model's ability to detect fraudulent postings.
- New fraud patterns and unfamiliar wording may affect predictions.
- A model prediction does not guarantee that a job posting is genuine or fraudulent.

Always verify job offers through official company websites and avoid paying upfront fees to secure employment.

## Author

**Shrushti Shelgave**

Computer Science Graduate | Aspiring Data Analyst | Machine Learning Enthusiast

[GitHub](https://github.com/shrushti5134-source) · [LinkedIn](https://www.linkedin.com/in/shrushti-shelgave-0287a234a/)

---

*This project was developed for educational and portfolio purposes.*
