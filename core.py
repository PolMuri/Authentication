import hashlib
import secrets
import json
from datetime import datetime, timedelta, timezone

def update_user_token(data, token, password):
    for user in data["users"]:
        if user["token"] == token:
            user["token"] = None
            salt = secrets.token_hex(20)
            password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
            user["hash"] = password_hash.hex()
            user["salt"] = salt



from jwt import (
    JWT,
    jwk_from_dict,
    jwk_from_pem,
)
from jwt.utils import get_int_from_datetime

def crearBearer (mail):

    instance = JWT()

    message = {
        'mail': mail,
        'iat': get_int_from_datetime(datetime.now(timezone.utc)),
        'exp': get_int_from_datetime(
            datetime.now(timezone.utc) + timedelta(hours=1)),
    }

    """
    Encode the message to JWT(JWS).
    """

   
    # Or load a RSA key from a PEM file.
    with open('pem/private.pem', 'rb') as fh:
        signing_key = jwk_from_pem(fh.read())
    # You can also load an octet key in the same manner as the RSA.
    # signing_key = jwk_from_dict({'kty': 'oct', 'k': '...'})

    compact_jws = instance.encode(message, signing_key, alg='RS256')
    return compact_jws
    