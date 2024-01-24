import argparse
from jwt import (
    JWT,
    jwk_from_dict,
    jwk_from_pem,
)
import json

def verify_token(bearer_token):
    # Funció per verificar un token Bearer i mostrar el missatge (payload) del JWT.
    with open('pem/public.pem', 'rb') as fh:
        verifying_key = jwk_from_pem(fh.read())

    instance = JWT()
    try:
        # Intenta descodificar el token utilitzant la clau pública.
        decoded_token = instance.decode(bearer_token, verifying_key, do_time_check=True)
        print(decoded_token)
    except Exception as e:
        # En cas d'error, mostra un missatge d'error.
        print(f"Error verifying token: {e}")

if __name__ == "__main__":
    # Configuració de l'analitzador d'arguments de la línia de comandes.
    parser = argparse.ArgumentParser(description="Verifica un token bearer i mostra el missatge (payload) del JWT.")
    parser.add_argument('-t', '--token', required=True, help="Token Bearer a verificar")
    args = parser.parse_args()

    # Verifica el token utilitzant la funció definida anteriorment.
    verify_token(args.token)

