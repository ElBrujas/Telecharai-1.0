import csv
from datetime import datetime

def obtener_evento(hora, dia, archivo_csv="agenda.csv"):
    """
    Obtiene el evento asociado a una hora y día específica desde un archivo CSV.
    
    Args:
        hora (str): La hora en formato "HH:MM:SS AM/PM".
        dia (str): El día de la semana (e.g., "lunes", "martes").
        archivo_csv (str): Ruta al archivo CSV con la agenda.
    
    Returns:
        str: El evento asociado o un mensaje indicando que no hay evento.
    """
    try:
        # Abrir el archivo CSV
        with open(archivo_csv, mode="r") as archivo:
            lector = csv.DictReader(archivo)
            
            # Iterar sobre las filas del archivo
            for fila in lector:
                if fila.get("") == hora:  # Columna de la hora
                    evento = fila.get(dia.lower(), "").strip()
                    return evento if evento else "No hay evento en este momento."
                    
    except FileNotFoundError:
        return "El archivo de agenda no se encontró."
    except KeyError:
        return f"El día '{dia}' no existe en la agenda."
    except Exception as e:
        return f"Error al procesar la agenda: {e}"