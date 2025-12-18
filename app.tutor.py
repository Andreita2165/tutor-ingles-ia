import streamlit as st
from google import genai

st.title("🤖 Tutor de Inglés Técnico")

if "GEMINI_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    
    texto = st.text_area("Escribe en inglés para corregir:")
    
    if st.button("Analizar"):
        if texto:
            with st.spinner("Conectando con el cerebro de la IA..."):
                try:
                    # USAMOS EL MODELO 1.5 FLASH QUE TIENE MÁS CUOTA
                    response = client.models.generate_content(
                        model="gemini-1.5-flash", 
                        contents=f"Actúa como profesor. Corrige este inglés y explica en español: {texto}"
                    )
                    st.success("### Análisis del Profesor:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.warning("Escribe algo primero.")
else:
    st.error("Configura la Clave API en los Secrets de Streamlit.")
