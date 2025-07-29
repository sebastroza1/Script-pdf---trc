"""Service for generating Excel files from extracted data."""
from typing import List, Dict
import os
import pandas as pd


def generate_excel(data: List[Dict[str, str]], output_path: str) -> str:
    """Generate an Excel file from the provided data."""
    df = pd.DataFrame(data, columns=["Fecha", "Nombre", "Cargo", "Empresa"])
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_excel(output_path, index=False)
    return output_path
