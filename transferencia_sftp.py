import paramiko
import os
import getpass

def transferencia_respuesta_sftp():
    # Configurar la conexión SSH
    cliente = paramiko.SSHClient()
    cliente.load_system_host_keys()
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Solicitar la contraseña del usuario
    password = getpass.getpass("Ingrese su contraseña para el usuario {}: ".format(os.getlogin()))

    # Conectarse a localhost con la contraseña
    cliente.connect('localhost', username=os.getlogin(), password=password)

    # Crear cliente SFTP
    sftp = cliente.open_sftp()

    # Definir el archivo de origen (respuesta de la consultora) y destino (Seguros Globales)
    archivo_origen = os.path.expanduser('~/SFTPTransfer/consultora/respuesta_reclamos.csv')
    archivo_destino = os.path.expanduser('~/SFTPTransfer/seguros_globales/respuesta_reclamos.csv')

    # Transferir el archivo
    sftp.put(archivo_origen, archivo_destino)
    print(f'Archivo de respuesta transferido a {archivo_destino}')

    # Cerrar la conexión SFTP
    sftp.close()
    cliente.close()

if __name__ == '__main__':
    transferencia_respuesta_sftp()




