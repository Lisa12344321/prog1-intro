import random

from random import randint


slump = randint(1,100)

if slump >= 90:
    print("Du fick en hamburgare! 10%")
    exit()
elif slump >= 70:
    print("Du fick en pizza! 30%")
    exit()
elif slump >= 50:
    print("Du fick en kebabrulle! 50%")
    exit()
else:
    print("Du fick lucas kyckling! 49%")
    exit()
