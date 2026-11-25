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


def obter_temperatura():
    """
    Recupera e valida a temperatura de geração do Gemini.
    """
    temperatura = os.getenv(
        "GEMINI_TEMPERATURE",
        "0.2"
    )

    try:
        temperatura = float(temperatura)
    except ValueError:
        raise ValueError(
            "A temperatura do Gemini deve ser um número válido."
        )

    if not 0 <= temperatura <= 2:
        raise ValueError(
            "A temperatura deve estar entre 0 e 2."
        )

    return temperatura


def obter_limite_tokens():
    """
    Recupera e valida o limite máximo de tokens da resposta.
    """
    limite = os.getenv(
        "GEMINI_MAX_OUTPUT_TOKENS",
        "1024"
    )

    try:
        limite = int(limite)
    except ValueError:
        raise ValueError(
            "O limite de tokens deve ser um número inteiro."
        )

    if limite <= 0:
        raise ValueError(
            "O limite de tokens deve ser maior que zero."
        )

    return limite
