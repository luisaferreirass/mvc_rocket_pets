# 🚀 MVC Rocket Pets

## 📝 About the project

Pet management API built following the **MVC (Model-View-Controller)** architectural pattern with **Flask**. The project implements a complete CRUD for registering and managing pets, demonstrating good code organization practices and separation of concerns.

Great for learning:
- MVC architecture
- The Flask framework
- Python project organization
- Layer separation (Model, View, Controller)
- SQLite database with SQLAlchemy
- RESTful APIs

## 🚀 Technologies used

- **Python 3.x**
- **Flask** - Web framework
- **Flask-SQLAlchemy** - Database ORM
- **SQLite** - Database

## 🏗️ MVC Architecture

### Model
Represents the data layer, responsible for business logic and database interaction.

### View
Presentation layer, responsible for returning JSON responses to the client.

### Controller
Manages communication between Model and View, processing requests and responses.

## ⚙️ How to run

### Prerequisites

- Python 3.x installed
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/luisaferreirass/mvc_rocket_pets.git
cd mvc_rocket_pets
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install the dependencies:
```bash
pip install flask flask-sqlalchemy
```

### Running the application
```bash
python run.py
```

The API will be available at: `http://localhost:5000`

## 🎯 Features

- ✅ **Register** new pets
- 📖 **List** all registered pets
- ✏️ **Edit** pet information
- 🗑️ **Delete** pets from the system
- 🔍 **View** details of each pet

## 🛠️ Data model

### Pet

| Field | Type | Description |
|-------|------|-----------|
| id | Integer | Primary key (auto-increment) |
| name | String | Pet name |
| species | String | Animal species |
| age | Integer | Pet age |
| owner | String | Owner name |

## 📸 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-----------|
| GET | `/pets` | Lists all pets |
| GET | `/pets/<id>` | Shows pet details |
| POST | `/pets` | Registers a new pet |
| PUT | `/pets/<id>` | Updates pet information |
| DELETE | `/pets/<id>` | Deletes a pet |

## 🎨 MVC Pattern in the project
```
HTTP Request
      ↓
  Controller (handles the request)
      ↓
   Model (accesses/manipulates data)
      ↓
   View (returns JSON)
      ↓
  HTTP Response (JSON)
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License.

## 👩‍💻 Author

Developed by [Luisa Ferreira](https://github.com/luisaferreirass)
```

**Updated About:**
```
Pet management API built with Flask following the MVC pattern. Implements full CRUD with a layered (Model-View-Controller) architecture and data persistence in SQLite.
