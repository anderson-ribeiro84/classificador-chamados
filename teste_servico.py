from services.gemini_service import consultar_gemini


pergunta = (
    "Explique brevemente o que é um chamado de suporte de TI."
)

try:
    resposta = consultar_gemini(pergunta)

    print("\nRESPOSTA DO GEMINI:\n")
    print(resposta)

except Exception as erro:
    print(f"\nErro ao consultar o Gemini: {erro}")
