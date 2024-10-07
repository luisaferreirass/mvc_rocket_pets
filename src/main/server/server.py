# vamos configurar nossa aplicação nos modelos iniciais
from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

# Importar blueprints
from src.main.routes.pets_route import pet_route_bp
from src.main.routes.person_routes import person_route_bp

db_connection_handler.connect_to_db() 
# Primeiro estamos nos conectando ao banco de dados depois estamos 
# ligando a aplicação

app = Flask(__name__)
CORS(app) # ?

app.register_blueprint(pet_route_bp)
app.register_blueprint(person_route_bp)
# Todas as rotas que colocamos nesse bluprint estão
# cadastradas no nosso app
