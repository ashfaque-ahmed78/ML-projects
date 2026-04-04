# app.py

import streamlit as st
import pickle
import docx
import PyPDF2
import re
import os

# =========================
# 🌟 Load the full model
# =========================
MODEL_PATH = "clf_full.pkl"  # This file contains model + tfidf + encoder

try:
    if not os.path.exists(MODEL_PATH):
        st.error(f"❌ Model file '{MODEL_PATH}' not found! Place it in the same folder as app.py")
        st.stop()
    with open(MODEL_PATH, 'rb') as f:
        data = pickle.load(f)

    svc_model = data['model']
    tfidf = data['tfidf']
    le = data['encoder']

except Exception as e:
    st.error(f"❌ Error loading model: {e}")
    st.stop()

# =========================
# ✨ Utility Functions
# =========================

def cleanResume(txt):
    """Clean resume text for prediction"""
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText

def extract_text_from_pdf(file):
    text = ''
    pdf_reader = PyPDF2.PdfReader(file)
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + '\n'
    return text

def extract_text_from_docx(file):
    text = ''
    doc = docx.Document(file)
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

def extract_text_from_txt(file):
    try:
        text = file.read().decode('utf-8')
    except UnicodeDecodeError:
        text = file.read().decode('latin-1')
    return text

def handle_file_upload(uploaded_file):
    ext = uploaded_file.name.split('.')[-1].lower()
    if ext == 'pdf':
        return extract_text_from_pdf(uploaded_file)
    elif ext == 'docx':
        return extract_text_from_docx(uploaded_file)
    elif ext == 'txt':
        return extract_text_from_txt(uploaded_file)
    else:
        raise ValueError("Unsupported file type! Upload PDF, DOCX, or TXT.")

def pred(input_resume):
    cleaned_text = cleanResume(input_resume)
    vectorized_text = tfidf.transform([cleaned_text]).toarray()
    predicted_category = svc_model.predict(vectorized_text)
    predicted_category_name = le.inverse_transform(predicted_category)
    return predicted_category_name[0]

# =========================
# 🌐 Streamlit App
# =========================
def main():
    st.set_page_config(page_title="📄 Resume Category Predictor 🚀", page_icon="📄", layout="wide")
    st.title("📄 Resume Category Prediction App")
    st.markdown("Upload a resume in **PDF**, **DOCX**, or **TXT** format and get the predicted job category 🎯.")

    uploaded_file = st.file_uploader("Upload a Resume 📂", type=["pdf", "docx", "txt"])
    if uploaded_file is not None:
        try:
            resume_text = handle_file_upload(uploaded_file)
            st.success("✅ Text extracted successfully!")

            # Optional: show extracted text
            if st.checkbox("Show extracted text 📖", False):
                st.text_area("Extracted Resume Text", resume_text, height=300)

            # Predict category
            st.subheader("🔮 Predicted Category")
            category = pred(resume_text)
            st.success(f"🎉 The predicted category is: **{category}**")

        except Exception as e:
            st.error(f"❌ Error processing file: {str(e)}")

if __name__ == "__main__":
    main()