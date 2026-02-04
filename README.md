# 🚀 MVC Rocket Pets

## 📝 Sobre o projeto

Sistema de gerenciamento de pets desenvolvido seguindo o padrão arquitetural **MVC (Model-View-Controller)** com **Flask**. O projeto implementa um CRUD completo para cadastro e gerenciamento de animais de estimação, demonstrando boas práticas de organização de código e separação de responsabilidades.

Ideal para aprendizado de:
- Arquitetura MVC
- Framework Flask
- Organização de projetos Python
- Separação de camadas (Model, View, Controller)
- Banco de dados SQLite com SQLAlchemy

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **Flask** - Framework web
- **Flask-SQLAlchemy** - ORM para banco de dados
- **SQLite** - Banco de dados
- **HTML/CSS** - Interface do usuário
- **Jinja2** - Template engine

## 🏗️ Arquitetura MVC

### Model
Representa a camada de dados, responsável pela lógica de negócio e interação com o banco de dados.

### View
Camada de apresentação, responsável pela interface com o usuário através de templates HTML.

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

A aplicação estará disponível em: `http://localhost:5000`

## 📁 Estrutura do projeto
```
mvc_rocket_pets/
├── app/
│   ├── __init__.py           # Inicialização da aplicação
│   ├── models/
│   │   └── pet.py           # Model de Pet
│   ├── controllers/
│   │   └── pet_controller.py # Controller de Pet
│   ├── views/
│   │   └── templates/       # Templates HTML
│   └── static/
│       └── css/             # Arquivos CSS
├── instance/
│   └── pets.db              # Banco de dados SQLite
├── run.py                   # Arquivo principal para executar a aplicação
└── README.md
```

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

## 📸 Rotas da aplicação

| Rota | Método | Descrição |
|------|--------|-----------|
| `/` | GET | Lista todos os pets |
| `/pet/create` | GET, POST | Cadastra um novo pet |
| `/pet/<id>` | GET | Visualiza detalhes do pet |
| `/pet/update/<id>` | GET, POST | Atualiza informações do pet |
| `/pet/delete/<id>` | POST | Exclui um pet |

## 🎨 Padrão MVC no projeto
```
Requisição HTTP
      ↓
  Controller (processa a requisição)
      ↓
   Model (acessa/manipula dados)
      ↓
   View (renderiza template)
      ↓
  Resposta HTTP
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👩‍💻 Autora

Desenvolvido por [Luisa Ferreira](https://github.com/luisaferreirass)
