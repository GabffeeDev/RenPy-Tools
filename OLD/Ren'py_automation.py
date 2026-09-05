from pathlib import Path
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

project_dir = filedialog.askdirectory(
    title="Selecciona la carpeta game de tu proyecto"
)

if not project_dir:
    print("Operación cancelada.")
    exit()

project_dir = Path(project_dir)

if project_dir.name != "game":
    print("Debes seleccionar la carpeta 'game'.")
    exit()

folders = [
    "images/bg",
    "images/cg",
    "audio/fx",
    "audio/bgm"
]

for folder in folders:
    (project_dir / folder).mkdir(parents=True, exist_ok=True)

print(f"Estructura creada en: {project_dir}")

