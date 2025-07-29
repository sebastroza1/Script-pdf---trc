"""Service for handling temporary storage of uploaded files."""
from datetime import datetime
import os
from flask import current_app
from werkzeug.utils import secure_filename


def save_upload(file_storage):
    """Save uploaded file to the configured UPLOAD_FOLDER and return metadata."""
    upload_dir = current_app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_dir, exist_ok=True)
    filename = secure_filename(file_storage.filename)
    path = os.path.join(upload_dir, filename)
    file_storage.save(path)
    return {"name": filename, "path": path, "date": datetime.utcnow()}


def list_uploaded_files():
    """Return list of uploaded PDF files with upload timestamp."""
    upload_dir = current_app.config["UPLOAD_FOLDER"]
    if not os.path.isdir(upload_dir):
        return []
    files = []
    for name in os.listdir(upload_dir):
        if name.lower().endswith(".pdf"):
            path = os.path.join(upload_dir, name)
            timestamp = datetime.fromtimestamp(os.path.getmtime(path))
            files.append({"name": name, "date": timestamp})
    return sorted(files, key=lambda x: x["date"], reverse=True)
