import streamlit as st
import google.generativeai as genai

st.title("🤖 Mi Tutor de Inglés")

# Verificación de la Clave
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    
    # Usamos el nombre más estándar del modelo
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    user_input = st.text_input("Escribe algo en inglés:")
    
    if st.button("Corregir"):
        if user_input:
            try:
                response = model.generate_content(f"Corrige este texto: {user_input}")
                st.success(response.text)
            except Exception as e:
                st.error(f"Error de la IA: {e}")
        else:
            st.warning("Escribe algo primero.")
else:
    st.error("Error: No se encontró la GEMINI_API_KEY en Secrets.")
