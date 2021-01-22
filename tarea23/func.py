import random
from enum import Enum

def __swapEnds(cards):
    aPos = cards.index('A')
    bPos = cards.index('B')
    indexes = [aPos, bPos]
    indexes.sort()
    firstEnd = cards[:indexes[0]] if indexes[0] > 0 else []
    middleChunk = cards[indexes[0]:indexes[1] + 1]
    lastEnd = cards[indexes[1] + 1:] if indexes[1] + 1 < len(cards) else []
    cards[:] = lastEnd + middleChunk + firstEnd

def __checkLastAndSwap(cards):
    lastCard = cards[-1]
    #if __isJoker(lastCard):
    if (lastCard =='A'):
        return cards
    if (lastCard =='B'):
        return cards
    firstEnd = cards[lastCard:cards.__len__() - 1]
    middleEnd = cards[:lastCard]
    lastEnd = [lastCard]
    cards[:] = firstEnd + middleEnd + lastEnd

def __charToNumber(char):
    charToNumberMap = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26,
    }
    return charToNumberMap[char]


def __numberToChar(number):
    chars = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    if number <= 26: index = number - 1
    else: index = number - 27
    return chars[index]

def __module26(number):
    # si suman más de 26, restamos 26 de resultado :1+1=2, 26+1=27, y 27-26=1, así que 26+1=1.
    return number if number <= 26 else number - 26

def __solitaire(cards):
    currentPos = cards.index('A')
    nextPos = currentPos + 1 if currentPos < len(cards) - 1 else 1
    del cards[currentPos]
    cards.insert(nextPos, 'A')
    currentPos = cards.index('B')
    nextPos = currentPos + 1 if currentPos < len(cards) - 1 else 1
    del cards[currentPos]
    cards.insert(nextPos, 'B')
    __swapEnds(cards)
    __checkLastAndSwap(cards)
    topCard = cards[0]
    if (topCard=='A'):
        return
    if (topCard=='B'):
        return
    outputCard = cards[topCard - 1]
    if (outputCard=='A'):
        return
    if (outputCard=='B'):
        return
    if outputCard <= 26: return outputCard
    else: return outputCard - 26

def __getSolitaireNumbers(msgLen, cards):
    solitaireNumbers = []
    while (msgLen > len(solitaireNumbers)):
        number = __solitaire(cards)
        if (number != None):
            solitaireNumbers = solitaireNumbers + [number]
    return solitaireNumbers


def __makeChunk(chars):
    return [''.join(chars[i:i + 5]) for i in range(0, len(chars), 5)]

def encrypt(msg):
    baraja = list(range(1, 53)) + ['A', 'B']
    random.shuffle(baraja)
    cardsCopy = list(baraja)
    msgChars = list(msg.upper().replace(" ", ""))
    solitaireNumbers = __getSolitaireNumbers(len(msgChars), baraja)
    coded = []
    for i in range(len(msgChars)):
        charNumber = __charToNumber(msgChars[i])
        addition = charNumber + solitaireNumbers[i]
        coded = coded + [__numberToChar(addition)]
    return [__makeChunk(''.join(coded)), cardsCopy]

def decrypt(chunks, cards):
    text = ''
    for chunk in chunks:
        text = text + chunk
    msg = text
    msgChars = list(msg.upper().replace(" ", ""))
    solitaireNumbers = __getSolitaireNumbers(len(msgChars), cards)
    decoded = []
    for i in range(len(msgChars)):
        charNumber = __charToNumber(msgChars[i])
        solNumber = solitaireNumbers[i]
        substraction = charNumber - solNumber if charNumber > solNumber else charNumber - solNumber + 26
        decoded = decoded + [__numberToChar(substraction)]
    return [''.join(decoded[i:i + 4]) for i in range(0, len(decoded), 4)]