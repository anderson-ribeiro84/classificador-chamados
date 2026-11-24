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
- **httpx2:** biblioteca utilizada pelo ambiente de comunicação HTTP e no tratamento de exceções de conexão e timeout.
- **unittest:** framework nativo do Python utilizado nos testes automatizados.
- **Git e GitHub:** ferramentas utilizadas para controle de versão e armazenamento do código-fonte.

### 5.1. Modelo de linguagem

- **Provedor:** Google.
- **Modelo:** `gemini-3.5-flash-lite`.

A aplicação utiliza a API do Google Gemini para processar as descrições dos chamados.

O modelo pode ser configurado por variável de ambiente, permitindo sua alteração sem modificar o código-fonte.

A chave de acesso é armazenada na variável `GEMINI_API_KEY`, evitando sua exposição direta no código-fonte.

## 6. Estrutura do projeto

```text
P0/
├── services/
│   └── gemini_service.py
├── tests/
│   ├── test_config.py
│   ├── test_gemini_service.py
│   └── test_prompts.py
├── templates/
│   ├── index.html
│   └── resultado.html
├── cli.py
├── config.py
├── prompts.py
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── .dockerignore
├── Dockerfile
├── teste_gemini.py
├── teste_servico.py
└── README.md
```

### 6.1. Organização dos arquivos

- `cli.py`: recebe a descrição do chamado pelo terminal, solicita a classificação e apresenta o resultado.
- `config.py`: centraliza a leitura e validação das configurações e credenciais.
- `prompts.py`: prepara as instruções enviadas ao modelo de linguagem.
- `services/gemini_service.py`: centraliza a comunicação com a API do Gemini e o tratamento de falhas.
- `tests/test_config.py`: testa a leitura e validação das configurações.
- `tests/test_gemini_service.py`: testa o serviço Gemini e seus diferentes cenários de resposta e falha.
- `tests/test_prompts.py`: testa a preparação e validação dos prompts.
- `.env.example`: apresenta o modelo de configuração das variáveis de ambiente.
- `.env`: armazena as configurações privadas da aplicação e não deve ser publicado.
- `requirements.txt`: lista as dependências Python do projeto.
- `.gitignore`: impede que arquivos privados e temporários sejam enviados ao GitHub.
- `app.py` e `templates/`: componentes de uma versão inicial com interface web.
- `Dockerfile` e `.dockerignore`: arquivos utilizados na configuração inicial de execução em contêiner.
- `teste_gemini.py` e `teste_servico.py`: scripts auxiliares utilizados durante os primeiros testes de integração.

### 6.2. Organização da aplicação

A partir da etapa intermediária, o projeto passou a utilizar uma estrutura modular, separando responsabilidades:

1. **Entrada:** recebimento e validação da descrição do chamado.
2. **Configuração:** leitura das credenciais e do modelo utilizado.
3. **Preparação do prompt:** organização das instruções enviadas à LLM.
4. **Comunicação:** envio da solicitação ao Google Gemini.
5. **Tratamento da resposta:** validação do retorno e apresentação da classificação.

Essa organização facilita a manutenção, os testes e a evolução da aplicação.

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

### 7.5. Configurar as variáveis de ambiente

O projeto disponibiliza o arquivo `.env.example` como modelo de configuração.

Crie uma cópia desse arquivo com o nome `.env`:

No Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

O conteúdo esperado é:

```env
GEMINI_API_KEY=sua_chave_aqui
GEMINI_MODEL=gemini-3.5-flash-lite
```

Substitua `sua_chave_aqui` pela chave obtida no Google AI Studio.

A variável `GEMINI_MODEL` permite definir o modelo utilizado pela aplicação.

**Importante:** não publique o arquivo `.env` nem compartilhe sua chave de API. O arquivo está incluído no `.gitignore`.

### 7.6. Executar a aplicação

Com o ambiente virtual ativado e as variáveis configuradas, execute:

```bash
python cli.py
```

O programa solicitará a descrição do chamado.

Para finalizar a entrada no Windows, pressione `Ctrl + Z` e depois `Enter`.

## 8. Exemplo de utilização

### 8.1. Entrada

