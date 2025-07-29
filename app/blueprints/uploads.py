"""Blueprint handling file uploads and extraction."""
import os
import tempfile
from flask import Blueprint, render_template, request, current_app, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename

from ..services.extractor import extract_fields_from_pdf
from ..services.excel import generate_excel
from ..utils.validators import validate_file

# Explicitly tell Flask where to find the templates for this blueprint.
# They live one directory above this file in ``app/templates``.
bp = Blueprint('uploads', __name__, template_folder='../templates')


@bp.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        files = request.files.getlist('files')
        if not files:
            flash('No files selected')
            return redirect(request.url)

        results = []
        for file in files:
            if not validate_file(file):
                flash(f'Invalid file: {file.filename}')
                continue

            filename = secure_filename(file.filename)
            upload_dir = current_app.config['UPLOAD_FOLDER']
            os.makedirs(upload_dir, exist_ok=True)
            temp_path = os.path.join(upload_dir, filename)
            file.save(temp_path)

            data = extract_fields_from_pdf(temp_path)
            results.append(data)

        if not results:
            flash('No valid PDFs processed')
            return redirect(request.url)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp:
            excel_path = generate_excel(results, tmp.name)

        return render_template('result.html', excel_file=os.path.basename(excel_path))

    return render_template('upload.html')


@bp.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(tempfile.gettempdir(), filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    flash('File not found')
    return redirect(url_for('uploads.upload_files'))
