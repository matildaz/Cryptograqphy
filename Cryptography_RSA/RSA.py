import sympy
from keyGenerator import generateKey
import binascii
import base64
import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def RSAencode(openKey: int, n: int, openText: str):
    byteStr = bytes(openText, 'utf-8')
    blocks = unpackBlocks(byteStr, blockSize(n))
    blocks_upd = []
    for item in blocks:
        blocks_upd.append(pow(item,openKey,n))
    data = packBlocks(blocks_upd, blockSize(n)+1) 
    baseData = binascii.b2a_base64(data)
    bytBaseData = base64.b64decode(baseData)
    bytBaseData1 = base64.b64encode(bytBaseData)
    encodedString = str(bytBaseData1, 'utf-8',"ignore")
    return encodedString

def RSAdecode(closed: int, n: int, cipherText: str):
    byteStr = bytes(cipherText, 'utf-8')
    newData = binascii.a2b_base64(byteStr)
    blocks = unpackBlocks(newData, blockSize(n)+1)
    blocks_upd = []
    for item in blocks:
        blocks_upd.append(pow(item,closed,n))
    data = packBlocks(blocks_upd, blockSize(n)) 
    decodedString = data.decode('utf-8',"ignore")
    return decodedString

def blockSize(n: int):
    byteN = bin(n)
    size = len(byteN) - 2
    return size - 1

def unpackBlocks(data: bytes, bs: int):
    blocks = []
    block = 0
    c = 0
    for b in data:
        block |= (b & ((2 ** (bs - c)) - 1)) << c
        added = min(bs - c, 8)
        c += added
        if c >= bs:
            blocks.append(block)
            if added < 8:
                block = b >> added
                c = 8 - added
            else:
                block = 0
                c = 0
    if c:
        blocks.append(block)
    return blocks

def packBlocks(blocks: list, bs: int):
    data = b''
    rem = 0
    c = 0
    for blk in blocks:
        k = bs
        while k:
            b = 0
            if c:
                b |= rem
            if k >= 8 - c:
                b |= (blk & ((2 ** (8 - c)) - 1)) << c
                data += bytes([b])
                blk >>= 8 - c
                k -= 8 - c
                c = 0
            else:
                rem = blk
                c = k
                k = 0
    if c:
        data += bytes([rem])
    return data

def RSAmain(state: str, key: dict({str: int})) -> str: #key = [ e , d , n ]
    e = key["e"]
    d = key["d"]
    n = key["n"]
    if state == "encode":
        with open(dir_path+'/read.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            encodeLine = RSAencode(e,n,line)
            encodeLine += '\n'
            with open(dir_path+'/output.txt', 'a') as encodedText:
                encodedText.write(encodeLine)
    elif state == "decode":
        with open(dir_path+'/output.txt', 'r') as text:
            textMessage = text.readlines()
        for line in textMessage:
            decodeLine = RSAdecode(d,n,line)
            decodeLine += '\n'
            with open(dir_path+'/outputDecode.txt', 'a') as decodedText:
                decodedText.write(decodeLine)
    return ""

if __name__ == "__main__":
    p = sympy.randprime(pow(2,100), pow(2,101))
    q = sympy.randprime(pow(2,100), pow(2,101))
    dictionary = generateKey(p,q)
    e = dictionary["e"]
    d = dictionary["d"]
    n = dictionary["n"]
    print("e = ", dictionary["e"])
    print("d = ", dictionary["d"])
    print("n = ", dictionary["n"])

    # RSAmain("encode", dictionary)
    # RSAmain("decode", dictionary)