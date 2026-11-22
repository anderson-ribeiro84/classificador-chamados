# P0 — Classificador de Chamados de Suporte com Inteligência Artificial

## 1. Apresentação

Este projeto tem como objetivo desenvolver uma aplicação em Python integrada a um modelo de Inteligência Artificial (LLM), capaz de analisar descrições textuais de chamados de suporte de Tecnologia da Informação (TI) e gerar uma classificação estruturada.

A aplicação utiliza o Google Gemini para interpretar as informações fornecidas pelo usuário e apresentar uma sugestão de classificação, contemplando:

- **Categoria:** tipo de ocorrência identificada.
- **Prioridade:** nível de criticidade do chamado.
- **Sistema:** sistema ou aplicação mencionada.
- **Resumo:** síntese do problema relatado.
- **Justificativa:** explicação da classificação sugerida.

## 2. Objetivo

O projeto busca demonstrar como modelos de linguagem podem auxiliar no processo de triagem de chamados de suporte, transformando descrições livres em informações organizadas e facilitando a análise inicial das ocorrências.

A classificação gerada pela Inteligência Artificial tem caráter consultivo e deve ser validada pelo profissional responsável pelo atendimento.

## 3. Problema identificado

No atendimento de suporte de TI, os chamados geralmente são registrados por meio de descrições em linguagem natural, apresentando diferentes níveis de detalhamento, terminologias e formas de relatar uma ocorrência.

Essa variedade pode dificultar a identificação rápida da categoria, da prioridade e do sistema afetado, tornando a triagem dependente da interpretação individual de cada profissional.

Além disso, descrições incompletas ou pouco claras podem aumentar o tempo necessário para compreender o problema e encaminhá-lo corretamente.

## 4. Justificativa da solução

A utilização de um modelo de linguagem (LLM) permite analisar o contexto de uma descrição textual, identificar informações relevantes e gerar uma classificação estruturada.

Diferentemente de uma solução baseada exclusivamente em palavras-chave e regras fixas, a LLM pode interpretar diferentes formas de descrever uma mesma ocorrência, considerando o contexto apresentado.

Com isso, o classificador busca auxiliar o profissional de suporte na organização inicial dos chamados, contribuindo para uma triagem mais padronizada e eficiente.

A ferramenta não substitui a análise técnica do profissional, mas oferece uma recomendação inicial que pode ser revisada e ajustada conforme necessário.

## 5. Tecnologias utilizadas

- **Python:** linguagem utilizada no desenvolvimento da aplicação.
- **Google Gemini API:** serviço de Inteligência Artificial utilizado para analisar e classificar os chamados.
- **Google Gen AI SDK (`google-genai`):** biblioteca responsável pela comunicação entre Python e Gemini.
- **python-dotenv:** biblioteca utilizada para carregar variáveis de ambiente do arquivo `.env`.
- **Git e GitHub:** ferramentas utilizadas para controle de versão e armazenamento do código-fonte.

### 5.1. Modelo de linguagem

- **Provedor:** Google.
- **Modelo:** `gemini-3.5-flash-lite`.

A aplicação utiliza a API do Google Gemini para processar as descrições dos chamados.

A chave de acesso é armazenada em uma variável de ambiente (`GEMINI_API_KEY`), evitando sua exposição direta no código-fonte.

## 6. Estrutura do projeto

```text
P0/
├── services/
│   └── gemini_service.py
├── templates/
│   ├── index.html
│   └── resultado.html
├── cli.py
├── app.py
├── requirements.txt
├── teste_gemini.py
├── teste_servico.py
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

### 6.1. Organização dos arquivos

- `cli.py`: recebe a descrição do chamado pelo terminal e apresenta a classificação.
- `services/gemini_service.py`: centraliza a comunicação com a API do Gemini.
- `requirements.txt`: lista as dependências Python do projeto.
- `.gitignore`: impede que arquivos privados e temporários sejam enviados ao GitHub.
- `teste_gemini.py`: script utilizado nos primeiros testes de comunicação com o Gemini.
- `teste_servico.py`: teste da integração por meio do serviço Python.
- `app.py` e `templates/`: componentes de uma versão inicial com interface web.
- `Dockerfile` e `.dockerignore`: arquivos utilizados na configuração inicial de execução em contêiner.

O fluxo principal do nível básico utiliza a interface de terminal implementada em `cli.py`.

## 7. Instalação e configuração

### 7.1. Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3.15.2 (versão utilizada durante o desenvolvimento).
- Git.
- Acesso à internet.
- Uma chave de API do Google Gemini.

### 7.2. Clonar o repositório

```bash
git clone https://github.com/anderson-ribeiro84/classificador-chamados.git
```

Acesse a pasta do projeto:

```bash
cd classificador-chamados
```

### 7.3. Criar o ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 7.4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 7.5. Configurar a chave da API

Crie um arquivo chamado `.env` na raiz do projeto e adicione:

```env
GEMINI_API_KEY=sua_chave_aqui
```

Substitua `sua_chave_aqui` pela chave obtida no Google AI Studio.

**Importante:** não publique o arquivo `.env` nem compartilhe sua chave de API. O arquivo já está incluído no `.gitignore`.

### 7.6. Executar a aplicação

Com o ambiente virtual ativado e a chave configurada, execute:

```bash
python cli.py
```

## 8. Exemplo de utilização

Após executar `python cli.py`, o programa solicita que o usuário descreva o problema de suporte.

### 8.1. Entrada

```text
O sistema ERP apresenta falha de conexão com o banco de dados.
Todos os usuários do setor estão sem acesso.
O problema começou hoje pela manhã.
A equipe não consegue realizar as operações.
```

Para finalizar a descrição no Windows, pressione `Ctrl + Z` e depois `Enter`.

### 8.2. Resultado esperado

A aplicação envia a descrição para o Google Gemini, que analisa o contexto e retorna uma classificação estruturada, contendo:

```text
Categoria: Software
Prioridade: Crítica
Sistema: ERP

Resumo:
Falha de conexão com o banco de dados no sistema ERP,
impedindo o acesso e as operações de todos os usuários do setor.

Justificativa:
A prioridade é crítica porque todos os usuários do setor
estão sem acesso e as operações estão comprometidas.
```

*Observação: como a classificação é gerada por um modelo de linguagem, o texto da resposta pode variar entre execuções.*

## 9. Testes realizados

Durante o desenvolvimento do projeto, foram realizados os seguintes testes:

| Teste | Resultado |
|---|---|
| Comunicação com a API do Google Gemini | Aprovado |
| Carregamento da chave por variável de ambiente | Aprovado |
| Classificação de chamado com descrição em uma linha | Aprovado |
| Classificação de chamado com descrição em múltiplas linhas | Aprovado |
| Tratamento de entrada vazia | Aprovado |
| Retorno estruturado com categoria, prioridade, sistema, resumo e justificativa | Aprovado |

Os testes foram realizados localmente, utilizando o ambiente virtual Python e a API do Google Gemini.

## 10. Limitações conhecidas

- A aplicação depende de conexão com a internet e disponibilidade da API do Google Gemini.
- O uso da API está sujeito aos limites e às condições estabelecidas pelo provedor.
- A classificação é uma recomendação gerada por Inteligência Artificial e deve ser validada por um profissional de suporte.
- A resposta pode variar conforme a descrição fornecida e a geração do modelo.
