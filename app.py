import streamlit as st

st.set_page_config(page_title="FaeThink", page_icon="🤖", layout="wide")

# Estilos do chat e título
st.markdown(
    """
    <style>
    /* Balões do chat */
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

    /* Título com gradiente */
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

    /* Texto normal em preto e negrito */
    .texto-preto {
        color: #FFFFFF;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título topo com gradiente e emoji
st.markdown("<h1 class='titulo-gradient'>FaeThink 🎓</h1>", unsafe_allow_html=True)

# Descrição personalizada em preto negrito
st.markdown("<p class='texto-preto'>Sou especializado em Faetec. Manda ver😁!</p>", unsafe_allow_html=True)

# Base de conhecimento com palavras-chave
base_conhecimento = [
    {"keywords": ["estágio", "trabalho"], "resposta": "Você pode procurar estágio no setor de carreiras da escola, na sala ***."},
    {"keywords": ["boletim", "notas"], "resposta": "O boletim pode ser pego na secretaria após cada trimestre."},
    {"keywords": ["horário", "aulas"], "resposta": "O horário completo das aulas está disponível no mural da escola."},
    {"keywords": ["secretaria", "contato"], "resposta": "Você pode falar com a secretaria pessoalmente, assim que entrar na escola à esquerda."}
]

# Inicializa histórico da conversa
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
pergunta_usuario = st.text_input("Digite sua pergunta:", value=st.session_state.get("pergunta", ""))

# Enviar apenas com botão
if st.button("Enviar"):
    if pergunta_usuario:
        pergunta_lower = pergunta_usuario.lower()
        resposta_bot = "Desculpe, não entendi sua pergunta 😅"

        # Verifica palavras-chave
        for item in base_conhecimento:
            if any(k in pergunta_lower for k in item["keywords"]):
                resposta_bot = item["resposta"]
                break

        # Atualiza histórico
        st.session_state.conversa.append(("Você", pergunta_usuario))
        st.session_state.conversa.append(("FaeThink", resposta_bot))
        st.session_state.pergunta = ""  # limpa input após envio

# Exibir histórico com balões com sombras
for usuario, mensagem in st.session_state.conversa:
    if usuario == "Você":
        st.markdown(f"<div class='balao-usuario'><b>Você:</b> {mensagem}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='balao-bot'><b>FaeThink:</b> {mensagem}</div>", unsafe_allow_html=True)