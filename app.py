import streamlit as st
import requests

# Configuração da página
st.set_page_config(page_title="FaeThink", page_icon="🤖", layout="wide")

# Fundo branco completo
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    .css-18e3th9 {  /* main content area */
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.markdown("<h1 style='text-align: center; color: #000;'>FaeThink 🤖</h1>", unsafe_allow_html=True)
st.write("Faça perguntas sobre escola, estágios, boletim, horários etc.")

# Base de conhecimento
base_conhecimento = {
    "onde posso arrumar estágio?": "Você pode procurar estágio no setor de carreiras da escola ou no portal de estágio da prefeitura.",
    "como acessar meu boletim?": "O boletim pode ser acessado pelo portal do aluno, usando seu login e senha.",
    "qual o horário das aulas?": "O horário completo das aulas está disponível no quadro de horários ou no portal do aluno.",
    "como falar com a secretaria?": "Você pode ir pessoalmente à secretaria ou enviar um e-mail para secretaria@escola.com."
}

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
pergunta_usuario = st.text_input("Digite sua pergunta aqui:", value=st.session_state.get("pergunta", ""))

# Enviar pergunta
if st.button("Enviar") or pergunta_usuario:
    if pergunta_usuario:
        # Checa base de conhecimento
        pergunta_lower = pergunta_usuario.lower()
        resposta_base = base_conhecimento.get(pergunta_lower, None)

        if resposta_base:
            prompt_para_ai = f"Reescreva de forma clara e amigável esta resposta escolar: {resposta_base}"
        else:
            prompt_para_ai = pergunta_usuario  # deixa IA responder normalmente

        url = "https://api.gemini.com/v1/ai"  # ajuste conforme sua API
        headers = {
            "Authorization": "Bearer AIzaSyC_cZE-j8YyKNe07YbzJXFzNr7MJx3nyr8",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt_para_ai,
            "model": "gemini-default",
            "max_tokens": 150
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            resposta_json = response.json()
            st.write("DEBUG JSON da resposta:", resposta_json)  # DEBUG: veja a estrutura retornada

            # Tenta pegar o campo correto da resposta
            if "text" in resposta_json:
                resposta_bot = resposta_json["text"]
            elif "output" in resposta_json and len(resposta_json["output"]) > 0:
                resposta_bot = resposta_json["output"][0].get("content", "Não consegui gerar uma resposta 😅")
            else:
                resposta_bot = "Não consegui gerar uma resposta 😅"

        except Exception as e:
            resposta_bot = f"Ocorreu um erro: {e}"

        # Atualiza histórico
        st.session_state.conversa.append(("Você", pergunta_usuario))
        st.session_state.conversa.append(("Bot", resposta_bot))
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