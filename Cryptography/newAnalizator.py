
if __name__ == "__main__":
    arrayOfKeys1 = []
    for alpha in range(0,26):
        for beta in range(0,27):
            if ((4*alpha)+beta)%26 == 7:
                arrayOfKeys1.append((alpha,beta))

    arrayOfKeys2 = []
    for alpha in range(0,26):
        for beta in range(0,27):
            if ((19*alpha)+beta)%26 == 4:
                arrayOfKeys2.append((alpha,beta))

    arrayOfKeys3 = []
    for key in arrayOfKeys1:
        if key in arrayOfKeys2:
            arrayOfKeys3.append(key)
    print()
    print(arrayOfKeys3)
    print()