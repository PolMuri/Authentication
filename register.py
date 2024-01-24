import argparse
import base64
import secrets
from db import add_user, is_valid_email  # Importa la funció "is_valid_email" des de "db.py".

# Funció per generar un token d'autenticació aleatori.
def generate_token():
    # Genera 32 bytes aleatoris per al token.
    token_bytes = secrets.token_bytes(32) 
    # Converteix els bytes aleatoris en una cadena URL-segura de 32 caràcters. 
    token = base64.urlsafe_b64encode(token_bytes).decode('utf-8')[:32]  
    return token  

# Crea un analitzador d'arguments de línia de comandes per gestionar els arguments d'entrada.
parser = argparse.ArgumentParser(description="Registra un nou usuari i genera un token d'autenticació.")
# Defineix l'argument d'adreça de correu electrònic com obligatori.
parser.add_argument('-e', '--email', required=True, help="Correu electrònic de l'usuari a registrar") 
# Processa els arguments de línia de comandes i guarda els valors a l'objecte "args". 
args = parser.parse_args()  

# Comprova si l'adreça de correu és vàlida abans de generar el token i afegir-lo a la base de dades.
if is_valid_email(args.email):
    # Genera un token d'autenticació cridant la funció "generate_token".
    token = generate_token()  
    # Afegeix l'usuari i el token a la base de dades utilitzant la funció "add_user".
    add_user(args.email, token, 'db.json') 
    # Mostra el token generat per pantalla. 
    print(token)  
else:
    # Mostra un missatge d'error si l'adreça de correu no és vàlida.
    print("L'adreça d'email no és vàlida.")  




