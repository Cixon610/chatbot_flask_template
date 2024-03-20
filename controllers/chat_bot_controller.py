"""ChatBotController"""

from quart import request
from flask_restx import Resource
from models.view_models.schemas.chat_bot_schema import (
    ns,
    req,
    res,
)
from middlewares.api_token_middleware import validate_token
from models.view_models.chat_bot.message_req_vm import MessageReqVM
from services.chatbot_service import ChatbotService

_chatbotService = ChatbotService()


@validate_token
@ns.route("/message")
class Message(Resource):
    @ns.expect(req)
    @ns.marshal_with(res)
    async def post(self):
        """message"""
        req = MessageReqVM(**request.json)
        _chatbotService.active_message(req)


# @validate_token
# @ns.route("/image")
# class Image(Resource):
#     @ns.expect(req)
#     @ns.marshal_with(res)
#     def post(self):
#         """image"""
#         _chatbotService.active_message(request.json)


# @validate_token
# @ns.route("/vision")
# class Vision(Resource):
#     @ns.expect(req)
#     @ns.marshal_with(res)
#     def post(self):
#         """vision"""
#         _chatbotService.active_message(request.json)


# @validate_token
# @ns.route("/whisper")
# class Whisper(Resource):
#     @ns.expect(req)
#     @ns.marshal_with(res)
#     def post(self):
#         """whisper"""
#         _chatbotService.active_message(request.json)
