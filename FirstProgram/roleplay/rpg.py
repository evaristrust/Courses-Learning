import random

# creating a colors class
class colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    WARNING = "\033[92m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


# create person class
class person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    # let's generate damage
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damge(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    # Create a function for a player or enemy to take damage
    def take_damge(self, dmg):
        self.hp = dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_maxmp(self):
        return self.maxmp

    def get_mp(self):
        return self.mp

    def reduce_mp(self, cost):
        self.mp = cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self):
        return self.magic[i]["cost"]

    # two more methods

    # choose action and choose magic
    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["dmg"]) + ")")
            i += 1
