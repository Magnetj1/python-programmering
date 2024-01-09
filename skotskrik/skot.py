texten_innan = input ("IM SCOT")
texten_efter = ""

for bokstav in texten_innan:
    if bokstav == "O" or bokstav =="A" or bokstav == "Y" or bokstav == "S":
        texten_efter += "E"
    else:
        texten_efter += bokstav
print(texten_efter.upper())