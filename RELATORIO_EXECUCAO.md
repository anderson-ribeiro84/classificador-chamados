# Relatório de Execução — P0

## 1. Evolução por nível

### 1.1. Nível Básico

No nível Básico, foi desenvolvida a primeira versão funcional do classificador de chamados de suporte técnico utilizando Python e o modelo Google Gemini.

A aplicação recebe uma descrição textual de um chamado pelo terminal, prepara uma solicitação para o modelo de linguagem, realiza a chamada por meio de sua interface programática e apresenta o resultado da classificação.

O resultado esperado consiste na identificação de uma categoria e de uma prioridade para o chamado informado.

Também foram definidos os arquivos iniciais do projeto, as dependências necessárias e a configuração externa da credencial de acesso ao serviço, evitando sua exposição direta no código-fonte.

Ao final desta etapa, foi possível executar o fluxo principal e obter uma classificação utilizando o Gemini.

### 1.2. Nível Intermediário

No nível Intermediário, a aplicação foi reorganizada para separar as responsabilidades de captura da entrada, carregamento das configurações, preparação dos prompts, comunicação com o modelo de linguagem e apresentação dos resultados.

Foram implementadas validações para impedir o processamento de entradas vazias e tratamentos para situações como ausência de credenciais, falhas de autenticação, erros de comunicação, indisponibilidade do serviço e respostas inválidas ou vazias.

Também foram desenvolvidos testes automatizados para verificar o comportamento das funcionalidades e dos tratamentos de erro sem depender exclusivamente de chamadas reais ao Gemini.

A evolução foi registrada por meio de commits progressivos em uma branch específica, posteriormente integrada à branch principal por meio de Pull Request.

Ao final desta etapa, a aplicação apresentou maior organização, previsibilidade e capacidade de tratamento de situações inesperadas.

### 1.3. Nível Avançado

No nível Avançado, foram implementadas melhorias para tornar a aplicação mais configurável, segura e reproduzível.

As configurações do modelo Gemini passaram a permitir ajustes externos, por meio de variáveis de ambiente, incluindo identificação do modelo, temperatura e limite máximo de tokens, sem necessidade de modificar o código principal.

Foi implementado um sistema de logging para registrar informações relevantes da execução, evitando a exposição de credenciais e do conteúdo dos chamados nos registros.

Também foram ampliados os testes automatizados, utilizando simulações para validar a lógica da aplicação sem realizar chamadas reais ao modelo de linguagem. A suíte completa totalizou 22 testes aprovados.

Por fim, foi realizada uma validação em ambiente virtual independente, com instalação das dependências, configuração do acesso ao Gemini e execução bem-sucedida da aplicação.

As alterações foram integradas à branch principal por Pull Request e identificadas pela tag `p0-avancado`, acompanhada de uma Release no GitHub.

## 2. Decisões principais

### 2.1. Escolha do provedor de LLM

**Decisão tomada:** utilizar o Google Gemini como serviço de inteligência artificial da aplicação.

**Alternativa considerada:** utilizar o LLM institucional disponibilizado pelo curso ou outro provedor de modelos de linguagem.

**Justificativa:** as regras da missão permitem que o estudante escolha outro provedor. O Gemini ofereceu uma interface programática adequada ao escopo do projeto e permitiu realizar chamadas reais para classificação dos chamados.

### 2.2. Utilização de interface pelo terminal

**Decisão tomada:** desenvolver a aplicação principal com interação pelo terminal.

**Alternativa considerada:** construir uma interface gráfica ou aplicação web.

**Justificativa:** o objetivo do P0 é demonstrar o primeiro fluxo funcional com um LLM. A interface pelo terminal atende à necessidade de entrada e apresentação dos resultados, mantendo o escopo simples e concentrando os esforços na integração, organização e validação da solução.

### 2.3. Separação das responsabilidades do código

**Decisão tomada:** organizar a aplicação em módulos específicos para configuração, preparação dos prompts, comunicação com o Gemini e execução do programa.

**Alternativa considerada:** concentrar toda a lógica em um único arquivo Python.

**Justificativa:** a separação facilita a manutenção, a compreensão do código e a realização de testes independentes, além de permitir alterações futuras com menor impacto sobre as demais partes da aplicação.

### 2.4. Utilização de testes automatizados com simulações

**Decisão tomada:** utilizar `unittest` e recursos de simulação (*mock*) para testar a lógica da aplicação sem realizar chamadas reais ao LLM.

**Alternativa considerada:** depender exclusivamente de chamadas reais ao Gemini ou utilizar um modelo local para realizar os testes.

