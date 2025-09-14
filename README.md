
# Gerenciador de Filmes 🎬

> Aplicação web desenvolvida em Django para catalogar filmes e atores, consumindo a API da OMDb para popular o banco de dados.

## ✨ Funcionalidades

* **Gerenciamento de Models:**
    * CRUD completo (Criação, Leitura, Atualização e Exclusão) para a model Ator.
    * CRUD completo (Criação, Leitura, Atualização e Exclusão) para a model Filme.
* **Gerenciamento de Filmes:**
    * Criação de novos filmes no banco de dados através de uma busca na API externa da OMDb.
    * Listagem de todos os filmes salvos no banco, exibindo título e ano de lançamento.
    * Página de detalhes para cada filme, exibindo sinopse e a lista de atores associados.
    * Funcionalidade para gerenciar os atores associados.
    * Exclusão de filmes do catálogo local.

## 🛠️ Tecnologias Utilizadas

* **Back-end:**
    * Python 3.10.10
    * Django 
* **Front-end:**
    * HTML
    * Django Template Language (DTL)
* **Banco de Dados:**
    * PostgreSQL
* **APIs e Bibliotecas:**
    * OMDb API (que busca de dados de filmes)
    * `psycopg2-binary` (Driver de conexão com o PostgreSQL)
    * `python-dotenv` (Gerenciamento de variáveis de ambiente)

---

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### **Pré-requisitos**

Antes de começar, você vai precisar ter as seguintes ferramentas instaladas:
* [Git](https://git-scm.com)
* [Python 3.10.10](https://www.python.org/downloads/) ou superior
* [PostgreSQL](https://www.postgresql.org/download/)

### **1. Clonar o Repositório**

Clone este repositório
```bash
git clone https://github.com/Brunocmv1/wsBackend-Fabrica25.2.git
```
Acesse a pasta do projeto
```bash
cd wsBackend-Fabrica25.2
```

### **2. Criar e Ativar o Ambiente Virtual**

Crie o ambiente virtual
```bash
python -m venv venv
```
Ative o ambiente virtual

No Windows:
```bash
venv\Scripts\activate
```
No Linux ou macOS:
```bash
source venv/bin/activate
```

### **3. Instalar as Dependências**

Instale todas as bibliotecas necessárias dentro do ambiente virtual
```bash
pip install -r requirements.txt
```

### **4. Configurar o Banco de Dados (Variáveis de Ambiente)**

1. Crie um arquivo `.env` na raiz do projeto
2. Gere uma nova chave secreta do Django. Para gerar, use o shell do Django:

    No ambiente virtual digite:
    ```bash
    python manage.py shell
    ```
    ```bash
    from django.core.management.utils import get_random_secret_key
    ```
    ```bash
    get_random_secret_key()
    ```
    
3. No .env defina sua secret key
    ```bash
    SECRET_KEY="chave_secreta"
    DEBUG=True
    ```

4. crie o banco de dados no pgAdmin 4
5. Copie e cole o conteúdo abaixo no arquivo no `.env`, substituindo com as informações da sua instalação do PostgreSQL:

    ```env
    # Credenciais do seu Banco de Dados PostgreSQL Local
    DB_NAME=nome_do_seu_banco
    DB_USER=seu_usuario_postgres
    DB_PASSWORD=sua_senha_postgres
    DB_HOST=localhost
    DB_PORT=5432
    ```

### **5. Configurar o Banco de Dados**
Use o comando para passar as tabelas necessárias para o banco de dados PostgreSQL.
```bash
python manage.py migrate
```
Crie um usuário administrador para acessar o painel `/admin/`.
```bash
python manage.py createsuperuser
```

### **6. Rodar o Servidor**
```bash
python manage.py runserver
```