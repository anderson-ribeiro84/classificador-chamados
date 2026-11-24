
from services.gemini_service import consultar_gemini
from prompts import preparar_prompt


def main():
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
        print("\nNenhuma descrição foi informada.")
        return

    print("\nAnalisando chamado com inteligência artificial...")

    try:
        prompt = preparar_prompt(chamado)
        resultado = consultar_gemini(prompt)

        print("\n========== RESULTADO DA CLASSIFICAÇÃO ==========\n")
        print(resultado)
        print("\n===============================================\n")

    except (ValueError, RuntimeError) as erro:
        print(f"\nNão foi possível classificar o chamado: {erro}")

    except Exception:
        print(
            "\nOcorreu um erro inesperado durante a classificação. "
            "Tente novamente ou entre em contato com o suporte."
        )


if __name__ == "__main__":
    main()
