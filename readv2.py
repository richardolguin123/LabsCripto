# readv2.py
import sys
from scapy.all import rdpcap, ICMP, Raw

def descifrado_cesar(texto_cifrado, desplazamiento):
    """Descifra un texto cifrado con el Cifrado César."""
    # Descifrar es simplemente cifrar con el desplazamiento inverso.
    return cifrado_cesar(texto_cifrado, -desplazamiento)

def cifrado_cesar(texto, desplazamiento):
    """
    Función de cifrado (reutilizada de la Actividad 1) para el descifrado.
    """
    resultado = ""
    for char in texto:
        if 'a' <= char <= 'z':
            offset = ord('a')
            resultado += chr((ord(char) - offset + desplazamiento) % 26 + offset)
        elif 'A' <= char <= 'Z':
            offset = ord('A')
            resultado += chr((ord(char) - offset + desplazamiento) % 26 + offset)
        else:
            # Conserva caracteres que no son letras (espacios, números, etc.)
            resultado += char
    return resultado

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 readv2.py <archivo.pcapng>")
        sys.exit(1)

    archivo_pcap = sys.argv[1]
    
    # Leemos los paquetes del archivo de captura
    try:
        paquetes = rdpcap(archivo_pcap)
    except FileNotFoundError:
        print(f"Error: Archivo '{archivo_pcap}' no encontrado.")
        sys.exit(1)

    mensaje_cifrado_bytes = b''
    
    # Filtramos los paquetes para extraer el mensaje
    for pkt in paquetes:
        # Buscamos paquetes que tengan capa ICMP, capa Raw (payload) y sean Echo Request
        if pkt.haslayer(ICMP) and pkt[ICMP].type == 8 and pkt.haslayer(Raw):
            # Extraemos el primer byte del payload
            mensaje_cifrado_bytes += pkt[Raw].load[:1]

    mensaje_cifrado = mensaje_cifrado_bytes.decode('utf-8', errors='ignore')
    
    if not mensaje_cifrado:
        print("No se encontró un mensaje en los paquetes ICMP del archivo.")
        sys.exit(0)

    print(f"Mensaje cifrado extraído: {mensaje_cifrado}\n")
    print("Realizando ataque de fuerza bruta...\n")

    # Realizamos el ataque de fuerza bruta e imprimimos todas las combinaciones
    for i in range(26):
        mensaje_descifrado = descifrado_cesar(mensaje_cifrado, i)
        # Imprimimos cada posible resultado con su número de desplazamiento
        print(f"Desplazamiento {i}: {mensaje_descifrado}")
