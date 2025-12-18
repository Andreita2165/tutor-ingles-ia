import streamlit as st
from google import genai

# Configuración de la página
st.set_page_config(page_title="Tutor de Inglés Técnico", layout="centered")
st.title("🤖 Mi Tutor de Inglés")

# Verificación de Secrets
if "GEMINI_API_KEY" in st.secrets:
    try:
        # Iniciamos el cliente nuevo
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        
        texto = st.text_area("Escribe en inglés para corregir:", placeholder="Ej: I is a technician...")

        if st.button("Analizar"):
            if texto:
                with st.spinner("La IA está analizando tu texto..."):
                    # USAMOS GEMINI 2.0 FLASH (El modelo más nuevo y estable)
                    response = client.models.generate_content(
                        model="gemini-2.0-flash", 
                        contents=f"Actúa como profesor de inglés técnico. Corrige este texto y explica en español: {texto}"
                    )
                    st.success("### Resultado:")
                    st.write(response.text)
            else:
                st.warning("Por favor, escribe algo.")
                
    except Exception as e:
        # Si sale error 429, es por cuota. Si sale 404, es por el nombre del modelo.
        st.error(f"Error técnico: {e}")
else:
    st.error("⚠️ Configura la GEMINI_API_KEY en los Secrets de Streamlit."
