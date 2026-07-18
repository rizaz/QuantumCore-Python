"""
Actividad 4.2 - Serializacion y Persistencia (JSON)
Grupo 4 - CEIPA - Fundamentos de Software

Este script demuestra el proceso completo de:
  1) Serializacion: Objeto -> Diccionario -> Cadena JSON
  2) Deserializacion: Cadena JSON -> Diccionario -> Nuevo objeto

Para ejecutarlo en Visual Studio Code:
  1) Abre esta carpeta en VS Code (Archivo > Abrir carpeta...).
  2) Asegurate de tener la extension "Python" instalada y un interprete
     de Python 3 seleccionado (no se requieren librerias externas).
  3) Abre este archivo (main.py) y presiona el boton "Run" (▶) o usa
     el atajo Ctrl+F5 / F5.
  4) La salida aparecera en la terminal integrada.
"""

import json


class Transaccion:
    """Representa una transaccion bancaria generica (Semana 3)."""

    def __init__(self, cliente_id: str, tipo: str, monto: float):
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.monto = monto

    def __str__(self):
        return f"Transaccion [{self.tipo}] - ID: {self.cliente_id}, Monto: {self.monto}"


class TransaccionCredito(Transaccion):
    """Transaccion de tipo credito (hereda de Transaccion)."""

    def __init__(self, cliente_id: str, monto: float):
        super().__init__(cliente_id, "CREDITO", monto)


def serializar(transaccion: TransaccionCredito) -> str:
    """Convierte un objeto TransaccionCredito en una cadena de texto JSON."""

    # 1) Objeto -> Diccionario
    #    json.dumps no sabe leer objetos propios; primero se extraen
    #    los atributos a un diccionario simple de Python.
    datos_dict = {
        "cliente_id": transaccion.cliente_id,
        "tipo": transaccion.tipo,
        "monto": transaccion.monto,
    }
    # Alternativa mas generica (si el objeto no tiene atributos ocultos):
    # datos_dict = transaccion.__dict__

    # 2) Diccionario -> Cadena de texto en formato JSON
    json_string = json.dumps(datos_dict, indent=4)
    return json_string


def deserializar(json_string: str) -> TransaccionCredito:
    """Convierte una cadena de texto JSON de nuevo en un objeto TransaccionCredito."""

    # 1) Cadena JSON -> Diccionario
    datos_recuperados = json.loads(json_string)

    # 2) Diccionario -> Nuevo objeto TransaccionCredito
    transaccion_reconstruida = TransaccionCredito(
        cliente_id=datos_recuperados["cliente_id"],
        monto=datos_recuperados["monto"],
    )
    return transaccion_reconstruida


def main():
    print("=" * 60)
    print("PASO 1: Objeto en memoria")
    print("=" * 60)
    transaccion = TransaccionCredito(cliente_id="C-1045", monto=750000)
    print(transaccion)

    print("\n" + "=" * 60)
    print("PASO 2: Serializacion (Objeto -> JSON)")
    print("=" * 60)
    json_string = serializar(transaccion)
    print(json_string)
    print(type(json_string))  # <class 'str'> -> confirma que es texto

    print("\n" + "=" * 60)
    print("PASO 3: Deserializacion (JSON -> Objeto)")
    print("=" * 60)
    transaccion_reconstruida = deserializar(json_string)
    print(transaccion_reconstruida)

    print("\n" + "=" * 60)
    print("Verificacion")
    print("=" * 60)
    print("Mismo contenido:", str(transaccion) == str(transaccion_reconstruida))
    print("Misma instancia en memoria:", transaccion is transaccion_reconstruida)


if __name__ == "__main__":
    main()
