def main():
    gloslista = {}
    print("-:glosor:-")
    antal_ratt = 0
    


    while True:
        svglosa = input("\n \tMata in svensk glosa: ")
        englosa = input("\n \tMata in eng glosa: ")
        
        gloslista.update({svglosa : englosa})



        stoppa = input("\n\t Villl du mata in en glosa till? j/n ")
        if (stoppa == "n"):
            break

    while True:

        print("\n Nu startar glosförhöret!!!")
        for glosa in gloslista:

            svar = input (f"\n{glosa} : ") 

            if svar == gloslista [glosa]:
                print("Rätt svar")
                antal_ratt += 1
                print(f"\n{antal_ratt}")
            else:
                print(f"\n Fel svar, det är {gloslista[glosa]}")
                print(f"\n{antal_ratt}")
        
        RAWR = input ("vill du köra om? j/n: ")
        if RAWR == "n":
            break

main()