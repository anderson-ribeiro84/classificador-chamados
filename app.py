from flask import Flask, render_template, request
import requests
import urllib3

app = Flask(__name__)

# Endereço interno do servidor Ollama
LLM_URL = "https://llm-internal.softex:9001/api/chat"

# Modelo disponibilizado pela Devel Lab
LLM_MODEL = "qwen3.5:9b-q4_K_M"

# Desabilita apenas os avisos da chamada com certificado interno
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@app.route("/")
def inicio():
    return render_template("index.html")


def classificar_com_ia(chamado):

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

    dados = {
        "model": LLM_MODEL,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    resposta = requests.post(
        LLM_URL,
        json=dados,
        verify=False,
        timeout=180
    )

    resposta.raise_for_status()

    resultado = resposta.json()

    return resultado["message"]["content"]


@app.route("/classificar", methods=["POST"])
def classificar():

    chamado = request.form.get("chamado", "").strip()

    if not chamado:
        return "Informe a descrição do chamado.", 400

    try:
        resultado = classificar_com_ia(chamado)

        return render_template(
            "resultado.html",
            chamado=chamado,
            resultado=resultado
        )

    except Exception as erro:
        app.logger.exception("Erro na comunicação com o LLM")

        return (
            "Não foi possível classificar o chamado. "
            "Consulte os logs da aplicação.",
            502
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)