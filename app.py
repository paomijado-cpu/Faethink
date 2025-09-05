import streamlit as st

st.set_page_config(page_title="FaeThink", page_icon="🎓", layout="wide")

# ----------------------------- CSS -----------------------------
st.markdown("""
<style>
.titulo-gradient{
  text-align:center;
  background:linear-gradient(90deg,#4A90E2,#ADD8E6);
  -webkit-background-clip:text;
  -webkit-text-fill-color:transparent;
  font-size:48px;font-weight:700;padding:15px;border-radius:10px;
}
.chat-wrapper{
  background:#111B21;border-radius:12px;padding:12px;height:70vh;
  display:flex;flex-direction:column;gap:10px;border:1px solid #202C33;
}
.chat-scroll{
  flex:1;overflow-y:auto;padding-right:4px;
}
.balao-usuario{
  background:#005C4B;color:#fff;padding:10px;border-radius:10px 0 10px 10px;
  margin:6px 0;display:inline-block;max-width:70%;float:right;clear:both;
}
.balao-bot{
  background:#202C33;color:#EDEDED;padding:10px;border-radius:0 10px 10px 10px;
  margin:6px 0;display:inline-block;max-width:70%;float:left;clear:both;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------- Estado -----------------------------
if "pagina" not in st.session_state:
    st.session_state.pagina = "Início"
if "conversa" not in st.session_state:
    st.session_state.conversa = []

# ----------------------------- Sidebar -----------------------------
menu = st.sidebar.radio("📌 Navegação", 
    ["Início", "Sobre o Projeto", "Projetos da Escola"] + 
    (["Chatbot"] if st.session_state.pagina == "Chatbot" else []), 
    index=["Início", "Sobre o Projeto", "Projetos da Escola", "Chatbot"].index(st.session_state.pagina)
)

# ----------------------------- Título -----------------------------
st.markdown("<h1 class='titulo-gradient'>FaeThink 🎓</h1>", unsafe_allow_html=True)

# ----------------------------- Páginas -----------------------------
if menu == "Início":
    st.session_state.pagina = "Início"
    st.markdown("## 👋 Bem-vindo ao FaeThink!")
    st.write("Seu assistente especializado em FAETEC. Manda ver 😁!")

    if st.button("💬 Abrir Chat"):
        st.session_state.pagina = "Chatbot"
        st.experimental_rerun()

elif menu == "Chatbot":
    st.session_state.pagina = "Chatbot"
    st.markdown("## 💬 Chatbot")

    # Caixa do chat
    st.markdown("<div class='chat-wrapper'><div class='chat-scroll'>", unsafe_allow_html=True)

    # Histórico dentro da caixa
    for usuario, mensagem in st.session_state.conversa:
        classe = "balao-usuario" if usuario == "Você" else "balao-bot"
        st.markdown(f"<div class='{classe}'>{mensagem}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # fecha chat-scroll

    # Input do chat
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([8,1])
        with col1:
            pergunta = st.text_input("Digite sua mensagem:", label_visibility="collapsed")
        with col2:
            enviar = st.form_submit_button("Enviar")

    if enviar and pergunta:
        pergunta_lower = pergunta.lower()
        resposta = "Desculpe, não entendi sua pergunta 😅"

        base_conhecimento = [
            {"keywords": ["estágio", "trabalho"], "resposta": "Você pode procurar estágio no setor de carreiras da escola, na sala ***."},
            {"keywords": ["boletim", "notas"],  "resposta": "O boletim pode ser pego na secretaria após cada trimestre."},
            {"keywords": ["horário", "aulas"],  "resposta": "O horário completo das aulas está disponível no mural da escola."},
            {"keywords": ["secretaria", "contato"], "resposta": "Você pode falar com a secretaria pessoalmente, assim que entrar na escola à esquerda."}
        ]
        for item in base_conhecimento:
            if any(k in pergunta_lower for k in item["keywords"]):
                resposta = item["resposta"]
                break

        st.session_state.conversa.append(("Você", pergunta))
        st.session_state.conversa.append(("FaeThink", resposta))
        st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)  # fecha chat-wrapper

    # Botão voltar
    if st.button("⬅️ Voltar"):
        st.session_state.pagina = "Início"
        st.experimental_rerun()

elif menu == "Sobre o Projeto":
    st.session_state.pagina = "Sobre o Projeto"
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

elif menu == "Projetos da Escola":
    st.session_state.pagina = "Projetos da Escola"
    st.markdown("## 📢 Projetos da Escola")
    st.write("Aqui estão alguns projetos em andamento na nossa escola:")

    col1, col2 = st.columns([1,5])
    with col1:
        st.image("https://i.imgur.com/N2DeKr9.png", width=200)
    with col2:
        st.markdown("### Jornal A Voz do Republica 🤖")
        st.markdown("[📸 Instagram](https://www.instagram.com/avoz_republica/)")
    st.divider()

    col1, col2 = st.columns([1,5])
    with col1:
        st.image("https://i.imgur.com/PAHqMhJ.png", width=200)
    with col2:
        st.markdown("### Projeto Multiplicadores 🎭")
        st.markdown("[📸 Instagram](https://www.instagram.com/alunomultiplicador/)")