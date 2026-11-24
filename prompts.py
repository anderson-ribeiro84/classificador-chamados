def preparar_prompt(chamado):
    """
    Prepara as instruções enviadas ao modelo de linguagem.
    """

    if not chamado or not chamado.strip():
        raise ValueError("A descrição do chamado não pode estar vazia.")

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

    return prompt.strip()
