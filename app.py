from google import genai
from dotenv import load_dotenv
from emails import emails
import os

load_dotenv()

client = genai.Client(
    api_key=os.environ.get("GOOGLE_API_KEY")
)
chat = client.chats.create(
    model="models/gemini-2.5-flash"
) 

def resumir_emails(lista_de_emails):
    
    lista_de_resumos = []
    
    for i, email in enumerate(lista_de_emails, start=1) :
        prompt = f"""
        Resuma o seguinte e-mail em poucas linhas:

        {email}
        """
        
        try:
           resposta = chat.send_message(prompt)
           
           print(f"E-mail {i}: {resposta.text}")
           print("-" * 100)
           lista_de_resumos.append(f"E-mail {i}: {resposta.text}")
           
        except Exception as erro:
           print(f"Erro ao resumir email: {erro}")
    return lista_de_resumos

lista_resumos = resumir_emails(emails)


with open("lista-de-resumos.txt", "w", encoding="utf-8") as arquivo:
    for resumo in lista_resumos :
        arquivo.write(resumo + "\n")