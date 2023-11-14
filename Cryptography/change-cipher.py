import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

keyChangeArray = {"g":"e", "m":"t", "c":"a", "x":"s",
                  "t":"r", "u":"o", "j":"i", "r":"k",
                  "v":"l", "a":"h", "i":"c", "k":"f",
                  "z":"g", "s":"m", "y":"u", "h":"d",
                  "n":"y", "f":"p", "q":"q", "o":"b",
                  "p":"w", "l":"v", "w":"x", "b":"j",
                  "e":"n", "d":"z"}

keyChangeArray_1 = {"c":"a", "e":"n", "v":"l", "n":"y", "x":"s", "j":"i", "o":"b", "g":"e",
                    "h":"d", "u":"o", "m":"t", "a":"h"}

def findKeyByValue(char: str, dictionary: dict) -> str:
    char = char.lower()
    if len(char) != 1:
        return ""
    for word in dictionary:
        if dictionary[word] == char:
            return word
    return char

def changeCiphreEncode(openText: str, key: dict) -> str:
    encodedText = ""
    for letter in openText:
        if (letter.isalpha()) and (letter.lower() in key):
            encodedText += key[letter.lower()]
        else:
            encodedText += letter
    return encodedText

def changeCiphreDecode(encodedText: str, key: dict) -> str:
    decodedText = ""
    for letter in encodedText:
        if letter.isalpha():
            decodedLetter = findKeyByValue(letter, key)
            if decodedLetter != "":
                decodedText += decodedLetter
        else:
            decodedText += letter
    return decodedText

def readlines(state: str):
    textMessage = []
    if state == "encode":
        with open(dir_path+'/read.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            encodeLine = changeCiphreEncode(line,keyChangeArray)
            with open(dir_path+'/output.txt', 'a') as encodedText:
                encodedText.write(encodeLine)
    elif state == "decode":
        with open(dir_path+'/output.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            decodedLine = changeCiphreDecode(line,keyChangeArray)
            with open(dir_path+'/outputDecode.txt', 'a') as decodedText:
                decodedText.write(decodedLine)

if __name__ == "__main__":
    readlines("encode")
