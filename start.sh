#!/bin/bash

# Ruta del archivo de log
LOGFILE="run.log"

# Ejecuta el programa y redirige las salidas
python run.py >> "$LOGFILE" 2>&1
