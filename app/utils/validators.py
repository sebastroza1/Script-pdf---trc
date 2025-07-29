import os
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'pdf'}
MAX_FILE_SIZE_MB = 10


def allowed_file(filename: str) -> bool:
    """Check file extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def validate_file(file_storage) -> bool:
    """Validate uploaded file type and size."""
    filename = secure_filename(file_storage.filename)
    if not allowed_file(filename):
        return False
    file_storage.seek(0, os.SEEK_END)
    file_size = file_storage.tell()
    file_storage.seek(0)
    if file_size > MAX_FILE_SIZE_MB * 1024 * 1024:
        return False
    return True
