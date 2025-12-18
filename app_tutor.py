import streamlit as st
import requests

st.set_page_config(page_title="Tutor de Inglés", layout="centered")
st.title("🤖 Tutor de Inglés Técnico")

# 1. Recuperar la clave
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    user_input = st.text_area("Escribe en inglés:", placeholder="Ej: I is a student...")

    if st.button("Analizar"):
        if user_input:
            with st.spinner("Consultando al profesor virtual..."):
                # URL directa para saltarse librerías viejas
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
                
                payload = {
                    "contents": [{
                        "parts": [{"text": f"Actúa como profesor de inglés. Corrige este texto y explica los errores en español: {user_input}"}]
                    }]
                }
                
                try:
                    response = requests.post(url, json=payload)
                    data = response.json()
                    
                    if response.status_code == 200:
                        # Extraer la respuesta de la IA
                        resultado = data['candidates'][0]['content']['parts'][0]['text']
                        st.success("### Resultado:")
                        st.write(resultado)
                    else:
                        st.error(f"Error de Google: {data['error']['message']}")
                except Exception as e:
                    st.error(f"Error de conexión: {e}")
        else:
            st.warning("Escribe algo primero.")
else:
    st.error("Falta la clave GEMINI_API_KEY en los Secrets.")
