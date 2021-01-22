def convertToBinary(num):
    binary = ''
    while num // 2 != 0:
        binary = str(num % 2) + binary
        num = num // 2
    return str(num) + binary


numero = int(input("Introduce un numero: "))
print("El numero en binario es : ", convertToBinary(numero))