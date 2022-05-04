from curses.ascii import isdigit
import os
import numpy as np
from pandas import array

dir_path = os.path.dirname(os.path.realpath(__file__))

encodeDictionary = {'a':0,'b':1,'c':2,'d':3,'e':4,
                    'f':5,'g':6,'h':7,'i':8,'j':9,
                    'k':10,'l':11,'m':12,'n':13,'o':14,
                    'p':15,'q':16,'r':17,'s':18,'t':19,
                    'u':20,'v':21,'w':22,'x':23,'y':24,
                    'z':25,'0':26,'1':27,'2':28,'3':29,
                    '4':30,'5':31,'6':32,'7':33,'8':34,
                    '9':35,' ':36,'.':37,',':38,'?':39,'!':40}
decodeDictionary = {0:'a',1:'b',2:'c',3:'d',4:'e',
                    5:'f',6:'g',7:'h',8:'i',9:'j',
                    10:'k',11:'l',12:'m',13:'n',14:'o',
                    15:'p',16:'q',17:'r',18:'s',19:'t',
                    20:'u',21:'v',22:'w',23:'x',24:'y',
                    25:'z', 26:'0',27:'1',28:'2',29:'3',
                    30:'4',31:'5',32:'6',33:'7',34:'8',
                    35:'9',36:' ',37:'.',38:',',39:'?',40:'!'}

def encodeVizhiner(openText: str, key: array, encodeDict: dict, decodeDict: dict) -> str:
    newKeyStr = ""
    cipherText = ""
    cnt = 0
    for index,letter in enumerate(openText):
        if len(newKeyStr) >= len(key):
            key = makeKey(newKeyStr, encodeDict)
            newKeyStr = ""
        letter = letter.lower()
        index = (index - cnt) % len(key)
        numberToAdd = key[index]
        if letter in encodeDict:
            newKeyStr += letter
            numberOfLetter = (encodeDict[letter] + numberToAdd) % len(decodeDict)
            cipherText += decodeDict[numberOfLetter]
        else:
            cnt += 1
            continue
    return cipherText

def decodeVizhiner(cipherText: str, key: array, encodeDict: dict, decodeDict: dict) -> str:
    openText = ""
    newKeyStr = ""
    for index,letter in enumerate(cipherText):
        if len(newKeyStr) >= len(key):
            key = makeKey(newKeyStr,encodeDict)
            newKeyStr = ""
        letter = letter.lower()
        index = index % len(key)
        numberToAdd = key[index]
        if letter in encodeDict:
            numberOfLetter = encodeDict[letter]
            numberToAdd = key[index]
            if numberOfLetter < numberToAdd:
                numberOfLetter += len(decodeDict)
            numberOfLetter -= numberToAdd
            openText += decodeDict[numberOfLetter]
            newKeyStr += decodeDict[numberOfLetter]
        else:
            continue
    return openText

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
            encodeLine = encodeVizhiner(line,newKey,encodeDictionary,decodeDictionary)
            encodeLine += '\n'
            with open(dir_path+'/output.txt', 'a') as encodedText:
                encodedText.write(encodeLine)
    elif state == "decode":
        with open(dir_path+'/output.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            decodeLine = decodeVizhiner(line,newKey,encodeDictionary,decodeDictionary)
            decodeLine += '\n'
            with open(dir_path+'/outputDecode.txt', 'a') as decodedText:
                decodedText.write(decodeLine)

if __name__ == "__main__":
    key = "abc"
    state = "decode"
    main(state, key)
