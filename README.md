# Proyecto de Testing Automatizado con Python y Selenium

Este proyecto implementa pruebas automatizadas utilizando **Selenium WebDriver**, **Pytest** y el patrón de diseño **Page Object Model (POM)** para organizar y mantener el código.

## 📚 Estructura del Proyecto

```plaintext
project/
├── config/
│   ├── config.yaml              # Configuración general
│   ├── config_dev.yaml          # Configuración para desarrollo
│   ├── config_staging.yaml      # Configuración para staging
│   ├── config_production.yaml   # Configuración para producción
├── pages/
│   ├── base_page.py             # Clase base para todas las páginas
│   ├── login_page.py            # POM para la página de login
│   ├── registration_page.py     # POM para la página de registro
│   ├── search_page.py           # POM para la página de búsqueda
├── tests/
│   ├── auth/
│   │   ├── test_login.py        # Pruebas de login
│   │   ├── test_registration.py # Pruebas de registro
│   ├── search/
│   │   ├── test_search.py       # Pruebas de búsqueda
│   ├── conftest.py              # Configuración de Pytest y fixtures
│   ├── test_homepage.py         # Pruebas generales de la página principal
├── utils/
│   ├── config.py                # Clase para manejar configuraciones
├── reports/                     # Carpeta para reportes generados
│   ├── html/                    # Reportes en HTML
│   ├── logs/                    # Archivos de logs
│   ├── screenshots/             # Capturas de pantalla
├── pytest.ini                   # Configuración global de Pytest
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Documentación del proyecto
```
## 🛠️ Instalación
1.  Clonar el repositorio
git clone https://github.com/Amechiw3/testing_python_selenium.git
cd tu_proyecto

2.Crear un entorno virtual
python -m venv venv
source venv/bin/activate    # En Linux/Mac
venv\Scripts\activate       # En Windows

3. Instalar dependencias
pip install -r requirements.txt


## 🚀 Uso del Proyecto
1. Configurar los valores en config/config.yaml
Edita el archivo config.yaml para definir la URL base, el navegador y las credenciales de prueba:
base_url: "http://example.com"
browser: "chrome"
credentials:
  user_email: "user@example.com"
  user_password: "password123"

2. Ejecutar pruebas
Ejecutar todas las pruebas:
pytest

Ejecutar pruebas específicas:

Solo pruebas de autenticación:
pytest -m auth

Generar un reporte HTML:
pytest --html=reports/html/report.html --self-contained-html

## 🧰 Herramientas Utilizadas
Python 3.8+: Lenguaje de programación.
Selenium: Herramienta para automatización de navegadores.
Pytest: Framework para pruebas.
Page Object Model (POM): Patrón de diseño para estructurar el código de las páginas.
YAML: Formato para archivos de configuración.

## 📦 Configuración de Entornos
El proyecto soporta configuraciones para diferentes entornos (desarrollo, staging, producción). Puedes cambiar el entorno cargando un archivo de configuración específico desde config/config.py.
Ejemplo:
from utils.config import get_config

config = get_config("staging")  # Cambia "staging" por "dev" o "production"
