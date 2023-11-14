import random
from keyGenerator import Extended_Euclidean_algorithm, generateKey
from RSA import RSAencode, unpackBlocks, blockSize
from chinize import chinese_remainder
import math
import sympy

openKeyE = 3
p = 7
q = 5

def chinise_current(number: int):
    return number

def createCipherKeyD(p: int, q: int, e: int) -> dict({str:int}):
    N = p * q
    Yn = (p-1)*(q-1)
    cipherKeyD = Extended_Euclidean_algorithm(Yn, e)
    return dict({"e": 3, "d": cipherKeyD, "n": N})

def checkDivisors(dictionary: dict({int:int})) -> dict({int:int}):
    newDict = {}
    for item in dictionary.items():
        if math.gcd(item[0],item[1]) == 1:
            newDict += item
        else:
            g_c_d = math.gcd(item[0],item[1])
            newDict[item[0]/g_c_d] = item[1]/g_c_d
    return newDict

if __name__ == "__main__":
    openKeyE = 3

    p = 7
    q = 5
    key1 = createCipherKeyD(sympy.randprime(pow(2,512), pow(2,513)),sympy.randprime(pow(2,512), pow(2,513)),openKeyE)
    key2 = createCipherKeyD(sympy.randprime(pow(2,512), pow(2,513)),sympy.randprime(pow(2,512), pow(2,513)),openKeyE)
    key3 = createCipherKeyD(sympy.randprime(pow(2,512), pow(2,513)),sympy.randprime(pow(2,512), pow(2,513)),openKeyE)

    e1 = key1["e"]
    d1 = key1["d"]
    n1 = key1["n"]

    e2 = key2["e"]
    d2 = key2["d"]  
    n2 = key2["n"]

    e3 = key3["e"]
    d3 = key3["d"]
    n3 = key3["n"]

    message = random.randint(5,99)

    cipherText1 = pow(message,e1,n1)
    cipherText2 = pow(message,e2,n2)
    cipherText3 = pow(message,e3,n3)

    print("x = ",cipherText1,"(mod", n1,")")
    print("x = ",cipherText2,"(mod", n2,")")
    print("x = ",cipherText3,"(mod", n3,")")

    dictionary = [(n1, cipherText1),(n2, cipherText2),(n3, cipherText3)]
    print(dictionary)

    encodedMessage = chinese_remainder(dictionary)
    encodedMessage = chinise_current(message)
    print(encodedMessage)