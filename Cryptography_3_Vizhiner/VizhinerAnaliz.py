import numpy as np
import os
import math

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

def phreses(line: str):
    dictionary = {}
    for position, _ in enumerate(line):
        if position > len(line) - 2:
            break
        try:
            if line[position+3] in encodeDictionary:
                phrase = line[position:position+3]
                if phrase in dictionary:
                    dictionary[phrase] += 1
                else:
                    dictionary[phrase] = 1
        except:
            pass
    return dictionary

def addToDictionary(dictionary1: dict({str: int}), dictionary2: dict({str: int})):
    for item in dictionary2.items():
        if item[0] in dictionary1:
            dictionary1[item[0]] += item[1]
        else:
            dictionary1[item[0]] = item[1]
    return dictionary1

def findCommonPhrase(dictionary: dict({str: int})):
    count = 0
    phrase = ""
    for item in dictionary.items():
        if item[1] > count:
            count = item[1]
            phrase = item[0]
    return phrase, count

def countLetters(line: str):
    dictionary: dict({str: int}) = {}
    for letter in line:
        if letter in encodeDictionary:
            if letter in dictionary:
                dictionary[letter] += 1
            else:
                dictionary[letter] = 1
    return dictionary

def findIndexOfCoincidence(textLine: str):
    summ = 0
    length = len(textLine)
    dictionary = countLetters(textLine)
    for item in dictionary.items():
        summ += (item[1]*(item[1]-1))/(length*(length-1))
    return summ

if __name__ == "__main__":
    
    # Вычисление индекса совпадения 
    globalDictionary = {}
    text: str = ""
    count = 0
    with open(dir_path+'/output.txt', 'r') as newText:
        textMessage = newText.readlines()
        for line in textMessage:
            text += line
            localDict = countLetters(line)
            globalDictionary = addToDictionary(globalDictionary,localDict)
            count += len(line)

    for j in range(1,11):
        stride = math.ceil(len(text) / j)
        parts = [text[i:i + stride] for i in range(0, len(text), stride)]
        sum_0 = 0
        for item in parts:
            sum_0 += findIndexOfCoincidence(item)
        print("При длине ключа",j," коэфициент совпадения равен" , sum_0/j)
    

    # Вычисление самого распространенного выражения из 3 символов
    globalDictionary = {}
    with open(dir_path+'/output.txt', 'r') as text_1:
            textMessage = text_1.readlines()
    for line in textMessage:
        localDict = phreses(line)
        globalDictionary = addToDictionary(globalDictionary,localDict)
    commonPhrase, number = findCommonPhrase(globalDictionary)
    print("Самая распространенная фраза -", commonPhrase)
    print("Она встретилась ", number, " раз")


    line1 = ""
    line2 = ""
    line3 = ""
    
    for index,letter in enumerate(text):
        if index % 3 == 0:
            line1 += letter
        elif index % 3 == 1:
            line2 += letter
        else:
            line3 += letter

    dictinatyLine1 = countLetters(line1)
    dictinatyLine1 = dict(sorted(dictinatyLine1.items(), key=lambda x: x[1], reverse=True))
    dictinatyLine2 = countLetters(line2)
    dictinatyLine2 = dict(sorted(dictinatyLine2.items(), key=lambda x: x[1], reverse=True))
    dictinatyLine3 = countLetters(line3)
    dictinatyLine3 = dict(sorted(dictinatyLine3.items(), key=lambda x: x[1], reverse=True))

    print(dictinatyLine1)
    print(dictinatyLine2)
    print(dictinatyLine3)

