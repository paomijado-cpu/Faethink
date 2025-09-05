import streamlit as st

st.set_page_config(page_title="FaeThink", page_icon="🎓", layout="wide")

# Estilos
st.markdown(
    """
    <style>
    .balao-usuario {
        background-color: #4A90E2; 
        color: #000000; 
        font-weight: bold; 
        padding: 10px; 
        border-radius: 15px; 
        margin: 5px 0; 
        display: inline-block; 
        max-width: 70%; 
        float: right; 
        clear: both;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    .balao-bot {
        background-color: #ADD8E6; 
        color: #000000; 
        font-weight: bold; 
        padding: 10px; 
        border-radius: 15px; 
        margin: 5px 0; 
        display: inline-block; 
        max-width: 70%; 
        float: left; 
        clear: both;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }
    .titulo-gradient {
        text-align: center;
        background: linear-gradient(90deg, #4A90E2, #ADD8E6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 48px;
        font-weight: bold;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título principal
st.markdown("<h1 class='titulo-gradient'>FaeThink 🎓</h1>", unsafe_allow_html=True)

# Sidebar menu
menu = st.sidebar.radio("📌 Navegação", ["Chatbot", "Sobre o Projeto", "Projetos da Escola"])

# -------- CHATBOT --------
if menu == "Chatbot":
    st.markdown("### 🤖 Faça suas dúvidas sobre a escola. Sou especializado em Faetec. Manda ver 😁!")

    base_conhecimento = [
        {"keywords": ["estágio", "trabalho"], "resposta": "Você pode procurar estágio no setor de carreiras da escola, na sala ***."},
        {"keywords": ["boletim", "notas"], "resposta": "O boletim pode ser pego na secretaria após cada trimestre."},
        {"keywords": ["horário", "aulas"], "resposta": "O horário completo das aulas está disponível no mural da escola."},
        {"keywords": ["secretaria", "contato"], "resposta": "Você pode falar com a secretaria pessoalmente, assim que entrar na escola à esquerda."}
    ]

    if "conversa" not in st.session_state:
        st.session_state.conversa = []

    # Campo de input (sem sugestões)
    pergunta_usuario = st.text_input("Digite sua pergunta:")

    if st.button("Enviar"):
        if pergunta_usuario:
            pergunta_lower = pergunta_usuario.lower()
            resposta_bot = "Desculpe, não entendi sua pergunta 😅"

            for item in base_conhecimento:
                if any(k in pergunta_lower for k in item["keywords"]):
                    resposta_bot = item["resposta"]
                    break

            st.session_state.conversa.append(("Você", pergunta_usuario))
            st.session_state.conversa.append(("FaeThink", resposta_bot))

    for usuario, mensagem in st.session_state.conversa:
        if usuario == "Você":
            st.markdown(f"<div class='balao-usuario'><b>Você:</b> {mensagem}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='balao-bot'><b>FaeThink:</b> {mensagem}</div>", unsafe_allow_html=True)

# -------- SOBRE O PROJETO --------
elif menu == "Sobre o Projeto":
    st.markdown("## ℹ️ Sobre o FaeThink")
    st.write("""
    O **FaeThink 🎓** é um projeto criado para ajudar alunos da Faetec 
    a encontrarem informações rápidas sobre:
    - Estágios
    - Boletim
    - Horários
    - Secretaria

    Nosso objetivo é facilitar a vida dos estudantes com tecnologia acessível 🚀.
    """)

# -------- PROJETOS DA ESCOLA --------
elif menu == "Projetos da Escola":
    st.markdown("## 📢 Projetos da Escola")
    st.write("Aqui estão alguns projetos em andamento na nossa escola:")

    projetos = {
        "Jornal A Voz do Republica 🤖": "https://www.instagram.com/avoz_republica/",
        "Projeto Multiplicadores 🎭": "https://www.instagram.com/alunomultiplicador/"
    }

    for nome, link in projetos.items():
        st.markdown(f"🔹 **[{nome}]({link})**")