Authentication

Funcionalitats

register.py Aquest script permet registrar nous usuaris i generar tokens d'autenticació. Utilitza el fitxer db.json com a base de dades per emmagatzemar la informació dels usuaris.
Comandament d'ús:

``python3 register.py -e "correu@exemple.com"``

init.py Aquest script permet inicialitzar contrasenyes per als usuaris existents. Busca un usuari pel seu token i emmagatzema un hash segur de la contrasenya dins de db.json.
Comandament d'ús:

``python3 init.py -t token -p password``

login.py Aquest script facilita el procés de login per als usuaris registrats. Genera un token bearer d'autenticació per a l'usuari proporcionat.
Comandament d'ús:

``python3 login.py -e correu@exemple.com -p 1234``

verify.py Aquest script permet verificar un bearer token JWT i mostrar el seu contingut (payload). S'ha de proporcionar la clau pública associada a la clau privada utilitzada durant el procés de login.

``python3 verify.py -t [tokenBearer]``

-t o --token: Bearer token a verificar.

Assegura't de substituir [tokenBearer] amb el teu token real. També és important tenir la llibreria PyJWT instal·lada: pip install PyJWT

Preparació de l'entorn i configuració inicial:

-El fitxer db.json representa la base de dades d'usuaris. Si no existeix, es crearà automàticament quan s'executi algun dels scripts. Ignorar fitxers sensibles

-El fitxer db.json s'ha d'afegir a l'arxiu .gitignore per a evitar que es carregui al repositori.

-Fitxers de clau o .pem: S'utilitzen fitxers de clau privada i pública per a la generació de tokens. Aquests fitxers estan exclosos del repositori per raons de seguretat.

