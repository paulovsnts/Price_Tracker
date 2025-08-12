````markdown
# Price Tracker

![Licença](https://img.shields.io/badge/license-MIT-blue.svg)
![Status do Projeto](https://img.shields.io/badge/status-em%20desenvolvimento-green.svg)
![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)

Um rastreador de preços versátil para monitorar produtos online e salvar o histórico em um banco de dados PostgreSQL.

[Read this README in English](#english-version)

---

## 🇧🇷 Versão em Português

### 📖 Sobre o Projeto

O Price Tracker nasceu da necessidade de monitorar os preços de componentes de hardware para montar um computador. O projeto evoluiu para uma ferramenta flexível de web scraping, projetada para extrair dados de preços de diferentes lojas online, processá-los e armazená-los de forma estruturada.

É uma solução completa para quem deseja acompanhar a flutuação de preços de qualquer produto ao longo do tempo.

### 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal do projeto.
* **PostgreSQL:** Banco de dados relacional para armazenamento dos dados de preços.
* **SQLAlchemy:** ORM para facilitar a comunicação entre o Python e o banco de dados.
* **Requests:** Para realizar as requisições HTTP às páginas dos produtos.
* **BeautifulSoup4:** Para fazer o parse do HTML e extrair as informações necessárias.
* **Pandas:** Para manipulação e análise de dados (principalmente nos notebooks).
* **python-dotenv:** Para gerenciar variáveis de ambiente de forma segura.

### 🚀 Começando

Siga estas instruções para ter uma cópia do projeto rodando na sua máquina local.

#### Pré-requisitos

* Python 3.9 ou superior
* Pip (gerenciador de pacotes do Python)
* Um servidor PostgreSQL instalado e rodando

#### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/price-tracker.git](https://github.com/seu-usuario/price-tracker.git)
    cd price-tracker
    ```

2.  **Crie e configure seu arquivo de ambiente:**
    Copie o arquivo `.env.example` para um novo arquivo chamado `.env` e preencha com suas credenciais do PostgreSQL.
    ```bash
    cp .env.example .env
    ```
    Seu arquivo `.env` deverá ficar assim:
    ```env
    POSTGRES_USER=seu_usuario
    POSTGRES_PASSWORD=sua_senha
    POSTGRES_DB=price_tracker
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicialize o banco de dados:**
    Este comando criará a tabela `prices` no seu banco de dados.
    ```bash
    python scripts/init_db.py
    ```

### ▶️ Uso

Para executar o pipeline de coleta de preços, rode o script `updater.py`. Ele irá:
1.  Visitar as URLs definidas em `src/scraper.py`.
2.  Extrair os dados.
3.  Processar e limpar as informações.
4.  Salvar os novos registros de preço no banco de dados.

```bash
python src/updater.py
````

### 🗂️ Estrutura do Projeto

```
price-tracker/
│
├── data/         # Dados brutos e processados (se necessário)
├── src/          # Código fonte principal
│   ├── config.py
│   ├── db.py
│   ├── scraper.py
│   ├── processor.py
│   └── updater.py
├── scripts/      # Scripts utilitários (ex: init_db.py)
├── .env          # Suas variáveis de ambiente (NÃO versionar)
├── .env.example  # Arquivo de exemplo para as variáveis
├── requirements.txt
└── README.md
```

### 🗺️ Roadmap

  * [ ] Adicionar suporte a mais lojas.
  * [ ] Criar um sistema de notificações (e-mail, Telegram) para alertas de queda de preço.
  * [ ] Desenvolver uma interface web simples (com Flask ou FastAPI) para visualização dos dados.
  * [ ] Empacotar a aplicação com Docker para facilitar o deploy.
  * [ ] Adicionar mais análises e visualizações nos notebooks.

### 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

### 👤 Contato

Paulo V Santos - [@dev_paulovsnts](https://x.com/dev_paulovsnts) 

Link do Projeto: [https://github.com/paulovsnts/Price_Tracker](https://www.google.com/search?q=https://github.com/paulovsnts/Price_Tracker)

\<br\>
\<hr\>
\<br\>

\<a id="english-version"\>\</a\>

## 🇬🇧 English Version

### 📖 About The Project

Price Tracker was born from the need to monitor the prices of hardware components to build a PC. The project evolved into a flexible web scraping tool designed to extract price data from different online stores, process it, and store it in a structured way.

It is a complete solution for anyone who wants to track price fluctuations of any product over time.

### 🛠️ Built With

  * **Python:** The project's core language.
  * **PostgreSQL:** Relational database for storing price data.
  * **SQLAlchemy:** ORM to facilitate communication between Python and the database.
  * **Requests:** To perform HTTP requests to product pages.
  * **BeautifulSoup4:** To parse HTML and extract the necessary information.
  * **Pandas:** For data manipulation and analysis (mainly in notebooks).
  * **python-dotenv:** To securely manage environment variables.

### 🚀 Getting Started

Follow these instructions to get a copy of the project running on your local machine.

#### Prerequisites

  * Python 3.9 or higher
  * Pip (Python package manager)
  * A running PostgreSQL server instance

#### Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/your-username/price-tracker.git](https://github.com/your-username/price-tracker.git)
    cd price-tracker
    ```

2.  **Create and configure your environment file:**
    Copy the `.env.example` file to a new file named `.env` and fill it with your PostgreSQL credentials.

    ```bash
    cp .env.example .env
    ```

    Your `.env` file should look like this:

    ```env
    POSTGRES_USER=your_user
    POSTGRES_PASSWORD=your_password
    POSTGRES_DB=price_tracker
    POSTGRES_HOST=localhost
    POSTGRES_PORT=5432
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Initialize the database:**
    This command will create the `prices` table in your database.

    ```bash
    python scripts/init_db.py
    ```

### ▶️ Usage

To run the price collection pipeline, execute the `updater.py` script. It will:

1.  Visit the URLs defined in `src/scraper.py`.
2.  Extract the data.
3.  Process and clean the information.
4.  Save the new price records to the database.

<!-- end list -->

```bash
python src/updater.py
```

### 🗂️ Project Structure

```
price-tracker/
│
├── data/         # Raw and processed data (if needed)
├── src/          # Main source code
│   ├── config.py
│   ├── db.py
│   ├── scraper.py
│   ├── processor.py
│   └── updater.py
├── scripts/      # Utility scripts (e.g., init_db.py)
├── .env          # Your environment variables (DO NOT commit)
├── .env.example  # Example file for variables
├── requirements.txt
└── README.md
```

### 🗺️ Roadmap

  * [ ] Add support for more stores.
  * [ ] Create a notification system (email, Telegram) for price drop alerts.
  * [ ] Develop a simple web interface (with Flask or FastAPI) for data visualization.
  * [ ] Containerize the application with Docker for easier deployment.
  * [ ] Add more analysis and visualizations in the notebooks.

### 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

### 👤 Contact

Seu Nome - [@dev_paulovsnts]((https://x.com/dev_paulovsnts)) 

Link do Projeto: [https://github.com/paulovsnts/Price_Tracker](https://www.google.com/search?q=https://github.com/paulovsnts/Price_Tracker)

```
```
