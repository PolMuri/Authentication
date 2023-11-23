import json
import hashlib
import binascii
import argparse
from Crypto.PublicKey import RSA
import os
import secrets
import core



def generar_certs_si_no_existixen():
    if not os.path.exists("pem"):
        os.makedirs("pem")
    if not os.path.exists("pem/private.pem") or not os.path.exists("pem/receiver.pem"):
        # Generar claus si no existeixen
        key = RSA.generate(2048)

        private_key = key.export_key()
        with open("pem/private.pem", "wb") as file_out:
            file_out.write(private_key)

        public_key = key.publickey().export_key()
        with open("pem/receiver.pem", "wb") as file_out:
            file_out.write(public_key)

# Executa aquesta funció al principi del teu script
generar_certs_si_no_existixen()

# Funció per carregar la base de dades des d'un fitxer JSON (db.json)
def carregar_base_dades():
    try:
        with open('db.json', 'r') as file:
            data = json.load(file)
            if 'users' in data:
                return data['users']
            else:
                print('Error: No es pot trobar la llista d\'usuaris en el fitxer JSON.')
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def validar_contrasenya(email, password, database):
    for user in database:
        if user['email'] == email:
            salt = user['salt']  # Obtenir el salt emmagatzemat al db.json
            # Generar el hash utilitzant PBKDF2
            password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000).hex()
            if password_hash == user['hash']:
                return password_hash == user['hash']
    return False

# Funció principal
def main():
    parser = argparse.ArgumentParser(description='Login script')
    parser.add_argument('-e', '--email', help='Correu electrònic', required=True)
    parser.add_argument('-p', '--password', help='Contrasenya', required=True)
    args = parser.parse_args()

    email = args.email
    password = args.password

    # Carregar la base de dades d'usuaris
    database = carregar_base_dades()

    # Verificar si database és vàlid
    if not isinstance(database, list):
        print('Error: La base de dades no es pot llegir o no és en format JSON.')
        return

    # Validar la contrasenya
    if validar_contrasenya(email, password, database):
        # Si la contrasenya és vàlida, generar el token
        token = core.crearBearer(email)
        print(f'Token Bearer generat: {token}')
    else:
        print('Contrasenya no trobada per a aquest correu electrònic.')

if __name__ == "__main__":
    main()

