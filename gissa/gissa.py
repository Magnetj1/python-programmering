import random

print("\n---------------------------------")
print(".:GissaTalet:.")

print("gissa ett tal mellan 1-10,du får 3 st försök!\n")
slumptal = random.randint(1,10)
print(slumptal)

i=0
hittat = False

while i<3:
    gissatal = input ("mata in ett tal:")

    if slumptal == int(gissatal):
        hittat == True
        print("bruv")
        break

    i += 1
    
    if hittat:
        print("buvva")
    else:
        print("what!")

        print("____________________________________________________________________________")