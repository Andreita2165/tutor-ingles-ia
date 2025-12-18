import streamlit as st
from google import genai

# Configuración básica
st.set_page_config(page_title="Tutor de Inglés", layout="centered")
st.title("🤖 Tutor de Inglés Técnico")

# Conexión con la API
if "GEMINI_API_KEY" in st.secrets:
    try:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        
        texto = st.text_area("Escribe tu frase en inglés:", placeholder="Ej: I is a student...")

        if st.button("Corregir"):
            if texto:
                with st.spinner("Analizando..."):
                    # Usamos el modelo 1.5-flash que es el más compatible
                    response = client.models.generate_content(
                        model="gemini-1.5-flash", 
                        contents=f"Actúa como profesor de inglés. Corrige este texto y explica en español: {texto}"
                    )
                    st.success("### Resultado:")
                    st.write(response.text)
            else:
                st.warning("Por favor, escribe algo primero.")
                
    except Exception as e:
        st.error(f"Error de conexión: {e}")
else:
    st.error("No se encontró la GEMINI_API_KEY en los Secrets.")
