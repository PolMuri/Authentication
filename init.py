import argparse
# Importa la funció update_user_token del mòdul core
from core import update_user_token 
# Importa les funcions load_data i save_data del mòdul db 
from db import load_data, save_data  

# Defineix la ruta de la base de dades
rutaDB = "db.json"  

# Configuració de l'argument parser
parser = argparse.ArgumentParser(description="Inicialitza un usuari i guarda les dades a la base de dades.")
parser.add_argument('-t', '--token', required=True, help="Token de l'usuari")
parser.add_argument('-p', '--password', required=True, help="Contrasenya de l'usuari")
# Analitza els arguments de la línia de comandes
args = parser.parse_args()  

# Carrega les dades actuals de la base de dades
data = load_data(rutaDB)  
# Actualitza la informació de l'usuari amb el token i la contrasenya proporcionats
update_user_token(data, args.token, args.password)
# Guarda les dades actualitzades a la base de dades  
save_data(data, rutaDB)  





