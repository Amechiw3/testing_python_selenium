
# Proyecto de Testing Automatizado con Python y Selenium

Este proyecto implementa pruebas automatizadas utilizando **Selenium WebDriver**, **Pytest** y el patrón de diseño **Page Object Model (POM)** para organizar y mantener el código.

## 📚 Estructura del Proyecto

```plaintext
testing_python_selenium/
├── reports/                               # Carpeta para reportes generados
│   ├── coverage/                          # Reportes de coverage
│   ├── html/                              # Reportes en HTML
│   ├── logs/                              # Archivos de logs
│   ├── screenshots/                       # Capturas de pantalla
│   ├── xml/                               # Reportes de junit
├── src/
│   ├── config/
│   │   ├── config.yaml                    # Configuración general
│   │   ├── config_dev.yaml                # Configuración para desarrollo
│   │   ├── config_staging.yaml	           # Configuración para staging
│   │   ├── config_production.yaml         # Configuración para producción
│   ├── pages/
│   │   ├── base_page.py                   # Clase base para todas las páginas
│   ├── tests/
│   │   ├── conftest.py                    # Configuración de Pytest y fixtures
│   ├── utils/
│   │   ├── config.py                      # Clase para manejar configuraciones
├── .pre-commit-config.yaml                # Configuración de hooks de pre-commit
├── .azure-pipelines.yml                   # Archivo de configuración para la CI con Azure Pipelines, que define los pasos de construcción, pruebas y despliegue del proyecto.
├── pytest.ini                             # Configuración global de Pytest
├── requirements.txt                       # Dependencias del proyecto
└── README.md                              # Documentación del proyecto
```
## 🛠️ Instalación
1.  Clonar el repositorio
```plaintext
git clone https://github.com/Amechiw3/testing_python_selenium.git
cd testing_python_selenium
```
2. Crear un entorno virtual
```ssh
python -m venv venv
source venv/bin/activate    # En Linux/Mac
venv\Scripts\activate       # En Windows
 ```
3. Instalar dependencias
```ssh
pip install -r requirements.txt
```

## 🚀 Uso del Proyecto
1. Configurar los valores en **config/config.yaml**
Edita el archivo config.yaml para definir la URL base, el navegador y las credenciales de prueba:
```plaintext
base_url: "http://example.com"
browser: "chrome"
credentials:
    user_email: "user@example.com"
    user_password: "password123"
```
2. Ejecutar pruebas
Ejecutar todas las pruebas:
```plaintext
pytest
```

Ejecutar pruebas específicas:
Solo pruebas de autenticación:
```
pytest -m auth
```
Generar un reporte HTML:
```
pytest --html=reports/html/report.html --self-contained-html
```

## 🧰 Herramientas Utilizadas
- Python 3.8+: Lenguaje de programación.
- Selenium: Herramienta para automatización de navegadores.
- Pytest: Framework para pruebas.
- Page Object Model (POM): Patrón de diseño para estructurar el código de las páginas.
- YAML: Formato para archivos de configuración.

## 📦 Configuración de Entornos
El proyecto soporta configuraciones para diferentes entornos (desarrollo, staging, producción). Puedes cambiar el entorno cargando un archivo de configuración específico **desde config/config.py**.

Ejemplo:
```
from utils.config import get_config
config = get_config("staging")  # Cambia "staging" por "dev" o "production"
```
