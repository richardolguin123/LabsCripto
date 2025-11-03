from Crypto.Cipher import AES, DES, DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import sys
import base64 

def ajustar_clave(clave_original_bytes, tamano_requerido):
    """
    Ajusta la clave al tamaño requerido.
    Rellena si es corta, trunca si es larga.
    """
    longitud_original = len(clave_original_bytes)
   
    if longitud_original < tamano_requerido:
        bytes_faltantes = tamano_requerido - longitud_original
        padding = get_random_bytes(bytes_faltantes)
        print(f"    (Clave ajustada: {longitud_original} bytes -> {tamano_requerido} bytes. Añadido relleno aleatorio.)")
        return clave_original_bytes + padding
       
    elif longitud_original > tamano_requerido:
        print(f"    (Clave ajustada: {longitud_original} bytes -> {tamano_requerido} bytes. Clave truncada.)")
        return clave_original_bytes[:tamano_requerido]
       
    else:
        print(f"    (Clave ajustada: Tamaño correcto de {tamano_requerido} bytes.)")
        return clave_original_bytes

def cifrar_des(texto_bytes, clave_bytes, iv_bytes):
    print("\n--- Cifrando con DES ---")
    try:
        clave_ajustada = ajustar_clave(clave_bytes, 8)
        iv_ajustado = ajustar_clave(iv_bytes, 8)
       
        cifrador = DES.new(clave_ajustada, DES.MODE_CBC, iv_ajustado)
       
        texto_rellenado = pad(texto_bytes, DES.block_size)
        texto_cifrado = cifrador.encrypt(texto_rellenado)
       
        print(f"Clave final usada (bytes): {clave_ajustada}")
        print(f"IV final usado (bytes):    {iv_ajustado}")
        print(f"Texto Cifrado (bytes):   {texto_cifrado}")
       
        texto_cifrado_hex = texto_cifrado.hex()
        texto_cifrado_base64 = base64.b64encode(texto_cifrado).decode('utf-8')
       
        print(f"Texto Cifrado (Hex):     {texto_cifrado_hex}")
        print(f"Texto Cifrado (Base64):  {texto_cifrado_base64}")

        descifrador = DES.new(clave_ajustada, DES.MODE_CBC, iv_ajustado)
        texto_descifrado_rellenado = descifrador.decrypt(texto_cifrado)
        texto_descifrado = unpad(texto_descifrado_rellenado, DES.block_size)
        print(f"Texto Descifrado:        {texto_descifrado.decode('utf-8')}")
       
    except Exception as e:
        print(f"ERROR en DES: {e}")

def cifrar_3des(texto_bytes, clave_bytes, iv_bytes):
    print("\n--- Cifrando con 3DES ---")
    try:
        clave_ajustada = ajustar_clave(clave_bytes, 24)
        iv_ajustado = ajustar_clave(iv_bytes, 8)
       
        cifrador = DES3.new(clave_ajustada, DES3.MODE_CBC, iv_ajustado)
       
        texto_rellenado = pad(texto_bytes, DES3.block_size)
        texto_cifrado = cifrador.encrypt(texto_rellenado)

        print(f"Clave final usada (bytes): {clave_ajustada}")
        print(f"IV final usado (bytes):    {iv_ajustado}")
        print(f"Texto Cifrado (bytes):   {texto_cifrado}")

        texto_cifrado_hex = texto_cifrado.hex()
        texto_cifrado_base64 = base64.b64encode(texto_cifrado).decode('utf-8')
       
        print(f"Texto Cifrado (Hex):     {texto_cifrado_hex}")
        print(f"Texto Cifrado (Base64):  {texto_cifrado_base64}")

        descifrador = DES3.new(clave_ajustada, DES3.MODE_CBC, iv_ajustado)
        texto_descifrado_rellenado = descifrador.decrypt(texto_cifrado)
        texto_descifrado = unpad(texto_descifrado_rellenado, DES3.block_size)
        print(f"Texto Descifrado:        {texto_descifrado.decode('utf-8')}")

    except Exception as e:
        print(f"ERROR en 3DES: {e}")

def cifrar_aes256(texto_bytes, clave_bytes, iv_bytes):
    print("\n--- Cifrando con AES-256 ---")
    try:
        clave_ajustada = ajustar_clave(clave_bytes, 32)
        iv_ajustado = ajustar_clave(iv_bytes, 16)
       
        cifrador = AES.new(clave_ajustada, AES.MODE_CBC, iv_ajustado)
       
        texto_rellenado = pad(texto_bytes, AES.block_size)
        texto_cifrado = cifrador.encrypt(texto_rellenado)

        print(f"Clave final usada (bytes): {clave_ajustada}")
        print(f"IV final usado (bytes):    {iv_ajustado}")
        print(f"Texto Cifrado (bytes):   {texto_cifrado}")

        texto_cifrado_hex = texto_cifrado.hex()
        texto_cifrado_base64 = base64.b64encode(texto_cifrado).decode('utf-8')
       
        print(f"Texto Cifrado (Hex):     {texto_cifrado_hex}")
        print(f"Texto Cifrado (Base64):  {texto_cifrado_base64}")

        descifrador = AES.new(clave_ajustada, AES.MODE_CBC, iv_ajustado)
        texto_descifrado_rellenado = descifrador.decrypt(texto_cifrado)
        texto_descifrado = unpad(texto_descifrado_rellenado, AES.block_size)
        print(f"Texto Descifrado:        {texto_descifrado.decode('utf-8')}")

    except Exception as e:
        print(f"ERROR en AES-256: {e}")


def main():
    print("--- Laboratorio 4: Cifrado Simétrico ---")
   
    print("Por favor, ingrese los datos como texto (serán convertidos a bytes usando UTF-8).")

    try:
        texto_plano_str = input("Ingrese el texto a cifrar: ")
        texto_plano_bytes = texto_plano_str.encode('utf-8')

        key_str = input("Ingrese la CLAVE (Key): ")
        key_bytes_original = key_str.encode('utf-8')

        iv_str = input("Ingrese el IV (Vector de Inicialización): ")
        iv_bytes_original = iv_str.encode('utf-8')

        print("\n--- Datos recibidos (en bytes) ---")
        print(f"Texto Plano Original: {texto_plano_bytes}")
        print(f"Clave Original:       {key_bytes_original}")
        print(f"IV Original:          {iv_bytes_original}")
       
        cifrar_des(texto_plano_bytes, key_bytes_original, iv_bytes_original)
        cifrar_3des(texto_plano_bytes, key_bytes_original, iv_bytes_original)
        cifrar_aes256(texto_plano_bytes, key_bytes_original, iv_bytes_original)

    except Exception as e:
        print(f"Error fatal al leer la entrada: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
