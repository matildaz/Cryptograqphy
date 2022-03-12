def encode(plain_text, a, b):
    plain_text = plain_text.casefold()
    plain_text = plain_text.replace('.','')
    plain_text = plain_text.replace(',','')
    d1 = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    d2 = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
    message = ''
    count = 0
    m = 26
    mass = []
    for i in range(0,1000):
      if (a * i) % m == 1:
        mass.append(i)
    if len(mass) == 0:
      raise ValueError('Error')
    for i in plain_text:
      if i == ' ':
        continue
      count += 1
      if i.isdigit():
        message += i
      else:
        y = int(d1[i])
        y = y * a
        y = y + b
        y = y % 26
        message = message + d2[y]
      if count == 5:
        if i == plain_text[-1]:
          continue
        message += ' '
        count = 0
    return message


def decode(ciphered_text, a, b):
    d1 = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
    d2 = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
    m = 26
    mass = []
    for i in range(0,1000):
      if (a * i) % m == 1:
        mass.append(i)
    if len(mass) == 0:
      raise ValueError('Error')
    c = mass[0]   
    message = ''
    for j in ciphered_text:
      if j == ' ':
        continue
      if j.isdigit():
        message += j
        continue
      y = int(d1[j])
      y = y - b
      y = c * y
      y = y % m
      message = message + d2[y]
    return message

if __name__ == "__main__":
  print(encode("zt ne govno",5,27))
  print(decode("wsovf tcot",5,27))
