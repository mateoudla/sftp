import csv
import os

def procesar_siniestros():
    archivo_entrada = os.path.expanduser('~/SFTPTransfer/consultora/reclamos.csv')
    archivo_respuesta = os.path.expanduser('~/SFTPTransfer/consultora/respuesta_reclamos.csv')

    # Leer los reclamos
    with open(archivo_entrada, mode='r') as archivo:
        lector_csv = csv.reader(archivo)
        datos_reclamos = list(lector_csv)

    # Procesar los reclamos (simulación simple de validación)
    resultados = [['Número Póliza', 'Resultado']]
    for reclamo in datos_reclamos[1:]:  # Omitir encabezado
        if int(reclamo[1]) > 3000:
            resultado = 'Rechazado'
        else:
            resultado = 'Aprobado'
        resultados.append([reclamo[0], resultado])

    # Guardar los resultados en un nuevo archivo CSV
    with open(archivo_respuesta, mode='w', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(resultados)

    print(f'Respuesta generada en {archivo_respuesta}')

if __name__ == '__main__':
    procesar_siniestros()

