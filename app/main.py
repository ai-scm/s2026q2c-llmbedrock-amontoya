import streamlit as st
from chatbot import generate_response

st.set_page_config(
    page_title="AWS AI Practitioner Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AWS AI Practitioner Assistant")
st.caption(
    "Especialista en Generative AI, RAG y Large Language Models"
)

# Inicializar historial
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensaje de bienvenida (solo visual)
if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        st.markdown(
            "Hola. Soy tu asistente especializado en "
            "Generative AI, RAG y AWS AI Practitioner. "
            "¿Qué tema deseas estudiar hoy?"
        )

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capturar entrada
user_input = st.chat_input(
    "Escribe tu pregunta..."
)

if user_input:

    # Guardar mensaje usuario
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Mostrar mensaje usuario
    with st.chat_message("user"):
        st.markdown(user_input)

    # Obtener respuesta
    response = generate_response(
        st.session_state.messages
    )

    # Guardar respuesta
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    # Mostrar respuesta
    with st.chat_message("assistant"):
        st.markdown(response)