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

    # Hago que el resultado tenga al menos uno de cada uno 
    contraseña = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(especiales),
    ]

    # Completo la contraseña hasta la longitud deseada
    contraseña += random.choices(todos_los_caracteres, k=longitud - 4)

    # Mezclo los caracteres para evitar claves repetidas
    random.shuffle(contraseña)

    # Convierto la lista en una cadena 
    return ''.join(contraseña)

# EN mi caso hago que la contraseña tenga una  de longitud 12
print(generar_contraseña())
