

with open("text.txt", "r") as my_file:
    data = my_file.read()
ciphertext = encode(data, key)
a = ciphertext

b = ''
alpha = np.array([['a', 0], ['b', 1], ['c', 2], ['d', 3],
                  ['e', 4], ['f', 5], ['g', 6], ['h', 7],
                  ['i', 8], ['j', 9], ['k', 10], ['l', 11],
                  ['m', 12], ['n', 13], ['o', 14], ['p', 15],
                  ['q', 16], ['r', 17], ['s', 18], ['t', 19],
                  ['u', 20], ['v', 21], ['w', 22], ['x', 23],
                  ['y', 24], ['z', 25]])
for i in a:
    if i in alpha:
        b += i
n = 3
stride = m.ceil(len(b) / n)
parts = [b[i:i + stride] for i in range(0, len(b), stride)]
g = 0
for i in parts:
    c = Counter(i)
    c = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))
    s = 0
    for k in c.values():
        s += (k * (k - 1) / (len(i) * (len(i) - 1)))
    g += s
print('Индекс совпадений равен', g / n)

t1 = ''
t2 = ''
t3 = ''
for ind, i in enumerate(b):
    if ind % 3 == 0:
        t1 += i
    elif ind % 3 == 1:
        t2 += i
    else:
        t3 += i

c = Counter(t1)
c = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))
print(c)

c = Counter(t2)
c = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))
print(c)

c = Counter(t3)
c = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))
print(c)