# Función para pedir un número positvo
def entero(texto):
    while True:
        numero = input(texto)
        if ( str(numero).isnumeric() and int(numero) > 0 ):
            # Si el valor obtenido es numerico y es mayor que 0, devolvemos el número
             return int(numero)
        else:
            # en caso contrario, volvemos a pedir un número positivo
             print('Escribe un número positivo')

