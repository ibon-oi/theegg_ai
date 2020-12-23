from cow import Cow
from entero import entero
from prettytable import PrettyTable
from MaxProduction import MaxProduction

x = PrettyTable()
y = PrettyTable()

if __name__ == '__main__':
    cows = []
    cows1 = []
    maxWeight = 0
    maxProduction = 0
    weightToCarry = 0
    totalV = entero('Número de vacas que hay en Tolosa: \n')
    totalWeight = entero("Peso total que el camión puede llevar: \n")
    for i in range(1, totalV+1):
        weight = entero("Introducir peso %d:\n" % i)
        milk = entero("Introducir cantidad de leche %d:\n" % i)
        nCow = Cow(i, weight, milk)
        cowsInMarket.append(nCow)

    [maxProduction, weightToCarry, cows1] = maxProduction(cows, maxWeight, 0, 0, 0, [])
    print("MAX: %d" % maxProduction)

    x.field_names = ["Número", "Peso", "Cantidad leche"]
    y.field_names = ["Número", "Peso", "Cantidad leche"]

    print("Produccion maxima de leche: %dl" % maxProduction)
    print("Peso a llevar: %dkg ; Peso maximo: %dkg" % (weightToCarry, maxWeight))

    for co in cows1:
        x.add_row([co.id, co.weight, co.milk])
    for co in cowsInMarket:
        y.add_row([co.id, co.weight, co.milk])

    print(x)
    print("\n******************************************\n")
    print(y)

