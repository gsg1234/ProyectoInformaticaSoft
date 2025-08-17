import random
import time
import os
from pathlib import Path

# Archivo en la misma carpeta que este script
ARCHIVO = Path(__file__).with_name("numero.txt")

HEADER = "##################################################\n"

try:
    while True:
        n = random.randint(1, 100)
        contenido = f"{HEADER}El numero es: {n}\n{HEADER}"

        # Escribir primero a un archivo temporal y luego reemplazar
        tmp = ARCHIVO.with_suffix(".tmp")
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            f.write(contenido)
            f.flush()
            os.fsync(f.fileno())  # fuerza a disco

        os.replace(tmp, ARCHIVO)  # reemplazo atómico
        print(f"Escribí: {n}", end="\r", flush=True)

        time.sleep(0.2)

except KeyboardInterrupt:
    print("\nDetenido por el usuario.")