**Justificativa:** as simulações permitem verificar respostas, entradas inválidas e situações de erro sem depender da disponibilidade do serviço externo, de conexão com a internet ou do consumo de créditos. As chamadas reais foram utilizadas separadamente para validar a integração com o Gemini.

## 3. Testes e resultados

Foram desenvolvidos testes automatizados utilizando `unittest`, incluindo simulações das respostas e falhas do serviço externo. Dessa forma, foi possível validar a lógica da aplicação sem realizar chamadas reais ao modelo de linguagem.

A suíte completa foi executada no ambiente virtual de validação, totalizando 22 testes aprovados.

| Teste | Situação | Esperado | Resultado |
|---|---|---|---|
| Classificação | Chamado válido | Processar solicitação | Aprovado |
| Entrada vazia | Texto vazio | Rejeitar entrada | Aprovado |
| Credencial | Chave ausente | Informar erro de configuração | Aprovado |
| Temperatura | Valor inválido | Rejeitar configuração | Aprovado |
| Tokens | Limite inválido | Rejeitar configuração | Aprovado |
| Resposta vazia | Serviço sem conteúdo | Tratar resposta inválida | Aprovado |
| Falha de comunicação | Erro simulado | Tratar falha do serviço | Aprovado |
| Preparação do prompt | Texto de entrada | Gerar prompt esperado | Aprovado |
| Integração real | Chamado fictício | Obter classificação do Gemini | Sucesso |

Além dos testes automatizados, foi realizada uma execução real da aplicação em ambiente virtual independente, confirmando a instalação das dependências, a configuração do acesso ao Gemini e o funcionamento da integração.

**Resultado geral:** 22 testes automatizados aprovados e validação real da integração com o Gemini concluída com sucesso.

## 4. Limitações identificadas

### 4.1. Limitação na classificação dos chamados

**O que acontece:** a classificação depende da interpretação do modelo de linguagem. Descrições incompletas, ambíguas ou com poucas informações podem resultar em sugestões de categoria ou prioridade diferentes das esperadas.

**Como foi identificada:** durante a análise dos requisitos e do comportamento esperado do classificador, foi identificada a possibilidade de resultados inconsistentes quando as descrições dos chamados apresentam informações insuficientes ou ambíguas.

**Como foi tratada:** foram definidos prompts com instruções para orientar a identificação da categoria e da prioridade. Também foram implementados tratamentos para respostas vazias e falhas de comunicação com o serviço.

**Por que permanece:** modelos de linguagem possuem comportamento probabilístico e dependem do contexto fornecido. Portanto, a aplicação apresenta sugestões de classificação que podem exigir revisão humana, não substituindo integralmente a avaliação de um profissional de suporte.

## 5. Uso de inteligência artificial no desenvolvimento

**Ferramenta utilizada:** ChatGPT, como ferramenta de apoio ao desenvolvimento.

**Atividades apoiadas:** planejamento da estrutura do projeto, esclarecimento de conceitos de Python e integração com APIs, elaboração e revisão de trechos de código, identificação de possíveis erros, criação de testes automatizados e organização da documentação.

**Resultados aproveitados:** as sugestões contribuíram para a organização dos módulos, implementação das configurações, tratamento de erros, logging, testes e documentação do projeto.

**Revisão e verificação:** as sugestões foram analisadas e adaptadas conforme as necessidades da aplicação. Os códigos foram executados no ambiente local, os comportamentos foram verificados por meio de testes automatizados e a integração com o Google Gemini foi validada com uma chamada real.

A inteligência artificial foi utilizada como ferramenta de apoio, sem substituir a análise, as decisões técnicas e a validação realizadas durante o desenvolvimento.

## 6. Reflexão final

**Principal aprendizado:** compreender e implementar a integração de uma aplicação Python com um modelo de linguagem por meio de uma API, desde a configuração das credenciais até o tratamento das respostas e dos possíveis erros.

**Competência mais desenvolvida:** desenvolvimento em Python para aplicações de inteligência artificial, especialmente na integração com serviços externos, organização do código e implementação de testes automatizados.

**Aspecto a melhorar:** aprofundar os conhecimentos em engenharia de software e avaliação de modelos de linguagem, incluindo técnicas para medir a qualidade das classificações e reduzir resultados inconsistentes.

O desenvolvimento do projeto proporcionou uma experiência prática de construção de uma aplicação com inteligência artificial, envolvendo programação, versionamento, testes, segurança de configurações e documentação.