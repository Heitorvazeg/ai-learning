import os
import re
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import StateGraph, END

load_dotenv()

os.environ.get("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7
)

template_text = (
    "Você é o TechAdvisor, um especialista amigável em tecnologia e programação.\n"
    "Converse de forma objetiva, em português, com o usuário {nome}.\n"
    "Pergunta do usuário: {pergunta}\n\n"
    "Responda de forma curta e útil. Quando adequado, recomende tecnologias, frameworks, "
    "boas práticas ou próximos passos de estudo."
)
prompt = PromptTemplate(
    input_variables=["nome", "pergunta"],
    template=template_text
)

qa_chain = prompt | llm | StrOutputParser()

def extrair_nome(texto: str) -> str:
    """Heurística simples: usa a frase inteira como nome, limpando espaços e pontuação leve."""
    if not texto:
        return ""
    candidato = texto.strip()
    candidato = re.sub(r'^["\'\s]+|["\'\s]+$', "", candidato)
    partes = [p.capitalize() for p in re.split(r"\s+", candidato) if p]
    return " ".join(partes)


def boas_vindas_node(state: dict) -> dict:
    state["resposta"] = "Olá! Eu sou o TechAdvisor. Como posso te chamar?"
    state["etapa"] = "aguardar_nome"
    return state


def aguardar_nome_node(state: dict) -> dict:
    mensagem = (state.get("mensagem_usuario") or "").strip()
    if not mensagem:
        state["resposta"] = "Não entendi. Qual é o seu nome?"
        state["etapa"] = "aguardar_nome"
        return state

    nome = extrair_nome(mensagem)
    if not nome:
        state["resposta"] = "Poderia repetir seu nome, por favor?"
        state["etapa"] = "aguardar_nome"
        return state

    state["nome"] = nome
    state.setdefault("historico", [])
    state["resposta"] = f"Prazer, {nome}! Como posso ajudar em tecnologia hoje?"
    state["etapa"] = "responder_perguntas"
    return state


def responder_perguntas_node(state: dict) -> dict:
    mensagem = (state.get("mensagem_usuario") or "").strip()
    nome = state.get("nome", "usuário")

    if mensagem.lower() == "tchau" or "tchau" in mensagem.lower():
        state["resposta"] = f"Até logo, {nome}! 👋"
        state["etapa"] = "fim"
        state["encerrar"] = True
        return state

    resposta = qa_chain.invoke({
        "nome": nome,
        "pergunta": mensagem or "Me diga algo legal sobre tecnologia."
    })

    historico = state.setdefault("historico", [])
    if mensagem:
        historico.append({"role": "user", "content": mensagem})
    historico.append({"role": "assistant", "content": resposta})

    state["resposta"] = resposta
    state["etapa"] = "responder_perguntas"
    state["encerrar"] = False
    return state


def roteador_node(state: dict) -> dict:
    return state


def proxima_parada(state: dict) -> str:
    etapa = state.get("etapa")
    if etapa == "aguardar_nome":
        return "aguardar_nome"
    if etapa == "responder_perguntas":
        return "responder_perguntas"
    if etapa == "fim":
        return "fim"
    return "boas_vindas"


graph = StateGraph(dict)

graph.add_node("roteador", roteador_node)
graph.add_node("boas_vindas", boas_vindas_node)
graph.add_node("aguardar_nome", aguardar_nome_node)
graph.add_node("responder_perguntas", responder_perguntas_node)

graph.add_conditional_edges(
    "roteador",
    proxima_parada,
    {
        "boas_vindas": "boas_vindas",
        "aguardar_nome": "aguardar_nome",
        "responder_perguntas": "responder_perguntas",
        "fim": END,
    },
)

graph.add_edge("boas_vindas", END)
graph.add_edge("aguardar_nome", END)
graph.add_edge("responder_perguntas", END)

graph.set_entry_point("roteador")

app = graph.compile()

if __name__ == "__main__":
    print("🤖 TechAdvisor - Agente conversacional sobre tecnologia\n")

    state: dict = {}

    result = app.invoke(state)
    state.update(result)
    print(state.get("resposta", "Olá!"))

    while True:
        try:
            mensagem = input("\nVocê: ")
        except (KeyboardInterrupt, EOFError):
            print("\nEncerrando o agente. Até logo!")
            break

        if mensagem.lower() in ["sair", "exit", "quit"]:
            print("Encerrando o agente. Até logo!")
            break

        state["mensagem_usuario"] = mensagem
        result = app.invoke(state)
        state.update(result)

        print(f"\n🔎 Agente: {state.get('resposta', '')}")

        if state.get("etapa") == "fim" or state.get("encerrar"):
            print("\nConversa encerrada.")
            break