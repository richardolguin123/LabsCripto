# cesar.py
import sys

def cifrado_cesar(texto, desplazamiento):
    """
    Cifra un texto utilizando el algoritmo de Cifrado César.
    Conserva mayúsculas, minúsculas y otros caracteres como espacios.
    """
    resultado = ""
    for char in texto:
        if 'a' <= char <= 'z':
            # Maneja letras minúsculas
            offset = ord('a')
            resultado += chr((ord(char) - offset + desplazamiento) % 26 + offset)
        elif 'A' <= char <= 'Z':
            # Maneja letras mayúsculas
            offset = ord('A')
            resultado += chr((ord(char) - offset + desplazamiento) % 26 + offset)
        else:
            # Conserva caracteres que no son letras (espacios, números, etc.)
            resultado += char
    return resultado

if __name__ == "__main__":
    # Validar que se hayan proporcionado los argumentos correctos
    if len(sys.argv) != 3:
        print("Uso: python3 cesar.py \"<texto a cifrar>\" <desplazamiento>")
        sys.exit(1)

    # Obtener los argumentos de la línea de comandos
    texto_original = sys.argv[1]
    try:
        desplazamiento = int(sys.argv[2])
    except ValueError:
        print("Error: El desplazamiento debe ser un número entero.")
        sys.exit(1)

    # Cifrar e imprimir el resultado
    texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
    print(texto_cifrado)
