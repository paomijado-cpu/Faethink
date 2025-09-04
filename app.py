import streamlit as st

st.set_page_config(page_title="FaeThink", page_icon="🤖", layout="wide")

# Fundo branco completo
st.markdown(
    """
    <style>
    body {background-color: #ffffff;}
    .css-18e3th9 {background-color: #ffffff;}
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.markdown("<h1 style='text-align:center;color:#000;'>FaeThink 🤖</h1>", unsafe_allow_html=True)
st.write("Faça perguntas sobre escola, estágios, boletim, horários etc.")

# Base de conhecimento com palavras-chave
base_conhecimento = [
    {"keywords": ["estágio", "trabalho"], "resposta": "Você pode procurar estágio no setor de carreiras da escola ou no portal de estágio."},
    {"keywords": ["boletim", "notas"], "resposta": "O boletim pode ser acessado pelo portal do aluno usando seu login e senha."},
    {"keywords": ["horário", "aulas"], "resposta": "O horário completo das aulas está disponível no portal do aluno ou no quadro de horários."},
    {"keywords": ["secretaria", "contato"], "resposta": "Você pode falar com a secretaria pessoalmente ou enviar um e-mail para secretaria@escola.com."}
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

if st.button("Enviar") or pergunta_usuario:
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
        st.session_state.pergunta = ""

# Exibir histórico com balões ajustáveis
for usuario, mensagem in st.session_state.conversa:
    if usuario == "Você":
        st.markdown(f"""
            <div style="
                background-color:#4A90E2; 
                color:#000000; 
                font-weight:bold; 
                padding:10px; 
                border-radius:10px; 
                margin:5px 0; 
                display:inline-block; 
                max-width:70%; 
                float:right; 
                clear:both;">
                <b>Você:</b> {mensagem}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="
                background-color:#ADD8E6; 
                color:#000000; 
                font-weight:bold; 
                padding:10px; 
                border-radius:10px; 
                margin:5px 0; 
                display:inline-block; 
                max-width:70%; 
                float:left; 
                clear:both;">
                <b>FaeThink:</b> {mensagem}
            </div>
        """, unsafe_allow_html=True)