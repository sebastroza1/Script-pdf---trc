"""Optional API blueprint placeholder."""
from flask import Blueprint, jsonify

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/status')
def status():
    """Return basic API status."""
    return jsonify({'status': 'ok'})
