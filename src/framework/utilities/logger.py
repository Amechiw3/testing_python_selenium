import logging
import os


def setup_logger(logger_name="test_logger", log_file="reports/logs/test.log", level=logging.INFO):
    """Configura un logger con un nombre, archivo de log y nivel de log.

    Args:
        name (str, optional): Nombre del logger. Defaults to "test_logger".
        log_file (str, optional): Ubicacion donde se guardara el archivo de log. Defaults to "reports/logs/test.log".
        level (_type_, optional): Nivel del log. Defaults to logging.INFO.

    Returns:
        _type_: Logger configurado.
    """
    # Si el archivo de log no es el default, se crea una carpeta con el nombre del archivo
    if log_file != "reports/logs/test.log":
        log_file = f"reports/logs/{log_file}.log"

    # Crear la carpeta si no existe
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Formato del logger
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Manejo de archivo
    file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Manejo de consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Evitar agregar múltiples handlers al logger
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger