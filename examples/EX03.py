from typing import AbstractSet, Annotated


# arg1 = 1
char = "a"
# str = "ant"
# arg2 = 9.9
list = ["sipelgas", "mutukas", "putukas"]
dict1 = {
    "pask": "pask",
    "jama": "jama"
}

väärtus1 = 1
väärtus2 = 9.9


def tagastaja(arg1, arg2):
    vastus = arg1 + arg2

    return vastus


print(tagastaja(väärtus1, väärtus2))


väärtus3 = 99
väärtus4 = 19
väärtus5 = 4.444


def okidoki(arg1, arg2, arg3):
    lahend = (arg1 + arg2 + arg3) / arg3

    return lahend


print(okidoki(väärtus1, väärtus2, väärtus3))
print(okidoki(väärtus3, väärtus2, väärtus1))
print(okidoki(väärtus5, väärtus4, väärtus5))

pärdik1 = "Franc"
pärdik2 = "Ott"
pärdik3 = "Rasmus"
pärdik4 = "Hendrik"


def koostaja(arg1, arg2):
    tulem = arg1 + arg2
    print(tulem.upper())


koostaja(pärdik1, pärdik1)
koostaja(pärdik3, pärdik2)

nimekiri = [1, 2, 3, 4, 5]


def listSum(numberlist):
    cool = 0

    for number in numberlist:
        print(number)
        cool = cool + number - 2
        print(cool)


listSum(nimekiri)

peenis = {
    "length": 0.2,
    "girth": 0.1
}

teinePeenis = {
    "length": 20,
    "girth": 40
}


def sisseVotja(arg1, arg2):
    votja = arg1.get("length") + arg2.get("length")
    print("Friendship length is: " + str(votja) + "cm.")
    pitsitus = arg1.get("girth") + arg2.get("girth")
    print("Bertha wont take no cock that has less than {} cm of GIRTH!".format(pitsitus))


sisseVotja(peenis, teinePeenis)
