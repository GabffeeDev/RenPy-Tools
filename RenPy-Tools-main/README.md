# RenPy Tools

Aplicación gráfica para automatizar tareas comunes en proyectos de Ren'Py.

## Herramientas actuales

### Crear estructura de carpetas
Crea dentro de `game`:

- `images/bg`
- `images/cg`
- `audio/fx`
- `audio/bgm`

### Generar definiciones de imágenes
Busca archivos `.png`, `.jpg`, `.jpeg` y `.webp` dentro de `game/images` y genera automáticamente definiciones de Ren'Py en:

`game/images/definitions.rpy`

Las definiciones se mantienen entre:

```rpy
# AUTO START
# AUTO END
```

## Crear el .exe para Windows

1. Instala Python 3 en Windows.
2. Abre `build_windows.bat`.
3. El ejecutable aparecerá en:

`dist/RenPy Tools.exe`

El usuario final **no necesita instalar Python** para usar el `.exe` generado con PyInstaller.
