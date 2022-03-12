import numpy as np
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

keyChangeArray = {"a":"b","b":"c","c":"d","d":"e",
                "e":"f","f":"g","g":"h","h":"i",
                "i":"j","j":"k","k":"l","l":"m",
                "m":"n","n":"o","o":"p","p":"q",
                "q":"r","r":"s","s":"t","t":"u",
                "u":"v","v":"w","w":"x","x":"y",
                "y":"z","z":"a"}

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
    readlines("decode")
