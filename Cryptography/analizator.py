import numpy as np
import os
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
lettersCount = {}
lettersArray = ["a","b","c","d","e","f",
                "g","h","i","j","k","l",
                "m","n","o","p","q","r",
                "s","t","u","v","w","x","y","z"]

def mostCommon(dictionary: dict) -> str:
    letter = ""
    for char in dictionary:
        if dictionary[char] > count:
            count = dictionary[char]
            letter = char
    return letter

def addSymbols():
    textMessage = ""
    with open(dir_path+'/output.txt', 'r') as text:
        textMessage = text.readlines()
    for line in textMessage:
        for letter in line:
            if letter.lower() in lettersArray:
                if letter.lower() in lettersCount:
                    lettersCount[letter.lower()] += 1
                else:
                    lettersCount[letter.lower()] = 1
    print(lettersCount)

def counter(dictionary):
    cnt = 0
    for letter in dictionary:
        cnt += int(dictionary[letter])
    return cnt

if __name__ == "__main__":
    addSymbols()
    cnt = counter(lettersCount)
    sortedLetterCount = dict(sorted(lettersCount.items(), key = lambda x:x[1], reverse = 1))
    print(sortedLetterCount)
    plt.bar(sortedLetterCount.keys(), np.divide(list(sortedLetterCount.values()), cnt))
    plt.ylim(0, 0.15)
    plt.show()