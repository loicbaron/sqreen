import flask
import hmac
import hashlib
import os

from flask import current_app
from functools import wraps

def check_signature(secret_key, request_signature, request_body):
    print(secret_key, request_signature, request_body)
    hasher = hmac.new(secret_key, request_body, hashlib.sha256)
    dig = hasher.hexdigest()

    return hmac.compare_digest(dig, request_signature)  

def verify_request_signature(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
          # for Flask:
          request_body = flask.request.get_data()
          request_signature = flask.request.headers['X-Sqreen-Integrity']
          secret_key = str.encode(current_app.config["SQREEN_NOTIFICATIONS_KEY"])

          if check_signature(secret_key, request_signature, request_body) is False:
            raise Exception("Signature is not recognized")

        except Exception as err:
          import traceback
          traceback.print_exc()
          # Forbidden
          flask.abort(403)

        return f(*args, **kwargs)

    return decorated_function