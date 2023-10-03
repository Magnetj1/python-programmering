import random
class Lotteri:
    def _init_(self):
        self.list_vinster = [
            "cat food"
            "air strike to your area"
            "You get to kill seb!!!"
            "nuhh uhh you get nothin"
            "AK 47 and RPG and minigun and a privet fighter jett"
            "this might not be a win but you get to spend a night with Emanuel when hes drunk"
            "BBQ but with a C at the end"
            "Motivation, you HAVE NO BITCHES KYS NOW!!!"
            ]
        
    def get_vinst(self):
        slumptal = random.randint(0,7)
        return self.list_vinster[slumptal]