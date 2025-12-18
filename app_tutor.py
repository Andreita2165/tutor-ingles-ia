import streamlit as st
import requests

# Configuración de la página
st.set_page_config(page_title="Tutor de Inglés Técnico", layout="centered")

st.title("🤖 Mi Tutor de Inglés Técnico")
st.markdown("---")

# 1. Recuperar la clave desde los Secrets de Streamlit
api_key = st.secrets.get("GEMINI_API_KEY")

if api_key:
    st.write("Escribe una frase en inglés para recibir una corrección y explicación profesional.")
    
    # Área de texto para el usuario
    user_input = st.text_area("Texto a corregir:", placeholder="Ej: The system work fine yesterday...")

    if st.button("Analizar Texto"):
        if user_input:
            with st.spinner("El profesor virtual está revisando tu inglés..."):
                # URL estable de Google Gemini v1
                url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
                
                # Cuerpo del mensaje
                payload = {
                    "contents": [{
                        "parts": [{"text": f"Actúa como un profesor de inglés técnico. Corrige el siguiente texto y explica los errores gramaticales en español de forma educativa: {user_input}"}]
                    }]
                }
                
                try:
                    # Petición directa a Google
                    response = requests.post(url, json=payload)
                    data = response.json()
                    
                    if response.status_code == 200:
                        # Extraer respuesta
                        resultado = data['candidates'][0]['content']['parts'][0]['text']
                        st.success("### ✅ Corrección y Explicación:")
                        st.markdown(resultado)
                    
                    elif response.status_code == 429:
                        # Error de cuota (muy común en plan gratuito)
                        st.warning("⚠️ Google está limitando la velocidad por ser una cuenta gratuita. Por favor, espera exactamente 60 segundos y vuelve a presionar el botón.")
                    
                    else:
                        # Otros errores (como el 404 si la clave está mal)
                        msg = data.get('error', {}).get('message', 'Error desconocido')
                        st.error(f"Error de Google: {msg}")
                        st.info("Si el error es 'not found', por favor verifica que tu API Key sea nueva y esté en un 'New Project'.")
                
                except Exception as e:
                    st.error(f"Hubo un problema de conexión: {e}")
        else:
            st.warning("Por favor, escribe algo antes de analizar.")
else:
    st.error("⚠️ No se encontró la GEMINI_API_KEY.")
    st.info("Ve a los 'Settings' -> 'Secrets' de Streamlit Cloud y agrega tu clave así: GEMINI_API_KEY = 'tu_clave_aqui'")

st.markdown("---")
st.caption("Desarrollado con Google Gemini AI y Streamlit")
