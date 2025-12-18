import streamlit as st
from google import genai

st.title("🤖 Tutor de Inglés Técnico")

if "GEMINI_API_KEY" in st.secrets:
    # Creamos el cliente con la nueva librería
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    
    texto = st.text_area("Escribe en inglés:")
    
    if st.button("Corregir"):
        if texto:
            try:
                # Usamos gemini-2.0-flash que es el modelo más nuevo y no usa v1beta
                response = client.models.generate_content(
                    model="gemini-2.0-flash", 
                    contents=texto
                )
                st.success(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
