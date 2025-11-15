import paramiko
import socket

# Configuración
HOST = '127.0.0.1' # Localhost porque mapeamos el puerto 2222
PORT = 2222        # El puerto expuesto de S1
USER = 'prueba'
PASS = 'prueba'

try:
    # 1. Modificamos la versión de transporte de Paramiko
    # Esto es lo que cambia el "Banner" que se ve en Wireshark
    old_version = paramiko.transport.Transport._CLIENT_ID
    paramiko.transport.Transport._CLIENT_ID = "SSH-2.0-OpenSSH_?"

    print(f"[*] Intentando conectar con versión falsificada: {paramiko.transport.Transport._CLIENT_ID}")

    # 2. Crear conexión
    transport = paramiko.Transport((HOST, PORT))
    transport.connect(username=USER, password=PASS)

    print("[+] ¡Conexión Exitosa! El servidor aceptó nuestra versión extraña.")
    
    # Cerramos
    transport.close()

except Exception as e:
    print(f"[!] Error: {e}")
