import csv
import os

def procesar_respuesta():
    archivo_respuesta = os.path.expanduser('~/SFTPTransfer/seguros_globales/respuesta_reclamos.csv')

    # Leer el archivo de respuesta
    with open(archivo_respuesta, mode='r') as archivo:
        lector_csv = csv.reader(archivo)
        respuestas = list(lector_csv)

    # Mostrar los resultados
    print("Resultados de la validación de siniestros:")
    for respuesta in respuestas[1:]:  # Omitir encabezado
        print(f'Póliza {respuesta[0]}: {respuesta[1]}')

if __name__ == '__main__':
    procesar_respuesta()

