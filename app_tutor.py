import streamlit as st
import google.generativeai as genai

# Título de la App
st.title("🤖 Tutor de Inglés Técnico")

# 1. Configuración de la API con manejo de errores
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        
        # 2. Definir el modelo sin prefijos complicados
        # Esta es la forma más compatible de invocarlo
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        texto = st.text_area("Escribe aquí el texto del alumno:")
        
        if st.button("Generar Feedback"):
            if texto:
                with st.spinner("IA analizando..."):
                    # 3. Llamada directa y simple
                    response = model.generate_content(
                        f"Actúa como un profesor de inglés. Corrige este texto en español: {texto}"
                    )
                    st.markdown("### 📝 Resultado:")
                    st.write(response.text)
            else:
                st.warning("Por favor escribe algo.")
                
    except Exception as e:
        st.error(f"Error técnico: {e}")
else:
    st.error("No se encontró la clave GEMINI_API_KEY en Secrets.")
