r = float(input("Insert average rate of star formation in our Galaxy: "))
f = float(input("Insert fraction of those stars that have planets: "))
n = float(input("Insert the average number of planets that can potentially support life per star that has planets: "))
p = float(input("Insert the fraction of planets that could support life that actually develop life at some point: "))
il = float(input("Insert fraction of planets with life that go on to develop intelligent life: "))
t = float(input("Insert fraction of civilizations that develop a technology that releases detectable signs of their existence into space: "))
l = float(input("Insert length of time for which such civilizations release detectable signals into space: "))

intelligentLife = (r*f*n*p*il*t*l)

print(intelligentLife)