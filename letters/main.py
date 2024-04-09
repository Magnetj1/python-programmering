sentence = input("write smtn!!!").upper().replace(" ","")

dictionary = {
}

for letter in sentence:
    if letter in dictionary:
        dictionary[letter] += 1
        pass
    else:
        dictionary  [letter] = 1

print (dictionary)