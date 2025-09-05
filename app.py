import streamlit as st

st.set_page_config(page_title="FaeThink", page_icon="🎓", layout="wide")

# Estilos
st.markdown(
    """
    <style>
    .balao-usuario {
        background-color: #4A90E2; 
        color: #fff; 
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
        background-color: #E5E5EA; 
        color: #000; 
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
    /* Overlay */
    .overlay {
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background: rgba(0,0,0,0.4);
        backdrop-filter: blur(6px);
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 999;
    }
    .chatbox {
        background: #f9f9f9;
        width: 400px;
        max-height: 80%;
        border-radius: 15px;
        padding: 15px;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.3);
        overflow-y: auto;
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
    st.markdown("## 👋 Bem-vindo ao FaeThink!")
    st.write("Seu assistente especializado em FAETEC. Manda ver 😁!")

    if "abrir_chat" not in st.session_state:
        st.session_state.abrir_chat = False

    if st.button("💬 Abrir Chat"):
        st.session_state.abrir_chat = True

    # Overlay do chat
    if st.session_state.abrir_chat:
        st.markdown("<div class='overlay'><div class='chatbox'>", unsafe_allow_html=True)

        st.markdown("### 💬 Chat estilo WhatsApp")

        base_conhecimento = [
            {"keywords": ["estágio", "trabalho"], "resposta": "Você pode procurar estágio no setor de carreiras da escola, na sala ***."},
            {"keywords": ["boletim", "notas"], "resposta": "O boletim pode ser pego na secretaria após cada trimestre."},
            {"keywords": ["horário", "aulas"], "resposta": "O horário completo das aulas está disponível no mural da escola."},
            {"keywords": ["secretaria", "contato"], "resposta": "Você pode falar com a secretaria pessoalmente, assim que entrar na escola à esquerda."}
        ]

        if "conversa" not in st.session_state:
            st.session_state.conversa = []

        pergunta_usuario = st.text_input("Digite sua mensagem:")

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

        # Histórico de mensagens
        for usuario, mensagem in st.session_state.conversa:
            if usuario == "Você":
                st.markdown(f"<div class='balao-usuario'>{mensagem}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='balao-bot'>{mensagem}</div>", unsafe_allow_html=True)

        if st.button("❌ Fechar Chat"):
            st.session_state.abrir_chat = False

        st.markdown("</div></div>", unsafe_allow_html=True)

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

    # Projeto 1
    col1, col2 = st.columns([1,5])
    with col1:
        st.image("https://i.imgur.com/N2DeKr9.png", width=200)
    with col2:
        st.markdown("### Jornal A Voz do Republica 🤖")
        st.markdown("[📸 Instagram](https://www.instagram.com/avoz_republica/)")

    st.divider()

    # Projeto 2
    col1, col2 = st.columns([1,5])
    with col1:
        st.image("https://i.imgur.com/PAHqMhJ.png", width=200)
    with col2:
        st.markdown("### Projeto Multiplicadores 🎭")
        st.markdown("[📸 Instagram](https://www.instagram.com/alunomultiplicador/)")