
import streamlit as st
from openai import OpenAI

st.title("ChatGPT Like")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Define modelo padrão
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Histórico de mensagens
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Exibe mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if prompt := st.chat_input("Whats is up?"):
    instructions = "Responda as perguntas do usuário de maneira informal"

    # Salva mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # Resposta do modelo
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": "system", "content": instructions},
                *st.session_state.messages
            ],
            stream=True,
        )

        response = st.write_stream(stream)

    # Salva resposta do assistente
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )