import httpx2

from google import genai
from google.genai import errors

from config import (
    obter_api_key,
    obter_modelo,
    obter_temperatura,
    obter_limite_tokens
)


def obter_cliente():
    """
    Cria o cliente de comunicação com o Gemini.
    """
    api_key = obter_api_key()

    return genai.Client(api_key=api_key)


def consultar_gemini(texto):
    """
    Envia um texto ao Gemini e trata possíveis falhas.
    """
    if not texto or not texto.strip():
        raise ValueError(
            "O texto para análise não pode estar vazio."
        )

    cliente = obter_cliente()
    modelo = obter_modelo()
    temperatura = obter_temperatura()
    limite_tokens = obter_limite_tokens()

    try:
        resposta = cliente.models.generate_content(
            model=modelo,
            contents=texto,
            config={
                "temperature": temperatura,
                "max_output_tokens": limite_tokens,
                "http_options": {
                    "timeout": 30000
                }
            }
        )

        if not resposta.text or not resposta.text.strip():
            raise ValueError(
                "O Gemini retornou uma resposta vazia."
            )

        return resposta.text

    except errors.APIError as erro:

        if erro.code == 400:
            raise RuntimeError(
                "A solicitação enviada ao Gemini é inválida."
            ) from erro

        elif erro.code in (401, 403):
            raise RuntimeError(
                "Falha de autenticação. Verifique sua chave da API."
            ) from erro

        elif erro.code == 404:
            raise RuntimeError(
                "O modelo Gemini configurado não foi encontrado."
            ) from erro

        elif erro.code == 429:
            raise RuntimeError(
                "Limite de solicitações atingido. Tente novamente mais tarde."
            ) from erro

        elif erro.code in (500, 502, 503, 504):
            raise RuntimeError(
                "O serviço Gemini está temporariamente indisponível."
            ) from erro

        else:
            raise RuntimeError(
                "Ocorreu um erro na comunicação com o Gemini."
            ) from erro

    except httpx2.TimeoutException as erro:
        raise RuntimeError(
            "O tempo limite de comunicação com o Gemini foi excedido."
        ) from erro

    except httpx2.ConnectError as erro:
        raise RuntimeError(
            "Não foi possível estabelecer conexão com o Gemini. "
            "Verifique sua conexão com a internet."
        ) from erro
