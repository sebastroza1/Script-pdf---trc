# Gestor de PDFs

Esta aplicación Flask permite subir múltiples archivos PDF y procesarlos para extraer información relevante. Utiliza un diseño moderno con Bootstrap 5 y ofrece carga de archivos mediante arrastrar y soltar. Ahora los documentos se procesan de forma concurrente para reducir el tiempo de espera.

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

Dependencias principales:
- Flask y Flask-WTF
- pdfplumber para leer PDFs
- pandas y openpyxl para generar Excel

## Configuración

- `SECRET_KEY`: clave secreta para Flask (opcional en variables de entorno).
- `UPLOAD_FOLDER`: carpeta donde se almacenan temporalmente los PDFs.

## Procesamiento asíncrono (opcional)

Si el volumen de PDFs es grande, se recomienda integrar Celery y Redis para manejar las tareas en segundo plano.

## Uso

1. Abre la página principal y arrastra varios PDFs al área azul.
2. Verás una lista previa de los archivos antes de enviarlos.
3. El sistema procesa los PDFs en paralelo para agilizar la generación del Excel.
4. Al terminar el procesamiento se mostrará un enlace para descargar el Excel.
