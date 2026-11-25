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

- **Python 3.15.2:** linguagem utilizada no desenvolvimento da aplicação.
- **Google Gemini API:** serviço de Inteligência Artificial utilizado para analisar e classificar os chamados.
- **Google Gen AI SDK (`google-genai` 3.6.1):** biblioteca responsável pela comunicação entre Python e Gemini.
- **python-dotenv 1.2.4:** biblioteca utilizada para carregar variáveis de ambiente do arquivo `.env`.
- **httpx2 2.16.2:** biblioteca utilizada na comunicação HTTP e no tratamento de exceções de conexão e timeout.
- **unittest:** framework nativo do Python utilizado nos testes automatizados.
- **Git e GitHub:** ferramentas utilizadas para controle de versão e armazenamento do código-fonte.

O arquivo `requirements.txt` também mantém dependências utilizadas na estrutura inicial do projeto com interface web, como Flask e Gunicorn.

### 5.1. Modelo de linguagem

- **Provedor:** Google.
- **Modelo padrão:** `gemini-3.5-flash-lite`.

A aplicação utiliza a API do Google Gemini para processar as descrições dos chamados.

O modelo pode ser configurado pela variável de ambiente `GEMINI_MODEL`, permitindo sua alteração sem modificar o código-fonte.

A chave de acesso é armazenada na variável `GEMINI_API_KEY`, evitando sua exposição direta no código-fonte.

O comportamento da geração também pode ser ajustado pelas variáveis `GEMINI_TEMPERATURE` e `GEMINI_MAX_OUTPUT_TOKENS`.

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

Arquivos temporários, ambientes virtuais, caches e configurações privadas não são apresentados na árvore principal, pois não fazem parte dos artefatos que devem ser publicados no repositório.

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
2. **Configuração:** leitura das credenciais e dos parâmetros do modelo utilizado.
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

Execute o comando:

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

Crie uma cópia desse arquivo com o nome `.env`.

No Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

O conteúdo esperado é:

```env
GEMINI_API_KEY=sua_chave_aqui
GEMINI_MODEL=gemini-3.5-flash-lite
GEMINI_TEMPERATURE=0.2
GEMINI_MAX_OUTPUT_TOKENS=1024
```

Substitua `sua_chave_aqui` pela chave obtida no Google AI Studio.

A variável `GEMINI_MODEL` permite definir o modelo utilizado pela aplicação.

As demais variáveis permitem ajustar o comportamento da geração:

- `GEMINI_TEMPERATURE`: controla a variação das respostas geradas. O valor padrão é `0.2`.
- `GEMINI_MAX_OUTPUT_TOKENS`: define o limite máximo de tokens da resposta. O valor padrão é `1024`.

Essas configurações podem ser alteradas diretamente no arquivo `.env`, sem necessidade de modificar o código-fonte.

**Importante:** não publique o arquivo `.env` nem compartilhe sua chave de API. O arquivo está incluído no `.gitignore`.

### 7.6. Executar a aplicação

Com o ambiente virtual ativado e as variáveis configuradas, execute:

```bash
python cli.py
```

O programa solicitará a descrição do chamado de suporte.

A descrição pode ser informada em uma ou várias linhas. Para finalizar a entrada no Windows, pressione `Ctrl + Z` e depois `Enter`.

Após o envio, a aplicação encaminhará o chamado ao Google Gemini e apresentará a classificação gerada.

## 8. Exemplo de utilização

### 8.1. Entrada

Exemplo de descrição fornecida pelo usuário:

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

**Observação:** como a classificação é gerada por um modelo de linguagem, o texto e a classificação podem variar entre execuções. O resultado apresentado é ilustrativo.

## 9. Testes automatizados

A partir da etapa intermediária, foram implementados testes automatizados utilizando o módulo `unittest`, nativo do Python.

Os testes verificam o comportamento das principais partes da aplicação sem depender de chamadas reais à API para simular os cenários de sucesso e falha.

### 9.1. Executar os testes

Com o ambiente virtual ativado, execute:

```powershell
python -m unittest discover -s tests -v
```

### 9.2. Cenários testados

| Arquivo | Cenários contemplados |
|---|---|
| `test_config.py` | Recuperação de chave, modelo e valores padrão; validação de configurações ausentes, inválidas e fora dos limites permitidos. |
| `test_gemini_service.py` | Resposta bem-sucedida, texto vazio, resposta vazia, chave inválida (HTTP 401), serviço indisponível (HTTP 503), timeout e falha de conexão. |
| `test_prompts.py` | Preparação de prompt válido e rejeição de descrições vazias ou contendo apenas espaços. |

