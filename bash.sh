#!/bin/bash

# Config simple 
TARGET_USER="admin"
MAX_LENGTH=4  #
# Nota: API_URL y CHARSET en BruteForce.py 

echo "=== LAUNCHER BASH: BRUTE FORCE VIA PYTHON ==="
echo "Usuario: $TARGET_USER | Max len: $MAX_LENGTH"
echo "Ejecutando python3 BruteForce.py $MAX_LENGTH..."
echo "----------------------------------------"

# Chequeo mínimo: Python y archivo
command -v python3 >/dev/null 2>&1 || { echo "Error: python3 no encontrado."; exit 1; }
[[ -f BruteForce.py ]] || { echo "Error: BruteForce.py no encontrado."; exit 1; }

# Llama a Python 
python3 BruteForce.py $MAX_LENGTH

echo "Ataque terminado."

# Si no encuentra al usuario
elapsed=$(( $(date +%s) - start_time ))
echo "No se encontró login hasta longitud $MAX_LENGTH. Intentos: $attempts | Tiempo: ${elapsed}s"
