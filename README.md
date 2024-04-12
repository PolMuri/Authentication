## Authentication

Aquest programa proporciona una estructura bàsica per implementar un sistema d'autenticació utilitzant tokens d'autenticació JWT, que és un mètode comú per autenticar usuaris i les seves credencials i gestionar-los de forma segura en aplicacions web i altres sistemes. 

# Funcionalitats

-Permet registrar nous usuaris proporcionant la seva adreça de correu electrònic.
-Genera un token d'autenticació únic per a cada usuari registrat.
-Emmagatzema la informació dels usuaris, incloent-hi el seu correu electrònic i el token, en un fitxer de base de dades db.json.

Comanda d'ús:

``python3 register.py -e "correu@exemple.com"``

-Permet inicialitzar les contrasenyes per als usuaris existents.
-Cerca un usuari pel seu token i guarda un hash segur de la contrasenya proporcionada a db.json.

Comanda d'ús:

``python3 init.py -t token -p password``

-Facilita el procés d'inici de sessió pels usuaris registrats.
-Genera un token d'autorització (Bearer token) per a l'usuari proporcionat, permetent l'accés a recursos protegits.

Comanda d'ús:

``python3 login.py -e correu@exemple.com -p password``

-Permet verificar un token d'autorització JWT i mostrar el seu contingut (payload).
-Requereix la clau pública associada a la clau privada utilitzada durant el procés d'inici de sessió.

Comanda d'ús:

``python3 verify.py -t [tokenBearer]``

-t o --token: Bearer token a verificar.

Assegura't de substituir [tokenBearer] amb el teu token real. També és important tenir la llibreria PyJWT instal·lada: pip install PyJWT

Preparació de l'entorn i configuració inicial:

-El fitxer db.json representa la base de dades d'usuaris. Si no existeix, es crearà automàticament quan s'executi algun dels scripts. Ignorar fitxers sensibles

-El fitxer db.json s'ha d'afegir a l'arxiu .gitignore per a evitar que es carregui al repositori.

-Fitxers de clau o .pem: S'utilitzen fitxers de clau privada i pública per a la generació de tokens. Aquests fitxers estan exclosos del repositori per raons de seguretat.

