import logging
import os

def setup_logger(name="test_logger", log_file="reports/logs/test.log", level=logging.INFO):
    """Configura el logger para registrar mensajes."""
    # Si el archivo de log no es el default, se crea una carpeta con el nombre del archivo
    if log_file != "reports/logs/test.log":
        log_file =  f"reports/logs/{log_file}.log"

    # Crear la carpeta si no existe
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Formato del logger
    #formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Manejo de archivo
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Manejo de consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger