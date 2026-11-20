import os

from dotenv import load_dotenv
from google import genai


# Carrega as variáveis do arquivo .env
load_dotenv()
# Recupera a chave da API
API_KEY = os.getenv("GEMINI_API_KEY")

# Define o modelo utilizado
MODEL_NAME = "gemini-3.5-flash-lite"


def obter_cliente():
    """
    Cria o cliente de comunicação com o Gemini.
    """
    if not API_KEY:
        raise ValueError(
            "Chave GEMINI_API_KEY não encontrada. "
            "Verifique o arquivo .env."
        )

    return genai.Client(api_key=API_KEY)


def consultar_gemini(texto):
    """
    Envia um texto ao Gemini e retorna a resposta.
    """
    cliente = obter_cliente()

    resposta = cliente.models.generate_content(
        model=MODEL_NAME,
        contents=texto
    )

    if not resposta.text:
        raise ValueError("O Gemini retornou uma resposta vazia.")

    return resposta.text
