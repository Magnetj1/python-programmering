#Jag gjorde 

gloslista = {}
print("-:glosor:-")
antal_ratt = 0
def Make_glosor():
    while True:
        svglosa = input("\n \tMata in svensk glosa: ")
        englosa = input("\n \tMata in eng glosa: ")
        gloslista.update({svglosa : englosa})
        stoppa = input("\n\t Villl du mata in en glosa till? j/n ")
        if (stoppa == "n"):
            break
Make_glosor()

def Start_glosförhör():
    while True:
        
        print("\n Nu startar glosförhöret!!!")
        for glosa in gloslista:
            svar = input (f"\n{glosa} : ") 

        if svar == gloslista [glosa]:
            print("Rätt svar")
            antal_ratt += 1
            print(f"\n du har {antal_ratt} Rätt!!")
        else:
            print(f"\n Fel svar, det är {gloslista[glosa]}")
            print(f"\n{antal_ratt}")
            
        RAWR = input ("vill du köra om? j/n: ") 
        print(f"\n Du hade {antal_ratt} rätt!!")
        antal_ratt = 0
        if RAWR == "n":
            break
Start_glosförhör()

with open("demofile2.txt", "w") as file:
    for glosa in gloslista:
        print(glosa)
        print(gloslista.get(glosa))
        file.write(glosa + " " +gloslista.get(glosa))
        file.close()