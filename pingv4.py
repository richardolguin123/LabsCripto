# pingv4.py
import sys
from scapy.all import IP, ICMP, send
import time

def enviar_caracter_icmp(destino, caracter):
    """
    Construye y envía un paquete ICMP Echo Request con un único carácter como payload.
    """
    # Construimos el paquete:
    # Capa IP: especificamos el destino. La IP de origen se establece automáticamente.
    # Capa ICMP: tipo 8 (Echo Request).
    # Payload: el carácter a enviar, codificado en bytes.
    paquete = IP(dst=destino)/ICMP(type=8, code=0)/bytes(caracter, 'utf-8')
    
    # Enviamos el paquete. verbose=0 para no imprimir información de Scapy en pantalla.
    send(paquete, verbose=0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: sudo python3 pingv4.py \"<texto cifrado a enviar>\"")
        sys.exit(1)

    # IP de destino. Usamos loopback (nuestra propia máquina) para la prueba.
    ip_destino = "127.0.0.1" 
    mensaje_cifrado = sys.argv[1]

    print(f"Enviando mensaje '{mensaje_cifrado}' a {ip_destino}...")

    for char in mensaje_cifrado:
        enviar_caracter_icmp(ip_destino, char)
        print(f"Carácter '{char}' enviado en un paquete ICMP.")
        # Agregamos una pequeña pausa para no saturar la red
        time.sleep(0.1)

    print("\nTransmisión de paquetes completada.")
