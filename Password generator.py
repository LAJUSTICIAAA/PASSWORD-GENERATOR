import random
import string

def generar_contraseña(longitud=12):
    # En este parte del código se definen las variables que estan permitidas 
    #En este caso como el usuario solo va a dar un clic yo selecciono las variables 
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    especiales = string.punctuation

    # Combino todos los carácteres 
    todos_los_caracteres = mayusculas + minusculas + numeros + especiales

    # Generar una contraseña que contenga al menos un carácter de cada tipo
    contraseña = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiales),
    ]

    # Completar la contraseña hasta la longitud deseada
    contraseña += random.choices(todos_los_caracteres, k=longitud - 4)

    # Mezclar los caracteres de la contraseña para evitar patrones predecibles
    random.shuffle(contraseña)

    # Convertir la lista en una cadena
    return ''.join(contraseña)

# Generar una contraseña de longitud 12
print(generar_contraseña())
