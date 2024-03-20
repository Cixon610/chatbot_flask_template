from flask_restx import Namespace, fields

base_output_payload = {
    "status": fields.String(required=True, default=0),
    "message": fields.String(required=True, default=""),
}

account_register_input_payload = {
    **base_output_payload,
    "email": fields.String(required=True, example="test01@gmail.com"),
    "password": fields.String(required=True, example="test"),
}

account_register_output_payload = {
    **base_output_payload,
    "email": fields.String(rexample="test01@gmail.com"),
    "qq": fields.String(example="test"),
}

# 建立namespace
ns = Namespace("chatbot", description="chatbot description")
# 建立model
req = ns.model("req", account_register_input_payload)
res = ns.model("res", account_register_output_payload)
