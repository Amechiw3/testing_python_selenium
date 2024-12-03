import yaml

class Config:
    def __init__(self, environment="config/config.yaml"):
        self.config_file = environment
        self.config_data = self.load_config()

    def load_config(self):
        """Carga el archivo de configuración YAML."""
        with open(self.config_file, "r") as file:
            return yaml.safe_load(file)

    def get(self, key, default=None):
        """Devuelve el valor de una clave en la configuración."""
        return self.config_data.get(key, default)

# Inicializa la configuración basada en el entorno
def get_config(environment="dev"):
    env_files = {
        "dev": "config/config_dev.yaml",
        "staging": "config/config_staging.yaml",
        "production": "config/config_production.yaml",
    }
    config_file = env_files.get(environment, "config/config.yaml")
    return Config(config_file)

# Ejemplo de inicialización
config = get_config("test")
