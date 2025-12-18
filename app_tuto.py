import streamlit as st
import google.generativeai as genai

# 1. Page Setup
st.set_page_config(page_title="Tutor de Inglés IA", layout="centered")
st.title("🤖 Asistente de Inglés Técnico")

# 2. Secure API Key Loading
if "GEMINI_API_KEY" in st.secrets:
    # FORCE THE API TO USE THE STABLE VERSION
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    
    # Using the most basic model name to avoid the 404 Beta error
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    texto = st.text_area("Escribe aquí el texto en inglés:", placeholder="Ej: I is a student...")
    
    if st.button("Analizar"):
        if texto:
            with st.spinner("Analizando..."):
                try:
                    # Direct call
                    response = model.generate_content(f"Corrige este inglés y explica en español: {texto}")
                    st.markdown("### 📝 Resultado:")
                    st.write(response.text)
                except Exception as e:
                    # This helps us see exactly what is happening
                    st.error(f"Error detectado: {e}")
                    st.info("Sugerencia: Intenta cambiar el modelo a 'gemini-pro' en el código si esto falla.")
        else:
            st.warning("Por favor, escribe algo.")
else:
    st.error("No se encontró la clave API en los Secrets.")
