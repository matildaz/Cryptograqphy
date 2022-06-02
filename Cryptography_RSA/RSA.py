from keyGenerator import generateKey
import binascii
def RSAencode(openKey: int, n: int, openText: str):
    cipherText = ""
    binaryCiphertext = ""
    binary_str = ''.join(format(ord(i), '08b') for i in openText)
    strOpenKey = bin(openKey)
    strOpenKey = strOpenKey[2:]
    adder = ''.join('0' for i in range(len(strOpenKey)-len(binary_str)%len(strOpenKey)))
    binary_str = adder + binary_str
    while len(binary_str) != 0:
        strToEncode = binary_str[-len(strOpenKey):]
        numberToEncode = int(strToEncode, 2)
        numberToEncode = pow(numberToEncode, openKey, n)
        strToEncode = bin(numberToEncode)
        strToEncode = strToEncode[2:]
        binaryCiphertext += strToEncode
        binary_str = binary_str[:-len(strOpenKey)]

    if len(binaryCiphertext) % 8 != 0:
        adder = ""
        adder = ''.join('0' for i in range(8-len(binaryCiphertext)%8))
        binaryCiphertext = adder + binaryCiphertext

    data_str = binascii.unhexlify('%x' % int(binaryCiphertext,2))

    print(data_str)
    return data_str

def RSAdecode(cipherKey: int, n: int, cipherText: str):
    binary_str = ''.join(format(ord(i), '08b') for i in cipherText)
    return 0

if __name__ == "__main__":
    p = 8527
    q = 7829
    # p = 181
    # q = 107
    e, d, n = generateKey(p,q)
    print("e = ", e)
    print("d = ", d)
    print("n = ", n)

    text = RSAencode(e,n,"Hello world!")
    print(text)
    text = RSAencode(d,n,text)
    print(text)