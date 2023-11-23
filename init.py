import argparse
from core import update_user_token
from db import load_data, save_data

rutaDB = "db.json"

parser = argparse.ArgumentParser(description="Inicialitza un usuari i guarda les dades a la base de dades.")
parser.add_argument('-t', '--token', required=True, help="Token de l'usuari")
parser.add_argument('-p', '--password', required=True, help="Contrasenya de l'usuari")
args = parser.parse_args()

data = load_data(rutaDB)
update_user_token(data, args.token, args.password)
save_data(data, rutaDB)




