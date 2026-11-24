import os

from dotenv import load_dotenv


# Carrega as variáveis definidas no arquivo .env
load_dotenv()


def obter_api_key():
    """
    Recupera e valida a chave de acesso do Google Gemini.
    """
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "Chave GEMINI_API_KEY não encontrada. "
            "Verifique o arquivo .env."
        )

    return api_key


def obter_modelo():
    """
    Recupera o modelo Gemini configurado.
    """
    modelo = os.getenv(
        "GEMINI_MODEL",
        "gemini-3.5-flash-lite"
    )

    if not modelo.strip():
        raise ValueError(
            "O modelo Gemini não foi configurado corretamente."
        )

    return modelo
