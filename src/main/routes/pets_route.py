from flask import Blueprint, jsonify

# A partir das blueprints conseguimos dar um nome para uma certa
# Capacidade de rotas

pet_route_bp = Blueprint("pets_routes", __name__)
# Colocamos o __name__ para dizer que estamos nos referenciando ao projeto inteiro

@pet_route_bp.route("/pets", methods=["GET"])
def list_pets():
    return jsonify({"Ola": "mundo"}), 200