**Resultado da última execução registrada: 22 testes aprovados.**

Os cenários de falha da API são simulados por meio de mocks, evitando chamadas desnecessárias ao serviço externo.

### 9.3. Teste de integração

Além dos testes automatizados, foram realizadas execuções manuais da aplicação pelo terminal, utilizando a API real do Google Gemini.

Os testes confirmaram:

- Recebimento de descrições com múltiplas linhas.
- Comunicação com o modelo de linguagem.
- Retorno de classificação estruturada.
- Identificação de diferentes categorias e níveis de prioridade.
- Tratamento adequado das respostas e apresentação dos resultados.

Essas execuções demonstraram o funcionamento da integração real, complementando os testes automatizados realizados localmente.

### 9.4. Validação em ambiente limpo

Foi realizada uma validação em um novo ambiente virtual Python, utilizando Python 3.15.2, independente do ambiente utilizado durante o desenvolvimento. A configuração da API foi realizada localmente, por meio do arquivo `.env`, sem exposição da chave de acesso.

O procedimento contemplou:

- Criação de um novo ambiente virtual.
- Instalação das dependências exclusivamente pelo arquivo `requirements.txt`.
- Execução dos 22 testes automatizados, todos aprovados.
- Execução da aplicação pelo terminal.
- Comunicação com a API real do Google Gemini.
- Classificação bem-sucedida de um chamado fictício.

A validação demonstrou que a aplicação pode ser preparada e executada em um ambiente novo, seguindo as instruções de instalação e configuração documentadas neste README.

## 10. Tratamento de erros

A aplicação possui mecanismos para identificar e tratar situações que podem impedir a classificação de um chamado.

Entre os cenários contemplados estão:

- Ausência da chave de API.
- Chave de API inválida ou sem autorização.
- Modelo configurado não encontrado.
- Temperatura inválida ou fora do intervalo permitido.
- Limite máximo de tokens inválido.
- Limite de solicitações atingido.
- Serviço Gemini temporariamente indisponível.
- Falha de conexão com a internet.
- Tempo limite de comunicação excedido.
- Entrada vazia ou resposta inválida.

As falhas conhecidas são convertidas em mensagens compreensíveis para o usuário, evitando a exposição desnecessária de detalhes técnicos.

A aplicação também utiliza registros de execução (*logs*) para acompanhar o processamento, identificar falhas e confirmar a conclusão das classificações.

Esses registros não armazenam o conteúdo dos chamados nem credenciais de acesso.

## 11. Limitações conhecidas

- A aplicação depende de conexão com a internet e disponibilidade da API do Google Gemini.
- O uso da API está sujeito aos limites e às condições estabelecidas pelo provedor.
- A classificação é uma recomendação gerada por Inteligência Artificial e deve ser validada por um profissional de suporte.
- A resposta pode variar conforme a descrição fornecida e a geração do modelo.
- A aplicação ainda não possui integração com ferramentas de gerenciamento de chamados ou sistemas corporativos.

## 12. Evolução do projeto

O desenvolvimento foi organizado de forma incremental, contemplando três níveis de evolução.

- **Básico:** criação de uma aplicação Python executada pelo terminal, integrada ao Google Gemini para receber descrições e gerar classificações de chamados de suporte.
- **Intermediário:** modularização do código, separação de responsabilidades, configuração de credenciais por variáveis de ambiente, tratamento de falhas de comunicação e implementação de testes automatizados.
- **Avançado:** ampliação das configurações do modelo por variáveis de ambiente, incluindo temperatura e limite máximo de tokens; implementação de registros de execução (*logs*); aprimoramento do tratamento de erros; ampliação dos testes automatizados e validação em ambiente limpo.

O projeto mantém seu histórico de desenvolvimento por meio do Git e do GitHub, com identificação das etapas por tags e integração de alterações por meio de branch e Pull Request.

As etapas já identificadas no repositório são:

- `p0-basico`
- `p0-intermediario`

A tag `p0-avancado` será criada após a conclusão e validação da respectiva etapa.

O objetivo dessa organização é preservar a evolução do código e permitir a identificação das entregas correspondentes a cada nível do projeto.

---

**Repositório GitHub:**

https://github.com/anderson-ribeiro84/classificador-chamados
