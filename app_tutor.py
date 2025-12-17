import streamlit as st
import google.generativeai as genai
import os

# CONFIGURACIÓN INICIAL
st.set_page_config(page_title="Tutor de Inglés Pro", layout="centered")
st.title("🤖 Asistente de Inglés Técnico")

# FORZAR VERSIÓN ESTABLE DE LA API (Esto elimina el error 404)
os.environ["GOOGLE_GENAI_USE_V1BETA"] = "0"

# CONFIGURACIÓN DE API
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    # Usamos el nombre completo del modelo
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    texto = st.text_area("Escribe aquí el texto en inglés:", placeholder="Ej: I is a professional...")
    
    if st.button("Obtener Feedback"):
        if texto:
            with st.spinner("Analizando con tecnología Pro..."):
                try:
                    response = model.generate_content(
                        f"Actúa como tutor de inglés. Corrige este texto y explica en español: {texto}"
                    )
                    st.markdown("### 📝 Retroalimentación:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error técnico: {e}")
        else:
            st.warning("Por favor, ingresa un texto.")
else:
    st.error("Configura tu GEMINI_API_KEY en los Secrets de Streamlit.")
