from flask import Flask
from routes.route import init_search_routes
from config.chroma_config import get_chroma_collection
from config.model_config import get_model

app = Flask(__name__)

# Init dependency (runtime)
collection = get_chroma_collection()
model = get_model()

# Register route
search_bp = init_search_routes(collection, model)
app.register_blueprint(search_bp)

if __name__ == "__main__":
    app.run(debug=True)