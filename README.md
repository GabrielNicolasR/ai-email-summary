# AI Email Summarizer with LangChain & OpenAI

[English](#english) | [Português](#português)

---

## English

Simple Python project using LangChain and OpenAI to automatically summarize emails with structured output (Topic, Priority, and Summary).

### Technologies Used

- Python
- LangChain
- OpenAI API
- Pydantic
- python-dotenv

### Features

- **Structured Output:** Each email is processed to extract the main topic, priority level (High, Medium, Low), and a concise summary.
- **Pydantic Models:** Uses Pydantic for robust data validation and structured JSON output.
- **LangChain Expression Language (LCEL):** Implements a clean chain for prompt management and model invocation.

### How to Run the Project

#### 1. Clone the repository

```bash
git clone https://github.com/GabrielNicolasR/ai-email-summary.git
```

#### 2. Install dependencies

```bash
pip install -r requirements.txt
```

#### 3. Create a `.env` file

Inside the project, create a file named `.env`

Example:

```env
OPENAI_API_KEY=your-key-here
OPENAI_MODEL=gpt-4o-mini
```

#### 4. Run the project

```bash
python app.py
```

---

## Português

Projeto simples em Python utilizando LangChain e OpenAI para resumir emails automaticamente com saída estruturada (Tópico, Prioridade e Resumo).

### Tecnologias utilizadas

- Python
- LangChain
- OpenAI API
- Pydantic
- python-dotenv

### Funcionalidades

- **Saída Estruturada:** Cada e-mail é processado para extrair o tópico principal, nível de prioridade (Alta, Média, Baixa) e um resumo conciso.
- **Modelos Pydantic:** Utiliza Pydantic para validação robusta de dados e saída JSON estruturada.
- **LangChain Expression Language (LCEL):** Implementa uma cadeia limpa para gerenciamento de prompts e invocação do modelo.

### Como executar o projeto

#### 1. Clone o repositório

```bash
git clone https://github.com/GabrielNicolasR/ai-email-summary.git
```

#### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 3. Crie um arquivo `.env`

Dentro do projeto, crie um arquivo chamado `.env`

Exemplo:

```env
OPENAI_API_KEY=sua-chave-aqui
OPENAI_MODEL=gpt-4o-mini
```

#### 4. Execute o projeto

```bash
python app.py
```
