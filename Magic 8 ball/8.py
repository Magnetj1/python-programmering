
import random

min_lista1 = ["It is certain"," It is decidedly so","Without a doubt","Yes definitely","You may rely on it","As I see it, yes","Most likely","B-B-B- BLA good!!!"," Outlook good","Yes","Signs point to yes"]
min_lista2 = ["Reply hazy, try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","MAN STOP ASKING IM NOT GIVING YOU A ANSWER!!!!"]
min_lista3 = ["Don't count on it","My reply is no","My sources say no","Outlook not so good"," Very doubtful","NO YOU WILL STAY A VIRGIN UNLESS YOU UN VIRGIN THE OLIVE OIL!"]
    

while True: 
    shake = input ("Do you wanna shake the ball?")
    bruv = random.randint(0,2)
    if bruv == 0:
        print (random.choice(min_lista1))
    elif bruv == 2:
        print (random.choice(min_lista2))
    else:
        print (random.choice(min_lista3))