def addToDictionary(dictionary1: dict({str: int}), dictionary2: dict({str: int})):
    for item in dictionary2.items():
        if item[0] in dictionary1:
            dictionary1[item[0]] += item[1]
        else:
            dictionary1[item[0]] = item[1]
    return dictionary1

dictionary1 = {"abc": 2, "bcd": 3}

dictionary2 = {"abc": 2, "bcd": 3, "cde": 5}

dictionary3 = addToDictionary(dictionary1,dictionary2)

print(dictionary3)