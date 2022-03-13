import numpy as np
import os
import random
from sqlalchemy import false, true
import sympy

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

def Extended_Euclidean_algorithm(firstNumber: int, SecondNumber: int) -> int:
    if firstNumber <= 0 or SecondNumber <= 0:
        return "Error"
    x2, x1 = 1, 0
    while SecondNumber > 0:
        q = firstNumber // SecondNumber
        r = firstNumber - q * SecondNumber
        x = x2 - q * x1
        firstNumber = SecondNumber
        SecondNumber = r
        x2 = x1
        x1 = x
    x = x2
    return x

def aphinaRecurrentEncode(openText: str, encodeDict: dict, decodeDict: dict, key1: tuple, key2: tuple):
    cipherText = ""
    for letter in openText:
        letter = letter.lower()
        if letter.isalpha() and letter in encodeDict:
            letterNumber = encodeDict[letter]
            letterNumber = (letterNumber * key1[0] + key1[1]) % len(encodeDict)
            cipherText += decodeDict[letterNumber]
            alpha = (key1[0] * key2[0]) % len(encodeDict)
            beta = (key1[1] + key2[1]) % len(encodeDict)
            newKey = (alpha,beta)
            key1 = key2
            key2 = newKey
        else:
            cipherText += letter
    return cipherText, key1, key2

def aphinaRecurrentDecode(cipherText: str, encodeDict: dict, decodeDict: dict, key1: tuple, key2: tuple):
    openText = ""
    for letter in cipherText:
        letter = letter.lower()
        if letter.isalpha() and letter in encodeDict:
            letterNumber = encodeDict[letter]
            antiKey = Extended_Euclidean_algorithm(key1[0], len(encodeDict))
            letterNumber = ((letterNumber - key1[1]) * antiKey) % len(encodeDict)
            openText += decodeDict[letterNumber]
            alpha = (key1[0] * key2[0]) % len(encodeDict)
            beta = (key1[1] + key2[1]) % len(encodeDict)
            newKey = (alpha,beta)
            key1 = key2
            key2 = newKey
        else: 
            openText += letter
    return openText, key1, key2

def readlines(state: str, key1: tuple, key2: tuple):
    if areSimple(simpleNumbers(key1[0]),simpleNumbers(len(encodeDictionary))) is false:
        print("Invalid key1")
        return
    if areSimple(simpleNumbers(key2[0]),simpleNumbers(len(encodeDictionary))) is false:
        print("Invalid key2")
        return
    textMessage = []
    if state == "encode":
        with open(dir_path+'/read.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            encodeLine, key1, key2 = aphinaRecurrentEncode(line, encodeDictionary, decodeDictionary, key1, key2)
            with open(dir_path+'/output.txt', 'a') as encodedText:
                encodedText.write(encodeLine)
    elif state == "decode":
        with open(dir_path+'/output.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            decodedLine, key1, key2 = aphinaRecurrentDecode(line, encodeDictionary, decodeDictionary, key1, key2)
            with open(dir_path+'/outputDecode.txt', 'a') as decodedText:
                decodedText.write(decodedLine)


if __name__ == "__main__":
    readlines("decode",(5,13),(7,13))