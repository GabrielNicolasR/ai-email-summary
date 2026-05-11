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
    for email in lista_de_emails :
        prompt = f"Resuma o seguinte email:{email}"
        
        try:
           resposta = chat.send_message(prompt)
           
           print(resposta.text)
           print("-" * 100)
        except Exception as erro:
           print(f"Erro ao resumir email: {erro}")

resumir_emails(emails)

