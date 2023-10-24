def main():
    gloslista = {}
    print("-:glosor:-")
    antal_ratt = 0

    while True:
        svglosa = input("\n\tMata in svensk glosa: ")
        englosa = input("\n\tMata in engelsk glosa: ")

        gloslista.update({svglosa: englosa})

        stoppa = input("\n\tVill du mata in en glosa till? (j/n): ")
        if stoppa.lower() == "n":
            break

    while True:
        print("\nNu startar glosförhöret!!!")
        for glosa in gloslista:
            svar = input(f"\n{glosa} : ")

            if svar == gloslista[glosa]:
                print("Rätt svar")
                antal_ratt += 1
            else:
                print(f"Fel svar, det är {gloslista[glosa]}")

        print(f"\nDu hade {antal_ratt} rätt av {len(gloslista)} glosor.")
        RAWR = input("Vill du köra om? (j/n): ")
        if RAWR.lower() == "n":
            break

if __name__ == "__main__":
    main()
