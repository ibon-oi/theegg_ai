from max import max

def maxProduction(market, maxWeight, i, actualMilk, actualWeight, cows):
    if(i < len(market)):
        # hasta comprobar la última vaca
        aCow = market[index]
        if(actualWeight + aCow.weight <= maxWeight):
            #insertamos la vaca, dependiendo de la cantidad de la leche
            return max(maxProduction(market, maxWeight, index + 1, actualMilk + aCow.milk,
                    actualWeight + aCow.weight, cows + [aCow]),
                maxProduction(market, maxWeight, i + 1, actualMilk, actualWeight, cows))
        else:
            #no insertamos la vaca actual
            return maxProduction(market, maxWeight, i + 1, actualMilk, actualWeight, cows)
        #devolvemos el resultado
    return [actualMilk, actualWeight, cows]