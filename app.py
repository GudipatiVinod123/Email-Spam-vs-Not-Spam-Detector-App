import streamlit as st
import pickle
st.markdown("""
<style>
/* Main background */
.stApp {
    background: linear-gradient(135deg, #fdfbfb, #ebedee);
}

/* Title card */
.title-card {
    background: linear-gradient(90deg, #667eea, #764ba2);
    padding: 25px;
    border-radius: 16px;
    text-align: center;
    color: white;
    font-size: 40px;
    font-weight: 800;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    margin-bottom: 20px;
}

/* Subtitle text */
.subtitle {
    text-align: center;
    color: #555;
    font-size: 16px;
    margin-bottom: 20px;
}

/* Text area styling */
textarea {
    border-radius: 12px !important;
    background-color: #f7f9fc !important;
}

/* Predict button */
.stButton > button {
    background: linear-gradient(90deg, #ff512f, #f09819);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 24px;
    border: none;
    box-shadow: 0 5px 12px rgba(0,0,0,0.2);
}

.stButton > button:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)
#title
st.markdown(
    '<div class="title-card">📧 Email Spam vs Not Spam Classifier</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Enter the email content to check whether it is SPAM or NOT SPAM using Machine Learning.</div>',
    unsafe_allow_html=True
)
#input box
email_text=st.text_area("Enter the email content here:", height=200)
#load model and vectorizer
with open("spam_classifier.pkl", "rb") as f:
    model = pickle.load(f)
with open("tfidf_vectorizer.pkl", "rb") as f:
    text_vec = pickle.load(f)

if st.button("Predict"):
    #vectorize the input
    email_vec=text_vec.transform([email_text])
    #train the model
    prediction=model.predict(email_vec)
    if prediction[0]==1:
        st.error("This email is classified as: SPAM 🚫" )
        st.error("Please be cautious while opening emails classified as SPAM. They may contain harmful content or phishing attempts.")
    else:
        st.success("This email is classified as: NOT SPAM ✅" )
        st.success("This email appears to be safe. However, always exercise caution when opening emails, especially if they contain links or attachments.")