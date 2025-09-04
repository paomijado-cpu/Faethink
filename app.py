import streamlit as st

st.set_page_config(page_title="FaeThink", page_icon="🎓", layout="wide")

# Título da página inicial
st.title("🎓 Bem-vindo ao FaeThink")
st.markdown("""
Olá! Eu sou o **FaeThink**, um assistente especializado em **Faetec**.  
Escolha uma das opções abaixo para começar:
""")

# Layout em 2 colunas para os botões
col1, col2 = st.columns(2)

with col1:
    if st.button("🤖 Acessar Chatbot", use_container_width=True):
        st.switch_page("pages/chatbot.py")

with col2:
    if st.button("📂 Ver Projetos", use_container_width=True):
        st.switch_page("pages/projetos.py")