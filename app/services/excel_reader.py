"""Service for reading data from Excel files."""
from typing import List, Dict, Union
import pandas as pd


def extract_data_from_excel(excel_path: str, sheet_name: Union[str, int] = 0) -> List[Dict[str, str]]:
    """Load Excel file and return records with Fecha, Nombre, Cargo and Empresa."""
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    expected_cols = ["Fecha", "Nombre", "Cargo", "Empresa"]
    for col in expected_cols:
        if col not in df.columns:
            raise ValueError(f"Columna esperada '{col}' no encontrada en el Excel.")
    records = df[expected_cols].to_dict(orient="records")
    return records
