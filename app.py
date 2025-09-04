import streamlit as st
import requests
import time

st.set_page_config(page_title="Chatbot Escolar", page_icon="🎓", layout="wide")

st.markdown("<h1 style='text-align: center;'>Chatbot Escolar 🎓</h1>", unsafe_allow_html=True)
st.write("Faça perguntas sobre escola, estágios, boletim, horários etc.")

# Inicializa o histórico da conversa
if "conversa" not in st.session_state:
    st.session_state.conversa = []

# Perguntas rápidas
perguntas_rapidas = [
    "Onde posso arrumar estágio? 🏢",
    "Como acessar meu boletim? 📄",
    "Qual o horário das aulas? ⏰",
    "Como falar com a secretaria? 📞"
]

# Botões de perguntas rápidas
cols = st.columns(len(perguntas_rapidas))
for i, pergunta in enumerate(perguntas_rapidas):
    if cols[i].button(pergunta):
        st.session_state.pergunta = pergunta

# Campo de input
pergunta_usuario = st.text_input("Digite sua pergunta aqui:", value=st.session_state.get("pergunta", ""))

# Função para chamar a API Gemini
def chamar_api(pergunta):
    url = "https://api.gemini.com/v1/ai"  # ajuste conforme a documentação da sua API
    headers = {
        "Authorization": "Bearer AIzaSyC_cZE-j8YyKNe07YbzJXFzNr7MJx3nyr8",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": pergunta,
        "model": "gemini-default",
        "max_tokens": 150
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        resposta_json = response.json()
        return resposta_json.get("text", "Não consegui gerar uma resposta 😅")
    except Exception as e:
        return f"Ocorreu um erro: {e}"

# Enviar pergunta
if st.button("Enviar") or pergunta_usuario:
    if pergunta_usuario:
        st.session_state.conversa.append(("Você", pergunta_usuario))
        st.session_state.pergunta = ""

        # Simula digitação do bot
        st.session_state.conversa.append(("Bot", "digitando..."))
        placeholder = st.empty()
        for i in range(3):
            placeholder.markdown(f"**Bot:** {'⏳' * (i+1)}")
            time.sleep(0.5)

        # Chama a API
        resposta_bot = chamar_api(pergunta_usuario)
        st.session_state.conversa[-1] = ("Bot", resposta_bot)

# Exibir histórico com avatar e balões
for usuario, mensagem in st.session_state.conversa:
    if usuario == "Você":
        st.markdown(f"""
            <div style="display:flex; justify-content:flex-end; margin:5px 0;">
                <div style="background-color:#DCF8C6; padding:10px; border-radius:10px; max-width:60%;">
                    <b>Você:</b> {mensagem} 🙂 
                </div>
                <img src="https://cdn-icons-png.flaticon.com/512/149/149071.png" width="40" style="margin-left:5px;">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="display:flex; justify-content:flex-start; margin:5px 0;">
                <img src="https://cdn-icons-png.flaticon.com/512/4712/4712011.png" width="40" style="margin-right:5px;">
                <div style="background-color:#FFF; padding:10px; border-radius:10px; border:1px solid #CCC; max-width:60%;">
                    <b>Bot:</b> {mensagem} 🤖
                </div>
            </div>
        """, unsafe_allow_html=True)