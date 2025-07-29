"""Blueprint handling file uploads and extraction."""
import os
import tempfile
from flask import Blueprint, render_template, request, current_app, send_file, flash, redirect, url_for, jsonify

from ..services.extractor import extract_fields_from_pdf
from ..services.excel import generate_excel
from ..services.storage import save_upload, list_uploaded_files
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

            info = save_upload(file)
            data = extract_fields_from_pdf(info["path"])
            results.append(data)

        if not results:
            flash('No valid PDFs processed')
            return redirect(request.url)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp:
            excel_path = generate_excel(results, tmp.name)

        return render_template('result.html', excel_file=os.path.basename(excel_path))

    files = list_uploaded_files()
    return render_template('upload.html', files=files)


@bp.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(tempfile.gettempdir(), filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    flash('File not found')
    return redirect(url_for('uploads.upload_files'))


@bp.route('/files')
def files_list():
    """Return list of uploaded PDF files."""
    files = [
        {"name": f["name"], "date": f["date"].isoformat()}
        for f in list_uploaded_files()
    ]
    return jsonify(files)
