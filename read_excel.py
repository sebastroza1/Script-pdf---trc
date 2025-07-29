"""Utility script to display data from a generated Excel file."""
from app.services.excel_reader import extract_data_from_excel


if __name__ == '__main__':
    ruta_excel = 'resultados.xlsx'
    try:
        datos = extract_data_from_excel(ruta_excel)
        for i, fila in enumerate(datos, 1):
            print(f"Registro {i}:")
            print(f"  Fecha:   {fila['Fecha']}")
            print(f"  Nombre:  {fila['Nombre']}")
            print(f"  Cargo:   {fila['Cargo']}")
            print(f"  Empresa: {fila['Empresa']}")
            print('-' * 30)
    except Exception as e:
        print(f"Error al procesar el Excel: {e}")
