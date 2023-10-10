import json
import os
import secrets
import argparse
import base64
import re

# Funció per generar un token aleatori de 32 bytes en format string
def generate_token():
    token_bytes = secrets.token_bytes(32)  # Genera 32 bytes aleatoris
    token = base64.urlsafe_b64encode(token_bytes).decode('utf-8')[:32]
    return token

# Funció per afegir un nou usuari al fitxer db.json
def add_user(email, token, db_file):
    # Verifica si l'adreça d'email té un format vàlid utilitzant una expressió regular
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        print("L'adreça d'email no és vàlida.")
        return

    user_data = {"email": email, "token": token}
    
    # Carrega el contingut del fitxer db.json si existeix
    if os.path.exists(db_file):
        with open(db_file, 'r') as f:
            data = json.load(f)
    # Si el fitxer db.json no existeix, en lloc de generar un error, simplement crea una llista buida com a valor predeterminat. 
    # És útil per assegurar que sempre hi hagi un fitxer db.json disponible encara que sigui buit al principi.
    else:
        data = {"users": []}

    # Afegeix el nou usuari a la llista d'usuaris
    data["users"].append(user_data)

    # Crea el fitxer si no existeix amb les dades de la variable data i el sobreescriu amb les dades actualitzades si ja existeix
    with open(db_file, 'w') as f:
        json.dump(data, f, indent=4)

# Parseja els arguments de línia de comandes
# Si posem la comanda python3 register.py -help (en comptes de  -e "correucorreu") ens apareix un text 
# que com a descripció del programa explica el que hi ha a sota
parser = argparse.ArgumentParser(description="Registra un nou usuari i genera un token d\'autenticació.")
# Diu que es requereix la comanda -e o --email, si fem -h o --help veiem el comentari de sota on explica què fem amb  -e
parser.add_argument('-e', '--email', required=True, help="Correu electrònic de l\'usuari a registrar")
# Aquesta part del codi defineix que el programa espera rebre un argument d'email a través de la línia de comandes i que 
# aquest argument és obligatori. El valor de l'email que es passi es guardarà a l'objecte args i s'hi pot accedir utilitzant args.email dins del codi.
args = parser.parse_args()

# Genera un token aleatori
token = generate_token()

# Afegeix l'usuari i el token al fitxer db.json
add_user(args.email, token, 'db.json')

# Mostra el token per pantalla
print(token)
