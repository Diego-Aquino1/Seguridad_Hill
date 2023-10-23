import numpy as np

# Función para cifrar un mensaje usando el cifrado Hill
def cifrar_hill(matriz_clave, mensaje):
    n = len(matriz_clave)
    mensaje = mensaje.upper()  # Convertir el mensaje a mayúsculas
    while len(mensaje) % n != 0:
        mensaje += 'X'  # Asegurarse de que el mensaje sea un múltiplo del tamaño de la matriz clave

    matriz_resultado = []

    for i in range(0, len(mensaje), n):
        bloque = mensaje[i:i + n]
        indices = [ord(char) - ord('A') for char in bloque]
        resultado = np.dot(matriz_clave, indices) % 26  # 26 letras en el alfabeto
        matriz_resultado.extend(resultado)

    texto_cifrado = ''.join([chr(result + ord('A')) for result in matriz_resultado])

    return texto_cifrado

# Matriz clave (debe ser cuadrada y tener un determinante inversible)
clave = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])

# Mensaje a cifrar
mensaje = "HELLO"

# Cifrar el mensaje
texto_cifrado = cifrar_hill(clave, mensaje)
print("Texto cifrado:", texto_cifrado)