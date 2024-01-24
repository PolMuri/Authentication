import argparse
from jwt import (
    JWT,
    jwk_from_dict,
    jwk_from_pem,
)
import json

def verify_token(bearer_token):
    with open('pem/receiver.pem', 'rb') as fh:
        verifying_key = jwk_from_pem(fh.read())

    instance = JWT()
    try:
        decoded_token = instance.decode(bearer_token, verifying_key, do_time_check=True)
        print(decoded_token)
    except Exception as e:
        print(f"Error verifying token: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verifica un token bearer i mostra el missatge (payload) del JWT.")
    parser.add_argument('-t', '--token', required=True, help="Token Bearer a verificar")
    args = parser.parse_args()

    verify_token(args.token)
