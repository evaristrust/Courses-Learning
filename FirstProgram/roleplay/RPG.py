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
        return random.randrange(self.atkl, self.atkh)
    def generate_spell_damge(self):
        mgl = self.magic[1]["dmg"] - 5
        mgh = self.magic[1]["dmg"] + 5
        return random.randrange(mgl,mgh)
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
    def get_spell_name(self):
        return self.magic[1]["name"]
    def get_spell_mp_cost(self):
        return self.magic[1]["cost"]
    # two more methods

    # choose action and choose magic
    def choose_action(self):
        i = 1
        print("Actions")
        for item in self.actions:
            print(str(1) + ":", item)
            i += 1
    def choose_magic(self):
        i = 1
        print("Magic")
        for spell in self.magic:
            print(str(1) + ":", spell["name"], "(cost:", str(spell["dmg"]) + ")")
            i += 1





