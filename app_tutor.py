import streamlit as st
from google import genai

st.title("🤖 Tutor de Inglés Técnico")

# Configuración de la nueva librería
if "GEMINI_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    
    texto = st.text_area("Escribe en inglés:")
    
    if st.button("Analizar"):
        if texto:
            with st.spinner("Consultando a Gemini..."):
                try:
                    # Nueva forma de llamar al modelo (2.0 Flash)
                    response = client.models.generate_content(
                        model="gemini-2.0-flash", 
                        contents=f"Corrige este texto en español: {texto}"
                    )
                    st.success("### Resultado:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error técnico: {e}")
        else:
            st.warning("Por favor, escribe algo.")
else:
    st.error("Falta la clave API en Secrets.")
