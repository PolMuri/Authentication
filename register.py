import argparse
import base64
import secrets
from db import add_user, is_valid_email  # Importa la funció "is_valid_email" des de "db.py".

# Funció per generar un token d'autenticació aleatori.
def generate_token():
    token_bytes = secrets.token_bytes(32)  # Genera 32 bytes aleatoris per al token.
    token = base64.urlsafe_b64encode(token_bytes).decode('utf-8')[:32]  # Converteix els bytes aleatoris en una cadena URL-segura de 32 caràcters.
    return token  

# Crea un analitzador d'arguments de línia de comandes per gestionar els arguments d'entrada.
parser = argparse.ArgumentParser(description="Registra un nou usuari i genera un token d'autenticació.")
parser.add_argument('-e', '--email', required=True, help="Correu electrònic de l'usuari a registrar")  # Defineix l'argument d'adreça de correu electrònic com obligatori.
args = parser.parse_args()  # Processa els arguments de línia de comandes i guarda els valors a l'objecte "args".

# Comprova si l'adreça de correu és vàlida abans de generar el token i afegir-lo a la base de dades.
if is_valid_email(args.email):
    token = generate_token()  # Genera un token d'autenticació cridant la funció "generate_token".
    add_user(args.email, token, 'db.json')  # Afegeix l'usuari i el token a la base de dades utilitzant la funció "add_user".
    print(token)  # Mostra el token generat per pantalla.
else:
    print("L'adreça d'email no és vàlida.")  # Mostra un missatge d'error si l'adreça de correu no és vàlida.




