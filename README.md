###Registre d'Usuaris i Generació de Tokens

##Aquest programa, anomenat register.py, és una eina senzilla que permet registrar usuaris i generar tokens d'autenticació. Els usuaris s'emmagatzemen en un fitxer db.json, que actua com a base de dades en format JSON. Cada usuari es registra amb la seva adreça de correu electrònic i es genera un token aleatori de 32 caràcters que s'associa amb aquest usuari.

Com Utilitzar el Programa
Per utilitzar el programa, segueix aquests passos:

Assegura't de tenir Python 3 instal·lat al teu sistema.

Obre una terminal o línia de comandes i navega fins al directori on es troba l'arxiu register.py.

Executa el programa utilitzant la següent comanda i substitueix correu@example.com per l'adreça de correu electrònic que desitges registrar:

`python3 register.py -e "correu@example.com"`

El programa generarà un token aleatori i l'associarà amb l'adreça de correu electrònic proporcionada. També mostrarà el token a la pantalla.

Fitxer db.json
El programa utilitza un fitxer anomenat db.json per emmagatzemar les dades dels usuaris registrats. Assegura't que aquest fitxer es trobi en el mateix directori que register.py. Si l'arxiu no existeix, el programa el crearà automàticament.

Validació de Correu Electrònic
El programa utilitza una expressió regular per validar si l'adreça de correu electrònic proporcionada té un format vàlid. Si l'adreça de correu electrònic no compleix amb el format correcte (per exemple, si falta el símbol "@"), mostrarà un missatge d'error i no registrarà l'usuari.

