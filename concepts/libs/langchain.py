# Lib para criar agentes via código

# Usando LLM Diretamente:
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
resposta = llm.invoke("Explique o que é um transformer em IA")
print(resposta)

# Prompt Template:
from langchain.prompts import PromptTemplate

texto1="LangChain é um framework que conecta modelos de linguagem a dados."
template = PromptTemplate.from_template("Resuma o seguinte texto em 3 pontos principais: \n\n{texto}")
prompt = template.format(texto=texto1)

# Chains:

from langchain.chains import LLMChain
chain = LLMChain(llm=llm, prompt=template)
resp = chain.invoke({"texto": texto1})

# Adicionando Memória:

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
llm3 = ChatOpenAI(model_name="gpt-4", temperature=0)

conversation = ConversationChain(llm=llm3, memory=memory)

response1 = conversation.invoke("Oi, quem é você?")
response2 = conversation.invoke("O que você pode fazer?")

print(response1['response']) # Retorna um objeto

# RAG (Retrieval-Augmented Generation):
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import retrieval_qa

documento = """
O LangChain é uma biblioteca que facilita a criação de aplicações usando LLMs.
Ele oferece componentes para conectar modelos, bancos de dados e APIs externas.
""" # Exemplo de documento que o modelo vai usar

# Cada pedaço terá até 100 caracteres (chunk_size)
# Pedaços consecultivos compartilham 20 caracteres sem perder contexto (chunk_overlap)
# LLMs tem limites de tokens
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = splitter.create_documents([documento])

# Transforma cada pedaço em vetor numérico
embeddings = OpenAIEmbeddings()
# cria um banco vetorial para busca rápida
# Texto pesquisado por significado, e não por palavra exata
db = FAISS.from_documents(docs, embeddings)
# Retriever busca apenas o que é importante
retriever = db.as_retriever()

# Aplica a LLM ao retriever
qa = retrieval_qa.RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

res = qa.invoke("O que é langchain?")

# Tools:
from langchain.agents import initialize_agent, load_tools

llm4 = ChatOpenAI(model_name="gpt-4")
tools = load_tools(["llm-math"]) # Calculadora
# Zero-shot-react-description permite o agente decidir usar a tool
# Initialize_agent combina o LLMS às tools.
agent = initialize_agent(tools, llm4, agent="zero-shot-react-description", verbose=True)

output = agent.invoke("Qual é a raiz quadrada de 16 multiplicada po 5?")

# Criar a própria tool:
from langchain.agents import Tool

def minha_tool(x):
    return f"Você passou o valor {x}"

tool_custom = Tool(
    name="MinhaTool",
    func=minha_tool,
    description="Mostra o valor passado"
)

# Integração com arquivos:
from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("documento.pdf")
doc = loader.Load() # Permite fazer o RAG após carregar o documento
