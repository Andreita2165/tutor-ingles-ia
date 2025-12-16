import streamlit as st
import google.generativeai as genai

# Configuración de la página
st.set_page_config(page_title="Tutor de Inglés IA", layout="centered")
st.title("🤖 Asistente de Inglés Técnico")

# Conexión Segura con los Secrets
if "GEMINI_API_KEY" not in st.secrets:
    st.error("⚠️ Configuración incompleta: Falta la clave API en los Secrets.")
    st.stop()

# Configurar el modelo (Usando 1.5-Flash para máxima estabilidad)
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel(model_name='gemini-1.5-flash')
except Exception as e:
    st.error(f"Error al configurar la IA: {e}")

st.info("Escribe una frase en inglés para recibir retroalimentación pedagógica.")
texto_alumno = st.text_area("Tu texto:", placeholder="Ej: I is a student from Chile...")

if st.button("Generar Retroalimentación"):
    if texto_alumno:
        with st.spinner("Analizando con IA..."):
            try:
                # Instrucción pedagógica clara
                prompt = f"Actúa como un mentor de inglés para estudiantes técnicos. Analiza el siguiente texto, corrige errores gramaticales resaltándolos y da consejos en español: {texto_alumno}"
                response = model.generate_content(prompt)
                
                st.markdown("### 📝 Retroalimentación:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Hubo un problema al generar la respuesta: {e}")
    else:
        st.warning("Por favor, escribe algo antes de presionar el botón.")
