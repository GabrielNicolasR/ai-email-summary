import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate
from pydantic import Field, BaseModel
from emails import emails

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class ResumoEmail(BaseModel):
    resumo: str = Field(description="Um resumo conciso do e-mail em poucas linhas")
    topico: str = Field(description="O tópico ou assunto principal abordado no e-mail")
    prioridade: str = Field(description="A prioridade do e-mail: Alta, Média ou Baixa")
    

parser = JsonOutputParser(pydantic_object=ResumoEmail)

prompt_resumo = PromptTemplate(
    template="""
    Você é um assistente de produtividade.
    Sua tarefa é ler o e-mail abaixo e extrair as informações principais.

    E-mail:
    {email}

    {formato_de_saida}
    """,
    input_variables=["email"],
    partial_variables={"formato_de_saida": parser.get_format_instructions()}
)
    

modelo = ChatOpenAI(
    model=os.getenv("OPENAI_MODEL"),
    temperature=0.5,
    api_key=api_key
)

cadeia = prompt_resumo | modelo | parser

def processar_e_resumir_emais(lista_de_emails):
    lista_de_resumos = []
    
    for i, email in enumerate(lista_de_emails):
        print(f"Processando e-mail {i}...")
        try:
           resposta = cadeia.invoke({"email": email})
           
           resumo_texto = (
            f"E-mail {i}: \n"
            f"Tópico: {resposta['topico']}\n"
            f"Prioridade: {resposta['prioridade']}\n"
            f"Resumo: {resposta['resumo']}\n"
           )

           print(resumo_texto)
           lista_de_resumos.append(resumo_texto)    
        except Exception as erro:
           print(f"Erro ao processar email {i}: {erro}")

    return lista_de_resumos

if __name__ == "__main__":
    resumos_finais = processar_e_resumir_emais(emails)

    with open("lista-de-resumos.txt", "w", encoding="utf-8") as arquivo:
        for item in resumos_finais:
            arquivo.write(item + "\n")