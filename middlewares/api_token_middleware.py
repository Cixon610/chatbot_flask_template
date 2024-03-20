"""api_token_middleware"""
from functools import wraps
from flask import Flask, request, abort

from common.system_config import SystemConfig

app = Flask(__name__)


def validate_token(func):
    """validate_token"""
    @wraps(func)
    def decorated(*args, **kwargs):
        authorization = request.headers.get("Authorization")
        if not authorization:
            abort(401, "Authorization header is missing")

        token = authorization.split(" ")[1]
        valid_token = SystemConfig.get_api_token()
        if token != valid_token:
            abort(401, "Invalid token")
        return func(*args, **kwargs)

    return decorated
