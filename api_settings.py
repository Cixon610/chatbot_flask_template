from flask import Blueprint
from flask_restx import Api
from controllers.chat_bot_controller import ns as chatbot_ns


blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint, title="Gamania.ChatBot", doc="/doc/")

# flask_restx要把namespace註冊到api
api.add_namespace(chatbot_ns)
