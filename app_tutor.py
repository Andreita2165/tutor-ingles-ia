import streamlit as st
import os
from google import genai
from google.genai import types

# --- 1. INTERFACE CONFIGURATION ---
st.set_page_config(
    page_title="🤖 Expert English Pedagogy Tutor",
    layout="wide"
)

st.title("🤖 Asistente Pedagógico de Inglés Técnico")
st.subheader("IA experta en Metodología de la Enseñanza y Taxonomía de Bloom")

# --- 2. API CONNECTION ---
try:
    # On the web (Streamlit Cloud), this will look for your "Secret" key
    API_KEY = os.environ.get("GEMINI_API_KEY")
    if not API_KEY:
        st.error("Error: API Key no encontrada. Configúrala en los 'Secrets' de Streamlit.")
        st.stop()
    
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    st.error(f"Error de conexión: {e}")
    st.stop()

# --- 3. THE PEDAGOGICAL BRAIN (Expert Teacher Methodology) ---
SYSTEM_INSTRUCTION = """
Eres un Asistente de Retroalimentación de Inglés (Nivel A2) con un Doctorado en Metodología de la Enseñanza del Inglés (ELT).
Tu rol es actuar como un Mentor Pedagógico especializado en Educación Técnico Profesional.

TUS REGLAS DE ORO:
1. IDIOMA: Responde EXCLUSIVAMENTE en ESPAÑOL.
2. MÉTODO SÁNDWICH: Comienza con una fortaleza (Elogio), sigue con las debilidades (Corrección) y termina con una meta (Motivación).
3. ANDAMIAJE (SCAFFOLDING): No solo des la respuesta, explica el 'por qué' de forma simple.
4. TAXONOMÍA DE BLOOM: Ayuda al alumno a subir del nivel de 'Recordar' al de 'Aplicar' y 'Analizar'.
5. TONO: Cercano, profesional y altamente motivador.
"""

# --- 4. TASK DEFINITION ---
CONSIGNA_FIJA = """
**TAREA:** Crea un Perfil Laboral que incluya: 3 Skills (adjetivos), 3 Duties (verbos de acción) y Disponibilidad.
"""
ESTANDAR_MODELO = """
**MODELO ESPERADO:** Skills: Organized, Fast, Responsible. Duties: Plan routes, Clean area, Pack boxes. Availability: Mon-Fri.
"""

# --- 5. STUDENT INTERFACE ---
st.markdown("---")
st.markdown(f"### 📝 Consigna para el Estudiante\n{CONSIGNA_FIJA}")

student_text = st.text_area(
    "Pega aquí tu trabajo en inglés:",
    height=150,
    placeholder="Ej: My skills is fast. I duties move boxes. I am available monday."
)

if st.button("🚀 Generar Retroalimentación Pedagógica"):
    
    if not student_text:
        st.warning("Por favor, ingresa el texto del alumno antes de procesar.")
        st.stop()
        
    # --- 6. DYNAMIC PROMPT (Logic & Color Formatting) ---
    PROMPT_USUARIO = f"""
    {CONSIGNA_FIJA}
    {ESTANDAR_MODELO}

    **ENTRADA DEL ESTUDIANTE:** "{student_text}"

    **TAREA PARA LA IA:**
    1. Evalúa el texto usando una rúbrica breve de 3 criterios.
    2. Crea una tabla con: Fortalezas, Debilidades (Errores), Recomendación Técnica y Puntaje (1-4).
    3. FORMATO CRÍTICO: En la sección de Debilidades, escribe los errores en color ROJO usando exactamente: <span style="color:red">ERROR AQUÍ</span>.
    4. CORRECCIÓN EXPLÍCITA: En 'Recomendación', muestra cómo se escribe correctamente la frase de forma simple.
    5. LIMITACIÓN: Sé conciso (máximo 100 palabras) para una respuesta rápida.
    
    RECUERDA: Todo el feedback debe estar en ESPAÑOL.
    """

    # --- 7. EXECUTION ---
    with st.spinner('Tu tutor experto está analizando el texto...'):
        try:
            response = client.models.generate_content(
                model='models\gemini-1.5-flash', # Fast & Smart
                contents=PROMPT_USUARIO,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION
                )
            )
            
            st.success("✅ Análisis Pedagógico Completado")
            # unsafe_allow_html=True is mandatory for the red color to work
            st.markdown(response.text, unsafe_allow_html=True)

        except Exception as e:

            st.error(f"Error al generar feedback: {e}")


