import csv
import os

def generar_reclamos():
    # Definir el archivo de destino
    archivo_reclamos = os.path.expanduser('~/SFTPTransfer/seguros_globales/reclamos.csv')

    # Definir los datos del reclamo
    datos_reclamos = [
        ['Número Póliza', 'Monto Reclamo', 'Fecha Siniestro', 'Descripción'],
        ['001', '1000', '2024-10-22', 'Choque leve'],
        ['002', '5000', '2024-10-21', 'Incendio en vivienda'],
        ['003', '750', '2024-10-20', 'Rotura de vidrio'],
    ]

    # Crear el archivo CSV
    with open(archivo_reclamos, mode='w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos_reclamos)

    print(f'Archivo de reclamos generado en {archivo_reclamos}')

if __name__ == '__main__':
    generar_reclamos()

