from prettytable import PrettyTable


def staples(a: int) -> str:
    if a >= 0:
        return str(a)
    else:
        return '(' + str(a) + ')'


def Chinese_remainder_theorem(k: dict) -> int:
    print('\nРешение системы сравнений первой степени\nВаша система:\n')
    array = []
    items = k.items
    for i in items():
        array.append([i[0], i[1]])
        print('x = ' + str(i[0]) + 'mod' + str(i[1]))
    N = 1
    for i in array:
        N *= i[1]
    print('\nN = ', end='')
    Ns = []
    for i in range(len(array)):
        if i != len(array) - 1:
            print(array[i][1], '· ', end='')
        else:
            print(array[i][1], '=', N)
        Ns.append(round(N / array[i][1]))
    Ns_Us_table = PrettyTable()
    Ns_Us_table.field_names = range(len(k) + 1)
    Ns_Us_table.add_row(['N'] + Ns)
    print(Ns_Us_table)
    Us = []
    for i in range(len(k)):
        u = Extended_Euclidean_algorithm(Ns[i], array[i][1])[1]
        print('u =', u)
        Us.append(u)
    Ns_Us_table.add_row(['u'] + Us)
    print(Ns_Us_table)
    a = 0
    for i in range(len(k)):
        a += array[i][0] * Us[i] * Ns[i]
    print('\na = ', end="")
    for i in range(len(k)):
        print(staples(array[i][0]) + ' · ' + staples(Us[i]) + ' · ' +
              staples(Ns[i]),
              end='')
        if i != len(k) - 1:
            print(' + ', end='')
    a = round(a % N)
    print('\na = ' + str(a))
    return a

def Extended_Euclidean_algorithm(a: int, b: int):
    print(
        '\nПоиск наибольшего общего делителя "d" и коэффициентов x и y\nдля линейной комбинации '
        + str(a) + 'x + ' + str(b) + 'y = d для чисел ' + str(a) + ' и ' +
        str(b))
    if a <= 0 or b <= 0:
        return "Error"
    x2, x1, y2, y1 = 1, 0, 0, 1
    table = PrettyTable()
    table.field_names = ['q', 'r', 'x', 'y', 'a', 'b', 'x2', 'x1', 'y2', 'y1']
    table.add_row(['-', '-', '-', '-', a, b, x2, x1, y2, y1])
    while b > 0:
        q = a // b
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
        table.add_row([q, r, x, y, a, b, x2, x1, y2, y1])
    print(table)
    d = a
    x = x2
    y = y2
    print('Ответ:\nНаибольший общий делитель: ' + str(d) + '\nx = ' + str(x) +
          '\ny = ' + str(y))
    return d, x, y

from functools import reduce
 
 
def egcd(a, b):
    "" "Расширенный Евклид" ""
    if 0 == b:
        return 1, 0, a
    x, y, q = egcd(b, a % b)
    x, y = y, (x - a // b * y)
    return x, y, q
 
 
def chinese_remainder(pairs):
    mod_list, remainder_list = [p[0] for p in pairs], [p[1] for p in pairs]
    mod_product = reduce(lambda x, y: x * y, mod_list)
    mi_list = [mod_product//x for x in mod_list]
    mi_inverse = [egcd(mi_list[i], mod_list[i])[0] for i in range(len(mi_list))]
    x = 0
    for i in range(len(remainder_list)):
        x += mi_list[i] * mi_inverse[i] * remainder_list[i]
        x %= mod_product
    return x

if __name__=='__main__':
    print(chinese_remainder([(91, 90), (21, 13), (77, 76)]))