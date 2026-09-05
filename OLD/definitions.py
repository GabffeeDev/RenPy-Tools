from pathlib import Path
import re

# ------------------------------
# Configuración
# ------------------------------

PROJECT = Path("E:/RENPY_GAMES/Patient_koharu")

TARGET = PROJECT / "game" / "images" / "definitions.rpy"
IMAGE_FOLDER = PROJECT / "game" / "images"


# ------------------------------
# Verificar rutas
# ------------------------------

if not IMAGE_FOLDER.exists():
    raise FileNotFoundError(f"No existe la carpeta de imágenes:\n{IMAGE_FOLDER}")

if not TARGET.exists():
    raise FileNotFoundError(f"No existe el archivo destino:\n{TARGET}")

# ------------------------------
# Generar definiciones
# ------------------------------

imagenes = []

for archivo in IMAGE_FOLDER.rglob("*"):
    if archivo.suffix.lower() not in [".png", ".jpg", ".jpeg", ".webp"]:
        continue

    # Ruta relativa a la carpeta de imágenes
    relativa = archivo.relative_to(IMAGE_FOLDER)

    # Nombre del archivo sin extensión
    nombre_png = archivo.stem

    # Ruta relativa a la carpeta game
    ruta_png = archivo.relative_to(PROJECT / "game").as_posix()

    # Nombre de la imagen (incluye carpetas)
    carpetas = list(relativa.parts[:-1])

    if carpetas:
        nombre_imagen = " ".join(carpetas + [nombre_png])
    else:
        nombre_imagen = nombre_png

    print(f"Nombre: {nombre_imagen}")
    print(f"Ruta: {ruta_png}")

    imagenes.append(f'image {nombre_imagen} = "{ruta_png}"')

print(f"Se encontraron {len(imagenes)} imágenes.")

imagenes.sort()
codigo = "\n".join(imagenes)

# ------------------------------
# Leer archivo destino
# ------------------------------

texto = TARGET.read_text(encoding="utf-8")

patron = re.compile(
    r"(# AUTO START\n)(.*?)(# AUTO END)",
    re.DOTALL
)

nuevo = patron.sub(
    lambda m: f"{m.group(1)}{codigo}\n{m.group(3)}",
    texto
)

TARGET.write_text(nuevo, encoding="utf-8")

print("¡Listo!")
print(f"Se generaron {len(imagenes)} definiciones.")