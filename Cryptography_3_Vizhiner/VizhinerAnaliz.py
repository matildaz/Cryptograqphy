import numpy as np
import os

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
        summ += (item[1] * (item[1] - 1)) / (length * (length - 1))
    return summ

if __name__ == "__main__":
    
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

    print(len(text))
    summ1 = findIndexOfCoincidence(text)
    print("При длине ключа 1 коэфициент совпадения равен " , summ1)

    summ2_1 = findIndexOfCoincidence(text[:round(len(text)/2)])
    summ2_2 = findIndexOfCoincidence(text[round(len(text)/2):])
    summ2 = (summ2_1 + summ2_2)/2
    print("При длине ключа 2 коэфициент совпадения равен " , summ2)

    summ3_1 = findIndexOfCoincidence(text[:round(len(text)/3)])
    summ3_2 = findIndexOfCoincidence(text[round(len(text)/3):2*round(len(text)/3)])
    summ3_3 = findIndexOfCoincidence(text[2*round(len(text)/3):])
    summ3 = (summ3_1 + summ3_2 + summ3_3)/3
    print("При длине ключа 3 коэфициент совпадения равен " , summ3)

    summ4_1 = findIndexOfCoincidence(text[:round(len(text)/4)])
    summ4_2 = findIndexOfCoincidence(text[round(len(text)/4):round(len(text)/2)])
    summ4_3 = findIndexOfCoincidence(text[round(len(text)/2):3*round(len(text)/4)])
    summ4_4 = findIndexOfCoincidence(text[3*round(len(text)/4):])
    summ4 = (summ4_1 + summ4_2 + summ4_3 + summ4_4)/4
    print("При длине ключа 4 коэфициент совпадения равен " , summ4)

    summ5_1 = findIndexOfCoincidence(text[:round((len(text)-4)/5)])
    summ5_2 = findIndexOfCoincidence(text[round((len(text)-4)/5):2*round((len(text)-4)/5)])
    summ5_3 = findIndexOfCoincidence(text[2*round((len(text)-4)/5):3*round((len(text)-4)/5)])
    summ5_4 = findIndexOfCoincidence(text[3*round((len(text)-4)/5):4*(round((len(text))-4/5))])
    summ5_5 = findIndexOfCoincidence(text[4*round((len(text)-4)/5):])
    summ5 = (summ5_1 + summ5_2 + summ5_3 + summ5_4 + summ5_5)/5
    print("При длине ключа 5 коэфициент совпадения равен " , summ5)

    summ6_1 = findIndexOfCoincidence(text[:round(len(text)/6)])
    summ6_2 = findIndexOfCoincidence(text[round(len(text)/6):round(len(text)/3)])
    summ6_3 = findIndexOfCoincidence(text[round(len(text)/3):round(len(text)/2)])
    summ6_4 = findIndexOfCoincidence(text[round(len(text)/2):2*round(len(text)/3)])
    summ6_5 = findIndexOfCoincidence(text[2*round(len(text)/3):5*round(len(text)/6)])
    summ6_6 = findIndexOfCoincidence(text[5*round(len(text)/6):])
    summ6 = (summ6_1 + summ6_2 + summ6_3 + summ6_4 + summ6_5 + summ6_5)/6
    print("При длине ключа 6 коэфициент совпадения равен " , summ6)
    

    # globalDictionary = {}
    # with open(dir_path+'/output.txt', 'r') as text:
    #         textMessage = text.readlines()
    # for line in textMessage:
    #     localDict = phreses(line)
    #     globalDictionary = addToDictionary(globalDictionary,localDict)
    # commonPhrase, number = findCommonPhrase(globalDictionary)
    # print("Самая распространенная фраза -", commonPhrase)
    # print("Она встретилась ", number, " раз")

    # with open(dir_path+'/output.txt', 'r') as text:
    #         textMessage = text.readlines()
    # gapBefore = 0
    # globalArray = []
    # for line in textMessage:
    #     array, gapBefore = findKeyLength(commonPhrase, line, gapBefore)
    #     if array != []:
    #         globalArray.append(array)
    
    # print("Расстояния между распространенными фразами -", globalArray)

