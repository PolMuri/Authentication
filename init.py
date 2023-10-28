# init.py
import argparse  # Importem la llibreria argparse per processar els arguments de línia de comandes.
import hashlib   # Importem la llibreria hashlib per realitzar operacions criptogràfiques.
import secrets   # Importem la llibreria secrets per generar valors aleatoris segurs.
from db import load_data, save_data, is_valid_email  # Importem funcions del fitxer "db.py".

rutaDB = "db.json"  # Definim la ruta del fitxer de base de dades "db.json".

def update_user_by_token(token, password, db_file):
    data = load_data(db_file)  # Carreguem les dades de la base de dades des del fitxer "db.json".

    for user in data["users"]:
        if user["token"] == token:  # Comprovem si el token correspon a l'usuari.
            user["token"] = None  # Desactivem el token de l'usuari.

            # Generem un salt aleatori amb la funció "token_hex" de la llibreria "secrets".
            salt = secrets.token_hex(20)
            # Creem un hash segur de la contrasenya utilitzant "pbkdf2_hmac" de "hashlib".
            password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
            user["hash"] = password_hash.hex()  # Assignem el hash resultant a l'usuari.
            user["salt"] = salt  # Assignem el salt generat a l'usuari.

            save_data(data, db_file)  # Desem les dades actualitzades al fitxer "db.json".

parser = argparse.ArgumentParser(description="Inicialitza un usuari i guarda les dades a la base de dades.")
# Definim els arguments de línia de comandes necessaris per a l'execució del script.
parser.add_argument('-t', '--token', required=True, help="Token de l'usuari")
parser.add_argument('-p', '--password', required=True, help="Contrasenya de l'usuari")
args = parser.parse_args()  # Processa els arguments de línia de comandes i els guarda a la variable "args".

update_user_by_token(args.token, args.password, rutaDB)  # Crida la funció per actualitzar les dades de l'usuari.

# Actualitzem les dades de l'usuari utilitzant el token i la contrasenya proporcionats.
update_user_by_token(args.token, args.password, rutaDB)


