import random
import math
from sqlalchemy import false, true


def generateKey(P: int, Q: int):
    N = P * Q
    Yn = (P-1)*(Q-1)
    arrayOfPossibleKeys = []
    lastKey = 0
    if Yn > 10000:
        lastKey = Yn - 500
    elif Yn> 1000: 
        lastKey = Yn - 750
    else:
        lastKey = round(Yn/2)
    for number in range(Yn, lastKey, -1):
        letterNumber = bin(number)
        letterNumber = letterNumber[2:]
        if checkTheNumber(letterNumber) and math.gcd(number,Yn) == 1:
            arrayOfPossibleKeys.append(number)

    if arrayOfPossibleKeys.count == 0:
        return 0, 0, 0

    randomKeyE, randomKeyD = choose_E_and_D(arrayOfPossibleKeys, Yn)

    return {"e":randomKeyE, "d":randomKeyD, "n":N}

def choose_E_and_D(arrayOfKeys, Yn: int):
    randomKeyE = random.randint(0, len(arrayOfKeys)-1)
    randomKeyE = arrayOfKeys[randomKeyE]

    randomKeyD = Extended_Euclidean_algorithm(Yn, randomKeyE)
    if randomKeyD <= 1:
        return choose_E_and_D(arrayOfKeys, Yn)
    return randomKeyE, randomKeyD

def checkTheNumber(strNumber: str) -> bool:
    dictionary01 = {0:0, 1:0}
    for item in strNumber:
        if item == "1":
            dictionary01[1] += 1
        else:
            dictionary01[0] += 1
    if abs(dictionary01[1] - dictionary01[0] > 5):
        return false
    else: 
        return true

def Extended_Euclidean_algorithm(a: int, b: int) -> int:
    if a <= 0 or b <= 0:
        return "Error"
    x2, x1 = 1, 0
    y2, y1 = 0, 1
    while b > 0:
        q = a // b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    y = y2
    return y

if __name__ == "__main__" :
    p = 7
    q = 11
    dictionary = generateKey(p,q)
    print("e = ", dictionary["e"])
    print("d = ", dictionary["d"])
    print("n = ", dictionary["n"])

    openText = 13
    print(openText)
    ciphertext = pow(openText,dictionary["e"],dictionary["n"])
    openText = pow(ciphertext,dictionary["d"],dictionary["n"])

    print(ciphertext)
    print(openText)