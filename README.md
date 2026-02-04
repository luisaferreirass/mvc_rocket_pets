# 🚀 MVC Rocket Pets

## 📝 Sobre o projeto

API de gerenciamento de pets desenvolvida seguindo o padrão arquitetural **MVC (Model-View-Controller)** com **Flask**. O projeto implementa um CRUD completo para cadastro e gerenciamento de animais de estimação, demonstrando boas práticas de organização de código e separação de responsabilidades.

Ideal para aprendizado de:
- Arquitetura MVC
- Framework Flask
- Organização de projetos Python
- Separação de camadas (Model, View, Controller)
- Banco de dados SQLite com SQLAlchemy
- APIs RESTful

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **Flask** - Framework web
- **Flask-SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados

## 🏗️ Arquitetura MVC

### Model
Representa a camada de dados, responsável pela lógica de negócio e interação com o banco de dados.

### View
Camada de apresentação, responsável por retornar respostas JSON para o cliente.

### Controller
Gerencia a comunicação entre Model e View, processando requisições e respostas.

## ⚙️ Como executar

### Pré-requisitos

- Python 3.x instalado
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/luisaferreirass/mvc_rocket_pets.git
cd mvc_rocket_pets
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install flask flask-sqlalchemy
```

### Executando a aplicação
```bash
python run.py
```

A API estará disponível em: `http://localhost:5000`

## 🎯 Funcionalidades

- ✅ **Cadastrar** novos pets
- 📖 **Listar** todos os pets cadastrados
- ✏️ **Editar** informações dos pets
- 🗑️ **Excluir** pets do sistema
- 🔍 **Visualizar** detalhes de cada pet

## 🛠️ Modelo de dados

### Pet

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Chave primária (auto-incremento) |
| name | String | Nome do pet |
| species | String | Espécie do animal |
| age | Integer | Idade do pet |
| owner | String | Nome do proprietário |

## 📸 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/pets` | Lista todos os pets |
| GET | `/pets/<id>` | Visualiza detalhes do pet |
| POST | `/pets` | Cadastra um novo pet |
| PUT | `/pets/<id>` | Atualiza informações do pet |
| DELETE | `/pets/<id>` | Exclui um pet |

## 🎨 Padrão MVC no projeto
```
Requisição HTTP
      ↓
  Controller (processa a requisição)
      ↓
   Model (acessa/manipula dados)
      ↓
   View (retorna JSON)
      ↓
  Resposta HTTP (JSON)
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👩‍💻 Autora

Desenvolvido por [Luisa Ferreira](https://github.com/luisaferreirass)
```

**About atualizado:**
```
API de gerenciamento de pets desenvolvida com Flask seguindo o padrão MVC. Implementa CRUD completo com arquitetura organizada em camadas (Model-View-Controller) e persistência de dados em SQLite.
