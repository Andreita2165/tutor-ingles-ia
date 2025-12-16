import streamlit as st
import google.generativeai as genai

# Configuración básica
st.set_page_config(page_title="Tutor de Inglés IA")
st.title("🤖 Asistente de Inglés Técnico")

# Conexión
if "GEMINI_API_KEY" not in st.secrets:
    st.error("Falta la API KEY en Secrets")
    st.stop()

# ESTA ES LA PARTE CLAVE:
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Probamos con el nombre corto del modelo que suele evitar el error 404
model = genai.GenerativeModel('gemini-1.5-flash')

texto = st.text_area("Pega aquí el texto del alumno:")

if st.button("Analizar"):
    if texto:
        with st.spinner("Analizando..."):
            try:
                # Quitamos configuraciones raras para ir a lo seguro
                response = model.generate_content(f"Actúa como tutor de inglés y corrige: {texto}")
                st.write(response.text)
            except Exception as e:
                st.error(f"Hubo un problema: {e}")
