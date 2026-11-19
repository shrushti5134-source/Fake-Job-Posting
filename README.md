# 🔍 Fake Job Posting Detection Using Deep Learning

A Natural Language Processing (NLP) and Deep Learning project that uses a Recurrent Neural Network (RNN) to identify potentially fraudulent job advertisements. The project includes text preprocessing, model training, evaluation, and an interactive Streamlit web application.

## 🚀 Live Demo

**Try the application here:**

[Fake Job Posting Detection – Live Application](https://fake-job-posting-hswndkqvyksmsdt9bfzjyq.streamlit.app/)

## 📌 Project Overview

Online job portals contain both genuine and fraudulent job advertisements. Fake job postings can mislead job seekers, collect personal information, and expose applicants to employment scams.

This project aims to develop a deep learning-based text classification system that analyzes job descriptions and predicts whether a job posting is genuine or fraudulent.

The system uses an RNN architecture to learn sequential patterns from textual data and provides predictions through an interactive Streamlit application.

## 🎯 Objectives

- Analyze job descriptions using Natural Language Processing.
- Perform text preprocessing and tokenization.
- Convert textual data into numerical sequences.
- Develop an RNN-based deep learning model.
- Classify job postings based on fraudulent and genuine labels.
- Evaluate model performance.
- Deploy an interactive application using Streamlit.

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| NLP | Tokenization, Text Preprocessing |
| Deep Learning | TensorFlow, Keras |
| Model Architecture | Recurrent Neural Network (RNN) |
| Model Evaluation | Scikit-learn |
| Application Development | Streamlit |
| Development Environment | Jupyter Notebook |

## 📂 Project Structure

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

## ⚙️ Project Workflow

1. **Data Collection:** Load the fake job posting dataset.
2. **Data Preprocessing:** Handle missing values and prepare textual data.
3. **Text Cleaning:** Clean job descriptions and perform necessary text preprocessing.
4. **Tokenization:** Convert text into numerical sequences using a tokenizer.
5. **Sequence Padding:** Apply padding to maintain a maximum sequence length of 50 tokens.
6. **Model Development:** Build and train an RNN-based deep learning model.
7. **Model Evaluation:** Evaluate the trained model using test data.
8. **Deployment:** Develop an interactive Streamlit application for predictions.

## 🧠 Model Architecture

The project uses a Recurrent Neural Network (RNN) to process sequential textual information and identify patterns in job descriptions.

### Model Configuration

| Layer | Configuration |
|---|---|
| Embedding Layer | 64 dimensions |
| SimpleRNN Layer | 64 units |
| Dropout Layer | 0.3 |
| Dense Layer | 32 neurons, ReLU activation |
| Output Layer | 5 neurons, Softmax activation |

### Training Configuration

- Optimizer: Adam
- Loss Function: Categorical Crossentropy
- Batch Size: 32
- Epochs: 5
- Maximum Sequence Length: 50 tokens

**Technical note:** The notebook's current five-neuron output layer needs to be aligned with the two original target classes (genuine and fraudulent). The final binary classification architecture and metrics should be updated after correcting the label encoding and retraining.

## 📊 Model Performance

The current notebook experiment recorded the following test result:

| Evaluation Metric | Result |
|---|---:|
| Test Accuracy | 95.61% |

The recorded accuracy is preliminary and should not be considered the final validated performance until the output-layer and target-label mismatch is corrected.

### Additional Evaluation Metrics

The following metrics are planned for comprehensive evaluation:

- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

These metrics will help assess the model's ability to identify fraudulent job postings, particularly its performance on the fraudulent class.

## 💻 Streamlit Application

The project includes an interactive web application developed using Streamlit.

### Application Features

- Enter job posting text.
- Process textual input using the saved tokenizer.
- Generate predictions using the trained RNN model.
- Display the predicted class.
- Provide an interactive interface for users.

**Live Application:** [Open Fake Job Posting Detection](https://fake-job-posting-hswndkqvyksmsdt9bfzjyq.streamlit.app/)

## ▶️ Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/shrushti5134-source/Fake-Job-Posting.git
```

### 2. Navigate to the Project Directory

```bash
cd Fake-Job-Posting
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application

```bash
streamlit run fake_app.py
```

The application will open in your default web browser.

## 🔮 Future Improvements

- Correct the binary target encoding and output-layer configuration.
- Improve model evaluation using precision, recall, F1-score, and confusion matrix.
- Experiment with advanced recurrent architectures such as LSTM and GRU.
- Improve text preprocessing and feature extraction.
- Enhance prediction visualization and user experience.
- Evaluate model generalization using unseen job posting data.
- Explore transformer-based NLP models for improved text understanding.

## ⚠️ Disclaimer

This project is developed for educational and research purposes. Model predictions should not be considered definitive proof that a job advertisement is genuine or fraudulent. Users should independently verify job opportunities before sharing personal information or accepting offers.

## 👩‍💻 Author

**Shrushti Shelgave**

B.Sc. Computer Science Graduate | Aspiring Data Analyst | Data Science & AI/ML Enthusiast

- **GitHub:** [shrushti5134-source](https://github.com/shrushti5134-source)
- **LinkedIn:** [Shrushti Shelgave](https://www.linkedin.com/in/shrushti-shelgave-0287a234a/)

---

⭐ If you find this project interesting, consider giving the repository a star!
