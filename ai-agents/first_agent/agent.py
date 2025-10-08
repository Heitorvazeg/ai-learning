from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


class FirstAgent:
    def __init__ (self, model_name="gpt-3.5-turbo", temperature=0):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
    
    def respond(self, prompt_user):
        template = PromptTemplate.from_template("Resuma o seguinte texto em 3 pontos principais: \n\n{texto}")
        self.chain = LLMChain(llm=self.llm, prompt=template)
        response = self.chain.invoke({"texto": prompt_user})
        return response


agent = FirstAgent()
