import logging

from services.gemini_service import consultar_gemini
from prompts import preparar_prompt


# Configuração dos registros de execução
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Reduz mensagens internas das bibliotecas utilizadas pelo Gemini
logging.getLogger("google").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpx2").setLevel(logging.WARNING)
logging.getLogger("google_genai").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def main():
    logger.info("Iniciando o classificador de chamados.")

    print("\n======================================")
    print("   CLASSIFICADOR DE CHAMADOS DE TI")
    print("======================================")

    print("\nDescreva o problema de suporte:")
    print("(Ao terminar, pressione Ctrl + Z e depois Enter)\n")

    linhas = []

    while True:
        try:
            linha = input()
            linhas.append(linha)
        except EOFError:
            break

    chamado = "\n".join(linhas).strip()

    if not chamado:
        logger.warning("Nenhum chamado foi informado.")
        print("\nNenhuma descrição foi informada.")
        return

    logger.info("Chamado recebido para classificação.")

    print("\nAnalisando chamado com inteligência artificial...")

    try:
        prompt = preparar_prompt(chamado)
        resultado = consultar_gemini(prompt)

        logger.info("Classificação concluída com sucesso.")

        print("\n========== RESULTADO DA CLASSIFICAÇÃO ==========\n")
        print(resultado)
        print("\n===============================================\n")

    except (ValueError, RuntimeError) as erro:
        logger.error("Falha na classificação: %s", erro)

        print(f"\nNão foi possível classificar o chamado: {erro}")

    except Exception:
        logger.error(
            "Ocorreu um erro inesperado durante a classificação."
        )

        print(
            "\nOcorreu um erro inesperado durante a classificação. "
            "Tente novamente ou entre em contato com o suporte."
        )


if __name__ == "__main__":
    main()
