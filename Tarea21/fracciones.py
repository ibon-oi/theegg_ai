#funciona tanto con números con . o , (0.5 o 0,5)
print ("Introduce un número entre 0,0001 y 0,9999")
num = (input())
# obtenemos un string para poder cambiar la , por .
num = num.replace(",",".")
# conertimos el string eln float para poder interactuar
num = float(num)
print(f"El número introducido es: {num}")

den = 10000
num = int(num * 10000)
i = num
count = 0
while i > 1:
    # Si el numerador y el denominador son divisibles entre i, se asignan nuevos denominador y numerador
    if num % i == 0 and den % i == 0:
        num = num / i
        den = den / i
    i = i - 1
    count = count + 1

print("Resultado: %d/%d. Iteraciones realizadas: %d" % (num, den, count))
