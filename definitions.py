from pathlib import Path
import re

# ------------------------------
# Configuración
# ------------------------------

# Carpeta raíz del proyecto
PROJECT = Path(r"E:/RENPY_GAMES//JustABook")

# Archivo .rpy que quieres modificar
TARGET = PROJECT / "game" / "mod_assets" / "definitions" / "definitions.rpy"

# Carpeta de imágenes
IMAGE_FOLDER = PROJECT / "game" / "mod_assets" / "images"

# ------------------------------
# Generar definiciones
# ------------------------------

imagenes = []

for archivo in IMAGE_FOLDER.rglob("*"):

    if archivo.suffix.lower() not in [".png", ".jpg", ".jpeg", ".webp"]:
        continue

    # Ruta relativa
    relativa = archivo.relative_to(IMAGE_FOLDER)

    # Nombre de la imagen
    #
    # images/yuri/happy.png
    # ->
    # image yuri happy

    # Nombre del archivo sin extensión
    nombre_png = archivo.stem

    # Ruta relativa al proyecto
    ruta_png = archivo.relative_to(PROJECT).as_posix()

    # Si quieres incluir las carpetas en el nombre de la imagen
    carpetas = list(relativa.parts[:-1])

    if carpetas:
        nombre_imagen = " ".join(carpetas + [nombre_png])
    else:
        nombre_imagen = nombre_png

    print(f"Nombre: {nombre_imagen}")
    print(f"Ruta: {ruta_png}")

    # Generar la definición
    imagenes.append(
        f'image {nombre_imagen} = "{ruta_png}"'
    )

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
print(f"Se generaron {len(imagenes)} imágenes.")