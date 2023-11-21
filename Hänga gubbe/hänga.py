def calc(cows,pigs,chickens):
    
    cow_leg = 4
    pig_leg = 4
    chicken_leg = 2
    cowlegs = cows*cow_leg
    chickenlegs = chicken_leg*chickens
    piglegs = pigs*pig_leg
    total_legs = cowlegs+chickenlegs+piglegs
    print(total_legs)
    '''
    return cows * 4 + pigs * 4  + chickens * 2
     '''
chickens = int(input ("\n\thow many chickens do you have?"))
cows = int(input ("\n\thow many cows do you have?"))
pigs = int(input ("\n\thow many pigs do you have?"))


print(calc(cows, pigs, chickens))