
from services.gemini_service import consultar_gemini


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

    prompt = f"""
Você é um assistente especializado em classificação de chamados de suporte de TI.

Analise o chamado abaixo e classifique-o.

CHAMADO:
{chamado}

Apresente o resultado neste formato:

Categoria:
Prioridade:
Sistema:
Resumo:
Justificativa:

Regras:
- Categoria: Software, Hardware, Acesso/Permissão,
  Rede/Conectividade, Dados/Relatórios ou Outro.
- Prioridade: Crítica, Alta, Média ou Baixa.
- Sistema: informe o sistema mencionado no chamado.
  Se não houver identificação, escreva Não identificado.
- Não invente informações que não estejam no chamado.
- Considere o impacto descrito para definir a prioridade.
- Responda em português brasileiro.
"""

    print("\nAnalisando chamado com inteligência artificial...")

    try:
        resultado = consultar_gemini(prompt)

        print("\n========== RESULTADO DA CLASSIFICAÇÃO ==========\n")
        print(resultado)
        print("\n===============================================\n")

    except Exception as erro:
        print(f"\nNão foi possível classificar o chamado: {erro}")


if __name__ == "__main__":
    main()
