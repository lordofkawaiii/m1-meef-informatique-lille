import sys
import math
import random
from liste_7776_mots import LISTE_MOTS


def meh(list):
    print("0 : ", list[0], "\n", len(list), " : ",
          list[-1], "\n2094 : ", list[2094])


def toNum(str):
    index = 1
    total = 0
    for k in str:
        pow = len(str) - index
        total = total + (int(k)-1)*int(math.pow(6, pow))
        index = index+1
    print(total)
    return total


def toWord(str):
    res = LISTE_MOTS[toNum(str)]
    return res


def generate(nb):
    numb = ""
    for k in range(nb):
        for g in range(5):
            numb = numb + str(random.randint(1, 6))
    print(numb)
    return numb


def generatePhrasePasse(rdm):
    i = 0
    i2 = 5
    finalstr = ""
    for k in range(int(len(rdm)/5)):
        l = toWord(rdm[i:i2])
        rup = ''
        for i in range(len(l)):
            if bool(random.getrandbits(1)):
                rup = rup + str.upper(l[i])
            else:
                rup = rup + l[i]
        finalstr = finalstr + rup
        i = i2
        i2 = i2+5
        if i != len(rdm):
            finalstr = finalstr + "-"
    print(finalstr)


max = (-1, "")
min = (sys.maxsize, "")
if (all(LISTE_MOTS)):
    for mot in LISTE_MOTS:
        if len(mot) > max[0]:
            max = (len(mot), mot)
        elif len(mot) < min[0]:
            min = (len(mot), mot)

print("the max length word is : ", max[1],
      "\n the min length word is : ", min[1])
meh(LISTE_MOTS)
toWord('11111')
toWord('66666')
toWord('24521')
generate(2)
generate(4)
generatePhrasePasse(generate(5))
