import random
import string

def generar_contraseña(longitud, palabra, incluir_simbolos, incluir_numeros, caracteres_extra):
    caracteres = string.ascii_letters

    if incluir_numeros:
        caracteres += string.digits
    
    if incluir_simbolos:
        caracteres += string.punctuation
    
    # Mezclo la palabra con los carácteres aleatorios
    mezcla = ''.join(random.choice(caracteres) for _ in range(longitud - len(palabra) - len(caracteres_extra)))
    
    # Me aseguro que los carácteres extra esten incluidos
    contraseña = list(palabra + mezcla + caracteres_extra)
    random.shuffle(contraseña)
    
    return ''.join(contraseña)

# Preguntas clave para el usuario
print("Bienvenido al generador de contraseñas de Justin.")
longitud = int(input("¿De cuántos caracteres quieres tu contraseña? (mínimo 8): "))
palabra = input("Ingresa una palabra o caracteres que quieras incluir en la contraseña: ")

while len(palabra) > longitud:
    print("La palabra es más larga que la longitud de la contraseña. Por favor, ingresa una palabra más corta.")
    palabra = input("Ingresa una palabra o caracteres que quieras incluir en la contraseña: ")

incluir_simbolos = input("¿Quieres incluir símbolos? (Sí/No): ").strip().lower() == 'sí'
incluir_numeros = input("¿Quieres incluir números? (Sí/No): ").strip().lower() == 'sí'
caracteres_extra = input("Ingresa caracteres adicionales que quieras incluir en la contraseña (ejemplo: @-_): ")

# Generación de contraseña
while len(palabra) + len(caracteres_extra) > longitud:
    print(f"La palabra y los caracteres adicionales ({len(palabra) + len(caracteres_extra)}) superan la longitud deseada.")
    longitud = int(input("Ingresa una longitud mayor para la contraseña: "))

contraseña = generar_contraseña(longitud, palabra, incluir_simbolos, incluir_numeros, caracteres_extra)
print(f"Tu nueva contraseña es: {contraseña}")
