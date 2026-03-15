import streamlit as st
import joblib

model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("SMS Spam Detector")

message = st.text_area("Enter an SMS message")

if st.button("Check"):
    if message.strip() == "":
        st.warning("Please enter a message")
    else:
        data = vectorizer.transform([message])
        prediction = model.predict(data)

        if prediction[0] == 1:
            st.error("Spam Message 🚨")
        else:
            st.success("Not Spam ✅")