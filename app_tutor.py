import streamlit as st
import google.generativeai as genai
import os

# Forzar versión estable
os.environ["GOOGLE_GENAI_USE_V1BETA"] = "0"

st.title("🤖 Tutor de Inglés")

if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Nombre de modelo ultra-específico
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    
    texto = st.text_area("Ingresa texto:")
    if st.button("Analizar"):
        try:
            response = model.generate_content(texto)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