```text
O sistema ERP apresenta falha de conexão com o banco de dados.
Todos os usuários do setor estão sem acesso.
O problema começou hoje pela manhã.
A equipe não consegue realizar as operações.
```

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

*Observação: como a classificação é gerada por um modelo de linguagem, o texto e a classificação podem variar entre execuções.*

## 9. Testes automatizados

A partir da etapa intermediária, foram implementados testes automatizados utilizando o módulo `unittest`, nativo do Python.

Os testes verificam o comportamento das principais partes da aplicação sem depender de chamadas reais à API para simular os cenários de sucesso e falha.

### 9.1. Executar os testes

Com o ambiente virtual ativado, execute:

```powershell
python -m unittest discover -s tests -v
```

### 9.2. Cenários testados

| Arquivo | Cenário | Resultado |
|---|---|---|
| `test_config.py` | Recuperação de chave configurada | Aprovado |
| `test_config.py` | Rejeição de chave ausente | Aprovado |
| `test_config.py` | Recuperação do modelo padrão | Aprovado |
| `test_config.py` | Recuperação de modelo configurado | Aprovado |
| `test_gemini_service.py` | Resposta bem-sucedida | Aprovado |
| `test_gemini_service.py` | Rejeição de texto vazio | Aprovado |
| `test_gemini_service.py` | Rejeição de resposta vazia | Aprovado |
| `test_gemini_service.py` | Tratamento de chave inválida (HTTP 401) | Aprovado |
| `test_gemini_service.py` | Tratamento de serviço indisponível (HTTP 503) | Aprovado |
| `test_gemini_service.py` | Tratamento de timeout | Aprovado |
| `test_gemini_service.py` | Tratamento de falha de conexão | Aprovado |
| `test_prompts.py` | Preparação de prompt válido | Aprovado |
| `test_prompts.py` | Rejeição de chamado com espaços | Aprovado |
| `test_prompts.py` | Rejeição de chamado vazio | Aprovado |

**Resultado da execução: 14 testes aprovados.**

Os cenários de falha da API são simulados por meio de mocks, evitando chamadas desnecessárias ao serviço externo.

### 9.3. Teste de integração

Além dos testes automatizados, foi realizada uma execução manual da aplicação pelo terminal, utilizando a API real do Google Gemini.

O teste confirmou:

- Recebimento de descrições com múltiplas linhas.
- Comunicação com o modelo de linguagem.
- Retorno de classificação estruturada.
- Identificação de categoria, prioridade, sistema, resumo e justificativa.

## 10. Tratamento de erros

A aplicação possui mecanismos para identificar e tratar situações que podem impedir a classificação de um chamado.

Entre os cenários contemplados estão:

- Ausência da chave de API.
- Chave de API inválida ou sem autorização.
- Modelo configurado não encontrado.
- Limite de solicitações atingido.
- Serviço Gemini temporariamente indisponível.
- Falha de conexão com a internet.
- Tempo limite de comunicação excedido.
- Entrada vazia ou resposta inválida.

As falhas conhecidas são convertidas em mensagens compreensíveis para o usuário, evitando a exposição desnecessária de detalhes técnicos.

## 11. Limitações conhecidas

- A aplicação depende de conexão com a internet e disponibilidade da API do Google Gemini.
- O uso da API está sujeito aos limites e às condições estabelecidas pelo provedor.
- A classificação é uma recomendação gerada por Inteligência Artificial e deve ser validada por um profissional de suporte.
- A resposta pode variar conforme a descrição fornecida e a geração do modelo.
- A aplicação ainda não possui integração com ferramentas de gerenciamento de chamados ou sistemas corporativos.

## 12. Evolução do projeto

O projeto foi desenvolvido de forma incremental, contemplando os seguintes níveis:

- **Básico:** criação de uma aplicação Python executada pelo terminal, integrada ao Google Gemini para classificação de chamados.
- **Intermediário:** modularização do código, configuração por variáveis de ambiente, tratamento de falhas e implementação de testes automatizados.
- **Avançado:** evolução da aplicação com recursos adicionais de configuração, segurança, qualidade e validação.

O repositório mantém o histórico de desenvolvimento por meio do Git, permitindo identificar a evolução de cada etapa.

---

**Repositório GitHub:**
https://github.com/anderson-ribeiro84/classificador-chamados