## First-term-exam---Practical: CRUD de Usuarios + Prueba Controlada de Fuerza Bruta
## Descripción
Este proyecto implementa una API REST con FastAPI que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre usuarios. Adicionalmente, incluye un script de fuerza bruta controlado (BruteForce.py) para demostrar vulnerabilidades asociadas a contraseñas débiles y medir los efectos de este tipo de ataques contra tu propia API.

Nota: El script de brute force está optimizado para simplicidad (usa itertools para generación y requests para POST). Prueba contraseñas alfanuméricas hasta longitud 4 (configurable). Para demo rápida, usa solo números y longitud 2.

## Guia del proyecto
~/proyecto_fastapi_brute/
├── main.py              # API con FastAPI (CRUD + endpoint /login)
├── BruteForce.py        # Script de ataque de fuerza bruta (Python puro, maneja 400/202)
├── bash.sh              # Launcher opcional para brute force (simple wrapper)
└── README.md            

main.py: Define la API con modelos Pydantic para usuarios (username, password). Incluye endpoints CRUD y login simple (retorna "Login successful" en 200 si coincide).
BruteForce.py: Genera passwords secuenciales (1 a MAX_LENGTH chars) y envía POST a /login. Ignora 400 (Bad Request), chequea éxito en 200/202. Config editable al inicio.
bash.sh: Script Bash simple para lanzar python3 BruteForce.py con chequeos (opcional; usa directo si prefieres).

## Instalación
1. Crear y Activar Entorno Virtual (Recomendado)
En WSL/Bash, desde ~/proyecto_fastapi_brute:

python3 -m venv venv
source venv/bin/activate  # Activa venv (prompt muestra (venv))

2. Instalar Dependencias
Crea requirements.txt si no existe (nano requirements.txt y pega):

fastapi[standard]==0.104.1
sqlmodel
requests==2.31.0

Asegura venv activado (source venv/bin/activate).

Desde la carpeta del proyecto (~/proyecto_fastapi_brute), ejecuta:
## Ejecución de la API
fastapi dev main.py --host 127.0.0.1 --port 8000
Esto inicia el servidor en http://127.0.0.1:8000 (o http://localhost:8000).
Logs: La terminal muestra requests (e.g., 200/400/202). No uses esta terminal para otros comandos.

## Endpoints Principales
* POST /users: Crear usuario (body: {"username": "test", "password": "12"}). Retorna 200 si OK, 400 si duplicado.
* GET /users: Listar todos los usuarios (JSON con usernames y passwords hashed/no en tu caso).
* GET /users/{id}: Obtener usuario por ID (e.g., /users/1).
* PUT /users/{id}: Actualizar usuario por ID (body como POST).
* DELETE /users/{id}: Eliminar usuario por ID.
* POST /login: Autenticar (body: {"username": "admin", "password": "1234"}). Retorna 200 con "Login successful" si correcto, 401/400 si falla.
Ejemplo manual con curl (API corriendo):

Crear user: curl -X POST "http://localhost:8000/users" -H "Content-Type: application/json" -d '{"username":"test","password":"12"}'

Login: curl -X POST "http://localhost:8000/login" -H "Content-Type: application/json" -d '{"username":"admin","password":"1234"}' → {"message":"Login successful"}

User por default: Asume "admin" con password "1234" (verifica en main.py o crea via POST).

## Ejecución del Ataque de Fuerza Bruta
La API debe estar corriendo en una terminal (con fastapi dev main.py).

Abre otra terminal (preferentemente WSL/Bash, en ~/proyecto_fastapi_brute), activa venv (source venv/bin/activate), y ejecuta:

## Con Launcher Bash 
chmod +x bash.sh  # Solo primera vez
./bash.sh

Qué hace: Lanza python3 BruteForce.py 4 con header y chequeos (e.g., si python3 existe). Config en bash.sh (edita TARGET_USER/MAX_LENGTH).

Salida: Similar a directo, con wrapper extra ("Ejecutando python3 BruteForce.py...").
