import random

from random import randint

spela = True

tal = randint(1,10)

antal_gissningar = 0

statistik = [] # append





while spela == True:

    try:
        gissning = int(input("Gissa det slumpade talet som är mellan 1-10: "))
    except ValueError:
        print("Är du trög?")
        continue


    if gissning == tal:
        print("RÄTT")


        antal_gissningar += 1

        if antal_gissningar == 1:
            print("Du gissade på första försöket!!?")
        elif antal_gissningar > 3:
            print(f"Du behövde {antal_gissningar} gissningar, du SUGER!")
        else:
            print(f"Du behövde {antal_gissningar} gissngar")
        
        
        spela_igen = input("Spela igen?")
        if spela_igen == "nej":
            print(statistik)
            spela = False
        else:
            statistik.append(antal_gissningar)
            antal_gissningar = 0
            tal = randint(1,10)
            spela = True


    elif gissning > tal:
        print("FÖR HÖGT")
        antal_gissningar += 1
    else:
        print("FÖR LÅGT")
        antal_gissningar += 1



    