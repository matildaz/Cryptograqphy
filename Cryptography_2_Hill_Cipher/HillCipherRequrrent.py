from curses.ascii import isdigit
import os
from matplotlib.pyplot import text
import numpy as np

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

def hillCipherEncode(openText: str, matrix1: np.array, matrix2: np.array, encodeDict: dict, decodeDict: dict, state: str):
    arrayOfLetters: np.array = []
    partOfArray: np.array = []
    cnt = 0
    for letter in openText:
        letter = letter.lower()
        if letter in encodeDict:
            partOfArray.append(encodeDict[letter])
            cnt += 1
        if cnt == 3:
            arrayOfLetters.append(partOfArray)
            partOfArray = []
            cnt = 0
    if len(partOfArray) < 3 and len(partOfArray) != 0:
        cnt = 0
        while len(partOfArray) != 3:
            cnt += 1
            partOfArray.append(0)
        arrayOfLetters.append(partOfArray)
        partOfArray = []
    matrix1, matrix2, arrayOfNumbers = encodeArray(arrayOfLetters, matrix1, matrix2, state)
    cipherText = ''
    for item in arrayOfNumbers:
        for number in item:
            if number in decodeDict:
                cipherText += decodeDict[number]
    if cnt != 0:
        while cnt != 0:
            cipherText = cipherText[:-1]
            cnt -= 1
    return matrix1, matrix2, cipherText

def encodeArray(array: np.array, matrix1: np.array, matrix2: np.array, state: str):
    for row in range(3):
        for number in range(3):
            matrix1[row][number] = round(matrix1[row][number], 2)
            matrix2[row][number] = round(matrix2[row][number], 2)
    newArray: np.array(np.array()) = []
    for item in array:
        newItem = np.array(item).dot(matrix1)
        newMatrix = matrix2.dot(matrix1)
        matrix1 = matrix2
        matrix2 = newMatrix
        matrix1 %= len(decodeDictionary)
        matrix2 %= len(decodeDictionary)
        for i in range(len(newItem)):
            newItem[i] = newItem[i] % 41
        newArray.append(newItem)
    if state == 'encode':
        return matrix1, matrix2, newArray
    else:
        return np.linalg.inv(matrix1), np.linalg.inv(matrix2), newArray

def hillCipherDecode(cipherText: str, matrix1: np.array, matrix2: np.array, encodeDict: dict, decodeDict: dict, state: str):
    arrayOfNumbers: np.array = []
    partOfArray: np.array = []
    cnt = 0
    for letter in cipherText:
        letter = letter.lower()
        if letter in encodeDict:
            cnt += 1
            partOfArray.append(encodeDict[letter])
        if len(partOfArray) == 3:
            arrayOfNumbers.append(partOfArray)
            partOfArray = []
            cnt = 0
    if len(partOfArray) < 3 and len(partOfArray) != 0:
        cnt = 0
        while len(partOfArray) != 3:
            partOfArray.append(0)
            cnt += 1
        arrayOfNumbers.append(partOfArray)
        partOfArray = []
    openText = ''
    matrix1, matrix2, arrayOfNumbers = encodeArray(arrayOfNumbers, np.linalg.inv(matrix1), np.linalg.inv(matrix2), state)
    for item in arrayOfNumbers:
        for number in item:
            if number in decodeDict:
                openText += decodeDict[number]
    if cnt != 0:
        while cnt != 0:
            cnt -= 1
            openText = openText[:-1]
    return matrix1, matrix2, openText

def readState(state: str, key1: np.array, key2: np.array):
    if np.linalg.det(key1) == 0 or np.linalg.det(key2) == 0:
        print("Invalid key")
        return
    textMessage = []
    if state == "encode":
        with open(dir_path+'/read.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            key1, key2, encodeLine = hillCipherEncode(line, key1, key2, encodeDictionary, decodeDictionary, state)
            encodeLine += '\n'
            with open(dir_path+'/output.txt', 'a') as encodedText:
                encodedText.write(encodeLine)
    elif state == "decode":
        with open(dir_path+'/output.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            key1, key2, decodeLine = hillCipherDecode(line, key1, key2, encodeDictionary, decodeDictionary, state)
            decodeLine += '\n'
            with open(dir_path+'/outputDecode.txt', 'a') as decodedText:
                decodedText.write(decodeLine)

if __name__ == "__main__":
    key1 = np.array([[2,5,7],[6,3,4],[5,-2,-3]], dtype = float)
    key2 = np.array([[1,0,0],[0,1,0],[0,0,1]], dtype = float)
    state = 'decode'
    readState(state, key1, key2)

    # text = "hello world"
    # key3, key4, text = hillCipherEncode(text,key1,key2,encodeDictionary,decodeDictionary)
    # print(key3, "\n")
    # print(key4, "\n")
    # print(text, "\n")

    # key3, key4, text = hillCipherDecode(text,key1,key2,encodeDictionary,decodeDictionary)
    # print(key3, "\n")
    # print(key4, "\n")
    # print(text, "\n")