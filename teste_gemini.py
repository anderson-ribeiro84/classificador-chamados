import os
from dotenv import load_dotenv
from google import genai

# Carrega as variáveis do arquivo .env
load_dotenv()

# Recupera a chave sem deixá-la exposta no código
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Chave GEMINI_API_KEY não encontrada.")

# Inicializa o cliente
client = genai.Client(api_key=api_key)

# Faz uma solicitação simples ao modelo
resposta = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Responda em português: explique brevemente o que é um chamado de suporte de TI."
)

print("\nRESPOSTA DO GEMINI:\n")
print(resposta.text)

client.close()
