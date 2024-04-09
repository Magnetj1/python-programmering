nummerlista = []
nummerlista = input("skriv nummer så får du ett medel värde, minst 3 nummer \n").split()

for i in range(len(nummerlista)):
    if i == 0 or i == len(nummerlista) -1 :
        pass
    else:
        print(nummerlista[i] + nummerlista[i-1] + nummerlista[i+1])