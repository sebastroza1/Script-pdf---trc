"""Service for reading data from Excel files."""
from typing import List, Dict
import pandas as pd


def extract_data_from_excel(filepath: str) -> List[Dict[str, str]]:
    """Read an Excel file and return the records under the expected header.

    This function searches for the row that contains the columns ``Fecha``,
    ``Nombre``, ``Cargo`` and ``Empresa``. Once found, it loads only the
    rows below that header and returns them as a list of dictionaries.
    """

    # 1) Read the entire sheet without assuming a header
    df_raw = pd.read_excel(filepath, header=None, dtype=str)

    # 2) Locate the header row that matches our expected columns
    expected = ["Fecha", "Nombre", "Cargo", "Empresa"]
    header_idx = None
    for idx, row in df_raw.iterrows():
        values = [str(cell).strip() for cell in row.tolist()]
        normalized = [v.lower().replace(" ", "") for v in values[:4]]
        if normalized == [e.lower() for e in expected]:
            header_idx = idx
            break

    if header_idx is None:
        raise ValueError("No se encontró la fila de encabezado en el archivo.")

    # 3) Read again using the found header row
    df = pd.read_excel(
        filepath,
        header=header_idx,
        usecols=[0, 1, 2, 3],
        names=expected,
        dtype=str,
    )

    # 4) Drop completely empty rows
    df = df.dropna(how="all")

    # 5) Return list of records
    return df.to_dict(orient="records")
