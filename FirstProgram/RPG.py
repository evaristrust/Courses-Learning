import random
#creating a colors class
class colors:
    color1 = "\033[0;37;40m"
    color2 = "\033[2;37;40m"
    color3 = "\033[1;37;40m"
    color4 = "\033[3;37;40m"

# create person class
class person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]
    # let's generate damage
    def generate_damage(self):
        return random.randrange(self.atkh, self.atkl)


