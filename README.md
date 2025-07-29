# PDF Extractor Flask App

Este proyecto permite cargar múltiples archivos PDF, extraer de ellos la fecha, nombre, cargo y empresa mediante expresiones regulares y generar un archivo Excel con los resultados.

## Instalación

1. Crear un entorno virtual y activarlo:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Exportar la variable `FLASK_APP` y ejecutar la aplicación:

```bash
export FLASK_APP=app.main
flask run
```

La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Configuración

- `SECRET_KEY`: clave secreta para Flask (opcional en variables de entorno).
- `UPLOAD_FOLDER`: carpeta donde se almacenan temporalmente los PDFs.

## Procesamiento asíncrono (opcional)

Si el volumen de PDFs es grande, se recomienda integrar Celery y Redis para manejar las tareas en segundo plano.
