import random
from random import randint

print("Jag ska slumpa ett heltal 1-100 och du ska skriva in ett heltal mellan 1-100.")
print("Sedan ska jag skriva ut summan av de talen.")

tal = randint(1,100)

try:
    inläst_tal = int(input("Skriv ett heltal 1-100: "))
except ValueError:
    print("Du är tappad")
    exit()

print(f"Summan av talen är {inläst_tal*randint(1,100)}")