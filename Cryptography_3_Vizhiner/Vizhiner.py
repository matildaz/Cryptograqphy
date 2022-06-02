import os
from appscript import k
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))

encodeDictionary = {'a':0,'b':1,'c':2,'d':3,'e':4,
                    'f':5,'g':6,'h':7,'i':8,'j':9,
                    'k':10,'l':11,'m':12,'n':13,'o':14,
                    'p':15,'q':16,'r':17,'s':18,'t':19,
                    'u':20,'v':21,'w':22,'x':23,'y':24,
                    'z':25}
decodeDictionary = {0:'a',1:'b',2:'c',3:'d',4:'e',
                    5:'f',6:'g',7:'h',8:'i',9:'j',
                    10:'k',11:'l',12:'m',13:'n',14:'o',
                    15:'p',16:'q',17:'r',18:'s',19:'t',
                    20:'u',21:'v',22:'w',23:'x',24:'y',
                    25:'z'}

def encodeVizhiner(openText: str, key: list, encodeDict: dict, decodeDict: dict) -> str:
    cipherText = ""
    for letter in openText:
        letter = letter.lower()
        if letter in encodeDict:
            numberToAdd = key[0]
            numberOfLetter = (encodeDict[letter] + numberToAdd) % len(decodeDict)
            cipherText += decodeDict[numberOfLetter]
            reusableKeyNumber = key.pop(0)
            key.append(reusableKeyNumber)
        else:
            continue
    return cipherText, key

def decodeVizhiner(cipherText: str, key: list, encodeDict: dict, decodeDict: dict) -> str:
    openText = ""
    for letter in cipherText:
        letter = letter.lower()
        if letter in encodeDict:
            numberToAdd = key[0]
            numberOfLetter = encodeDict[letter]
            if numberOfLetter < numberToAdd:
                numberOfLetter += len(decodeDict)
            numberOfLetter -= numberToAdd
            openText += decodeDict[numberOfLetter]
            reusableKeyNumber = key.pop(0)
            key.append(reusableKeyNumber)
        else:
            continue
    return openText, key

def makeKey(keyStr: str, encodeDict: dict):
    key = []
    for letter in keyStr:
        if letter in encodeDict:
            key.append(encodeDict[letter])
    return key

def main(state: str, key: str):
    newKey = makeKey(key, encodeDictionary)
    if state == "encode":
        with open(dir_path+'/read.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            encodeLine, newKey = encodeVizhiner(line,newKey,encodeDictionary,decodeDictionary)
            encodeLine += '\n'
            with open(dir_path+'/output.txt', 'a') as encodedText:
                encodedText.write(encodeLine)
    elif state == "decode":
        with open(dir_path+'/output.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            decodeLine, newKey = decodeVizhiner(line,newKey,encodeDictionary,decodeDictionary)
            decodeLine += '\n'
            with open(dir_path+'/outputDecode.txt', 'a') as decodedText:
                decodedText.write(decodeLine)

if __name__ == "__main__":
    # text, key = (encodeVizhiner("Hello World!", makeKey("apple", encodeDictionary), encodeDictionary, decodeDictionary))
    # print(text)
    # print(key)
    # text, key = decodeVizhiner(text,makeKey("apple", encodeDictionary), encodeDictionary, decodeDictionary)
    # print(text)
    # print(key)
    # for i in zip(text,"hello world!"):
    #     print(encodeDictionary[i[1]], "->", encodeDictionary[i[0]])
    key = "bye"
    state = "decode"
    main(state, key)
