
import streamlit as st
import tensorflow as tf
import pickle
import numpy as np
from pathlib import Path
from tensorflow.keras.preprocessing.sequence import pad_sequences

# File paths
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "rnn_model.keras"
TOKENIZER_PATH = BASE_DIR / "tokenizer.pkl"

st.set_page_config(
    page_title="Fake Job Posting Detection",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 Fake Job Posting Detection")
st.write("Enter a job description to analyze it using your trained RNN model.")

@st.cache_resource
def load_artifacts():
    model = tf.keras.models.load_model(MODEL_PATH)

    with open(TOKENIZER_PATH, "rb") as f:
        tokenizer = pickle.load(f)

    return model, tokenizer

try:
    model, tokenizer = load_artifacts()
except Exception as e:
    st.error(f"Unable to load model or tokenizer: {e}")
    st.stop()

job_text = st.text_area(
    "Job Description",
    placeholder="Paste the job title, description, requirements, and responsibilities here...",
    height=250
)

if st.button("Analyze Job Posting", type="primary"):
    if not job_text.strip():
        st.warning("Please enter a job description.")
    else:
        sequence = tokenizer.texts_to_sequences([job_text])

        padded = pad_sequences(
            sequence,
            maxlen=50,
            padding="pre",
            truncating="pre"
        )

        prediction = model.predict(padded, verbose=0)
        predicted_class = int(np.argmax(prediction, axis=1)[0])
        confidence = float(np.max(prediction)) * 100

        st.subheader("Prediction")
        st.write(f"Predicted class index: {predicted_class}")
        st.write(f"Model score: {confidence:.2f}%")

        st.caption(
            "The displayed class index must be mapped to your original "
            "target labels. The model score is not necessarily a calibrated "
            "probability that the posting is genuine or fraudulent."
        )
