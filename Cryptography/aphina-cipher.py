import numpy as np
import os
import random
import sympy
from sqlalchemy import false, true

dir_path = os.path.dirname(os.path.realpath(__file__))

encodeDictionary = {'a':0,'b':1,'c':2,'d':3,'e':4,
                    'f':5,'g':6,'h':7,'i':8,'j':9,
                    'k':10,'l':11,'m':12,'n':13,'o':14,
                    'p':15,'q':16,'r':17,'s':18,'t':19,
                    'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
decodeDictionary = {0:'a',1:'b',2:'c',3:'d',4:'e',
                    5:'f',6:'g',7:'h',8:'i',9:'j',
                    10:'k',11:'l',12:'m',13:'n',14:'o',
                    15:'p',16:'q',17:'r',18:'s',19:'t',
                    20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

def getRandomKey() -> tuple:
    key = (1,1)
    alpha = random.randint(0,len(encodeDictionary)-1)
    beta = random.randint(0,len(encodeDictionary))
    key = (alpha,beta)
    return key

def simpleNumbers(number: int) -> list:
    divisors = []
    for i in range(2,1000):
        if sympy.isprime(i) and number % i == 0:
            divisors.append(i)
            number = number/i
            if number == 1:
                break
            else:
                divisors += simpleNumbers(number)
                break
        else:
            continue
    return divisors

def areSimple(divisorsOfFirstNumber: list, divdisorsOfSecondNumber: list) -> bool:
    for divisor in divisorsOfFirstNumber:
        if divisor in divdisorsOfSecondNumber:
            return false
    return true
    
def afinaCipherEncode(openText: str, encodeDict: dict, decodeDict: dict, key: tuple) -> str:
    cipherText = ""
    for letter in openText:
        letter = letter.lower()
        if letter.isalpha() and letter in encodeDict:
            letterNumber = encodeDict[letter]
            letterNumber = (letterNumber * key[0] + key[1]) % len(encodeDict)
            cipherText += decodeDict[letterNumber]
        else:
            cipherText += letter
    return cipherText

def afinaCipherDecode(cipherText: str, encodeDict: dict, decodeDict: dict, key: tuple) -> str:
    openText = ""
    euclid = Extended_Euclidean_algorithm(key[0],len(encodeDict))
    dictionaryLen = len(encodeDict)
    for letter in cipherText:
        letter = letter.lower()
        if letter.isalpha() and letter in encodeDict:
            letterNumber = encodeDict[letter] + dictionaryLen
            letterNumber = ((letterNumber - key[1]) * euclid) % dictionaryLen
            openText += decodeDict[letterNumber]
        else:
            openText += letter
    return openText

def readlines(state: str, key: tuple):
    if areSimple(simpleNumbers(key[0]),simpleNumbers(len(encodeDictionary))) is false:
        print("Invalid key")
        return
    textMessage = []
    if state == "encode":
        with open(dir_path+'/read.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            encodeLine = afinaCipherEncode(line,encodeDictionary,decodeDictionary,key)
            with open(dir_path+'/output.txt', 'a') as encodedText:
                encodedText.write(encodeLine)
    elif state == "decode":
        with open(dir_path+'/output.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            decodeLine = afinaCipherDecode(line,encodeDictionary,decodeDictionary,key)
            with open(dir_path+'/outputDecode.txt', 'a') as decodedText:
                decodedText.write(decodeLine)

def Extended_Euclidean_algorithm(a: int, b: int) -> int:
    if a <= 0 or b <= 0:
        return "Error"
    x2, x1 = 1, 0
    while b > 0:
        q = a // b
        r = a - q * b
        x = x2 - q * x1
        a = b
        b = r
        x2 = x1
        x1 = x
    x = x2
    if x < 0:
        x = x + b
    return x

if __name__ == "__main__":
    readlines("encode", (5,13))

