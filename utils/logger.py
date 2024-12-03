import logging
import os

def setup_logger(name="test_logger", log_file="reports/logs/test.log", level=logging.INFO):
    """Configura el logger para registrar mensajes."""
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Formato del logger
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Manejo de archivo
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # Manejo de consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Instancia global del logger
logger = setup_logger()