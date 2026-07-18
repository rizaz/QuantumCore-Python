# Actividad 4.2 — Serialización y Persistencia (JSON)

**Grupo 4 — CEIPA — Fundamentos de Software**

Proyecto de Python que demuestra la serialización (Objeto → Diccionario →
JSON) y la deserialización (JSON → Diccionario → Objeto) de la clase
`TransaccionCredito`.

## Requisitos

- Python 3.8 o superior (no se necesita instalar ninguna librería externa;
  el módulo `json` viene incluido en Python).
- Visual Studio Code con la extensión oficial **Python** (de Microsoft).

## Cómo ejecutarlo en Visual Studio Code

1. Descomprime esta carpeta en tu computador.
2. Abre VS Code y ve a **Archivo → Abrir carpeta...** y selecciona la carpeta
   `proyecto_json`.
3. Si VS Code te pide seleccionar un intérprete de Python, elige cualquier
   Python 3 instalado en tu equipo.
4. Abre el archivo `main.py`.
5. Ejecuta el proyecto de cualquiera de estas dos formas:
   - Presiona **F5** (usa la configuración incluida en `.vscode/launch.json`).
   - O haz clic en el botón ▶ **Run Python File** en la esquina superior
     derecha del editor.
6. La salida se mostrará en la terminal integrada de VS Code.

## Cómo ejecutarlo desde la terminal (alternativa)

```bash
python main.py
```

## Estructura del proyecto

```
proyecto_json/
├── main.py              # Clases Transaccion / TransaccionCredito + demo
├── README.md             # Este archivo
└── .vscode/
    └── launch.json        # Configuración para ejecutar con F5 en VS Code
```

## Qué hace el script

1. Crea un objeto `TransaccionCredito` en memoria.
2. **Serializa** el objeto: lo convierte primero en un diccionario y luego
   en una cadena de texto JSON con `json.dumps()`.
3. **Deserializa** esa cadena JSON: la convierte de nuevo en un diccionario
   con `json.loads()` y con esos datos crea un **nuevo** objeto
   `TransaccionCredito`.
4. Verifica que el contenido reconstruido es igual al original, pero que
   se trata de una instancia distinta en memoria (demostrando que la
   serialización transporta el estado del objeto, no el objeto en sí).
