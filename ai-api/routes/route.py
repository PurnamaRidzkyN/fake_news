from flask import Blueprint
from controllers.search_controller import search_controller

search_bp = Blueprint("search", __name__)

def init_search_routes(collection, model):
    @search_bp.route("/search", methods=["POST"])
    def search():
        return search_controller(collection, model)

    return search_bp