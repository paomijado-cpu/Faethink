import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="Faethink", page_icon="🎓", layout="wide")

# Fundo branco
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.markdown("<h1 style='text-align: center; color: #000;'>Faethink 🎓</h1>", unsafe_allow_html=True)
st.write("Faça perguntas sobre escola, estágios, boletim, horários etc.")

# Inicializa o histórico da conversa
if "conversa" not in st.session_state:
    st.session_state.conversa = []

# Perguntas rápidas
perguntas_rapidas = [
    "Onde posso arrumar estágio?",
    "Como acessar meu boletim?",
    "Qual o horário das aulas?",
    "Como falar com a secretaria?"
]

# Botões de perguntas rápidas
cols = st.columns(len(perguntas_rapidas))
for i, pergunta in enumerate(perguntas_rapidas):
    if cols[i].button(pergunta):
        st.session_state.pergunta = pergunta

# Campo de input
pergunta_usuario = st.text_input("Digite sua pergunta aqui:", value=st.session_state.get("pergunta", ""))

# Enviar pergunta
if st.button("Enviar") or pergunta_usuario:
    if pergunta_usuario:
        url = "https://api.gemini.com/v1/ai"  # ajuste conforme sua API
        headers = {
            "Authorization": "Bearer AIzaSyC_cZE-j8YyKNe07YbzJXFzNr7MJx3nyr8",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": pergunta_usuario,
            "model": "gemini-default",
            "max_tokens": 150
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            resposta_json = response.json()
            resposta_bot = resposta_json.get("text", "Não consegui gerar uma resposta 😅")
        except Exception as e:
            resposta_bot = f"Ocorreu um erro: {e}"

        st.session_state.conversa.append(("Você", pergunta_usuario))
        st.session_state.conversa.append(("Bot", resposta_bot))
        st.session_state.pergunta = ""

# Exibir histórico com balões azul
for usuario, mensagem in st.session_state.conversa:
    if usuario == "Você":
        st.markdown(f"""
            <div style="background-color:#4A90E2; color:#000000; font-weight:bold; padding:10px; border-radius:10px; margin:5px 0; width:60%; float:right; clear:both;">
                <b>Você:</b> {mensagem}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="background-color:#ADD8E6; color:#000000; font-weight:bold; padding:10px; border-radius:10px; margin:5px 0; width:60%; float:left; clear:both;">
                <b>Bot:</b> {mensagem}
            </div>
        """, unsafe_allow_html=True)