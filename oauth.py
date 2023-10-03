import json 
import names 

with open('bd.json', 'r') as fitxer:
    dades = json.load(fitxer)

    print(dades)

usuaris = []
    
for i in range(10000):
    #usuari = {...}: En cada iteració del bucle, es crea un diccionari anomenat usuari amb dos camps:
    #"nom": S'utilitza la funció names.get_first_name() per generar un nom aleatori utilitzant la biblioteca names. 
    # Aquest serà un nom aleatori per a l'usuari. "token": S'estableix el camp "token" com una cadena constant "authentication-token". 
    # A diferència del nom, el token és el mateix per a tots els usuaris.
    usuari = {
        "nom": names.get_first_name(),
        "token": "authentication-token"
    }
    dades["users"].append(usuari)

with open ('db2.json', 'w') as fitxer1:
    #dades que és on hem guardat les dades dels usuaris, archivo1 hi escriuré el contingut
    #ident4 l'utilitzo per especificar el nivell d'identació
    json.dump(dades, fitxer1, indent=4)
        
