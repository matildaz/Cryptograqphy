from curses.ascii import isdigit
import os
import numpy as np
from sympy import primefactors

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

def hillCipherEncode(openText: str, matrix: np.array, encodeDict: dict, decodeDict: dict) -> str:
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
    arrayOfNumbers = encodeArray(arrayOfLetters,matrix)
    cipherText = ''
    for item in arrayOfNumbers:
        for number in item:
            if number in decodeDict:
                cipherText += decodeDict[number]
                print(number)
    if cnt != 0:
        while cnt != 0:
            cipherText = cipherText[:-1]
            cnt -= 1
    return cipherText

def encodeArray(array: np.array, matrix: np.array) -> np.array :
    for row in range(3):
        for number in range(3):
            matrix[row][number] = round(matrix[row][number], 2)
    newArray: np.array(np.array()) = []
    for item in array:
        newItem = np.array(item).dot(matrix)
        for i in range(len(newItem)):
            newItem[i] = newItem[i] % 41
        newArray.append(newItem)
    return newArray

def hillCipherDecode(cipherText: str, matrix: np.array, encodeDict: dict, decodeDict: dict) -> str:
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
    invertMatrix = np.linalg.inv(matrix) * np.linalg.det(matrix)
    invertDet = Extended_Euclidean_algorithm(round(np.linalg.det(matrix)),len(decodeDict))
    invertMatrix *= invertDet
    invertMatrix %= len(decodeDict)
    arrayOfNumbers = encodeArray(arrayOfNumbers, invertMatrix)
    for item in arrayOfNumbers:
        for number in item:
            if number in decodeDict:
                openText += decodeDict[number]
    if cnt != 0:
        while cnt != 0:
            cnt -= 1
            openText = openText[:-1]
    return openText


def readState(state: str, key: np.array):
    if np.linalg.det(key) == 0:
        print("Invalid key")
        return
    textMessage = []
    if state == "encode":
        with open(dir_path+'/read.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            encodeLine = hillCipherEncode(line, key, encodeDictionary, decodeDictionary)
            encodeLine += '\n'
            with open(dir_path+'/output.txt', 'a') as encodedText:
                encodedText.write(encodeLine)
    elif state == "decode":
        with open(dir_path+'/output.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            decodeLine = hillCipherDecode(line, key, encodeDictionary, decodeDictionary)
            decodeLine += '\n'
            with open(dir_path+'/outputDecode.txt', 'a') as decodedText:
                decodedText.write(decodeLine)

def analizator(state: str, openText: str):


    matrix = np.array([
        [2,5,7],
        [6,3,4],
        [5,-2,-3]],
         dtype = float)
    
    
    if state == "encode":
        print()
        print(hillCipherEncode(openText, matrix, encodeDictionary, decodeDictionary), "\n")

if __name__ == "__main__":
    # openText = "aaa"
    # state = "decode"
    # matrix = np.array([
    #     [2,23,7],
    #     [6,7,4],
    #     [5,-2,-3]],
    #      dtype = float)
    # print(np.linalg.det(matrix))
    # readState(state, matrix)
    # analizator(state, openText)
    # print(encodeDictionary['n'])
    # print(encodeDictionary['g'])
    # print(encodeDictionary['i'])
    
    
    
    
    matrix = np.array([[2,5,7],[6,3,4],[5,-10,-3]], dtype = float)
    print(np.linalg.det(matrix)%41)
    # print(round(np.linalg.det(matrix)))
    # state = 'decode'
    # readState(state,matrix)
    # print(matrix.dot(np.linalg.inv(matrix)))
    text = hillCipherEncode('Hello world', matrix, encodeDictionary, decodeDictionary)
    encode_matrix = np.array([[7,4,11],[11,14,36],[22,14,17]], dtype=float)
    new_matrix = np.array(encode_matrix).dot(matrix)
    print(new_matrix % 41)
    # print((np.linalg.inv(matrix) * np.linalg.det(matrix) * Extended_Euclidean_algorithm(-1,41) )% 41)
    # key1 = np.array([[11,25,32],[40,25,25],[8,38,36]])
    # key2 = np.array([[1,40,1],[3,0,7],[27,12,24]])
    # print(np.array(key2).dot(key1) % 41)
    # print(text)
    # print()
    # text = hillCipherDecode('lz6!zzi  !x', matrix, encodeDictionary, decodeDictionary)
    # print(text)