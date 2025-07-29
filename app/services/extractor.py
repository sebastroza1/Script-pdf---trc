"""Service for extracting fields from PDFs."""
import re
from typing import Dict
import pdfplumber
from pdfplumber.utils.exceptions import PdfminerException, MalformedPDFException


DATE_PATTERN = re.compile(r"\b(\d{2}[/-]\d{2}[/-]\d{4})\b")
NAME_PATTERN = re.compile(r"Nombre[:\s]+([A-Za-zÁÉÍÓÚÑñ ]+)")
TITLE_PATTERN = re.compile(r"Cargo[:\s]+([A-Za-zÁÉÍÓÚÑñ ]+)")
COMPANY_PATTERN = re.compile(r"Empresa[:\s]+([A-Za-zÁÉÍÓÚÑñ ]+)")


def extract_fields_from_pdf(path: str) -> Dict[str, str]:
    """Extract date, name, title and company from a PDF file.

    Raises ``ValueError`` if the file is not a valid PDF that can be parsed.
    """
    data = {"Fecha": "", "Nombre": "", "Cargo": "", "Empresa": ""}

    try:
        with pdfplumber.open(path) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
    except (PdfminerException, MalformedPDFException, Exception) as e:
        raise ValueError(f"Invalid PDF file {path}: {e}") from e

    if match := DATE_PATTERN.search(text):
        data["Fecha"] = match.group(1)
    if match := NAME_PATTERN.search(text):
        data["Nombre"] = match.group(1).strip()
    if match := TITLE_PATTERN.search(text):
        data["Cargo"] = match.group(1).strip()
    if match := COMPANY_PATTERN.search(text):
        data["Empresa"] = match.group(1).strip()

    return data
