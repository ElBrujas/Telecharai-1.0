import time
from threading import Thread
from modulos.consultor_evento import obtener_evento  # Importa la función previamente creada
from datetime import datetime

class MonitorAgenda:
    def __init__(self, ruta_csv, callback):
        """
        Inicializa el monitor de la agenda.
        
        Args:
            ruta_csv (str): Ruta al archivo CSV de la agenda.
            dia_actual (str): Día actual (e.g., "lunes", "martes").
            callback (function): Función a ejecutar cuando se detecte un evento.
        """
        self.ruta_csv = ruta_csv
        self.dia_actual = datetime.now().strftime("%A").lower()
        self.callback = callback
        self.running = False  # Control para detener el monitor
        self.hilo = None

    def iniciar_monitor(self):
        """Inicia el monitoreo de la agenda en un hilo separado."""
        if not self.running:
            self.running = True
            self.hilo = Thread(target=self._monitorear_agenda)
            self.hilo.start()
            print("Monitor de agenda iniciado.")

    def detener_monitor(self):
        """Detiene el monitoreo de la agenda."""
        if self.running:
            self.running = False
            self.hilo.join()  # Espera a que el hilo termine
            print("Monitor de agenda detenido.")

    def _monitorear_agenda(self):
        """Monitorea la agenda cada 30 segundos."""
        while self.running:
            hora_actual = datetime.now().strftime("%H:%M")
            evento = obtener_evento(hora_actual, self.dia_actual, self.ruta_csv)
            
            if evento and evento != "No hay evento en este momento.":
                self.callback(evento)

            if hora_actual == "00:00":
                self.dia_actual = datetime.now().strftime("%A").lower()

            time.sleep(30)  # Esperar 30 segundos antes de verificar de nuevo
