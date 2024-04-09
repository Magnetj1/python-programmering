blad = int (input("hur många blad har blomman \n"))

one = input("skriv älskar eller inte 1")
two = input("skriv älskar eller inte 2")

for i in range(blad):
    if(i % 2 == 0):
        print(one)
    else:
        print(two)
