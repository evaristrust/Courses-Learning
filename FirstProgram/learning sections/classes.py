import random

class premierLeague:
      team1 = "Arsenal"
      team2 = "Liverpool"
      team3 = "Chelsea"
      def get_team(self):
          print("The top team is PL are: \n", self.team1,"\n", self.team2, "\n", self.team3)
topTeam = premierLeague()
topTeam.get_team()


# The above is how we we deal with the classes ! rehusle down there
class rwandanTeam:
    teamA = "APR"
    teamB = "Kiyovu"
    teamC = "Mukura"
    teamD = "AS Kigali"

    def print_team(self):
        print("These are the ones: \n", self.teamA, "\n", self.teamB, "\n", self.teamC,
              "\n", self.teamD)


firstTeam = rwandanTeam()
firstTeam.print_team()

# Going to do the above using the simple way using __init__
class hits:
    speed = "100KM/S" # this is added after
    def __init__(self,hit1,hit2,hit3):
         self.hit1 = hit1
         self.hit2 = hit2
         self.hit3 = hit3
    def find_hits(self):
         print(self.hit1, self.hit2, self.hit3)
    def getSpeed(self):
         print(self.speed)
bestOne = hits('Abudabi','Kola','samoya')
bestOne.find_hits()
bestOne.getSpeed() #this is added after to check the speed
secondOne = hits('ayiwe', 'ele','dunda')
secondOne.find_hits()
secondOne.getSpeed()


'''
playerhp = 800
enemyattack1 = 600
enymyattack2 = 700

while playerhp > 0:
    dmg = random.randrange(enemyattack1,enymyattack2)
    playerhp = playerhp-dmg
    """if playerhp <= 0:
        playerhp = 0
    print("This enmey strikes", dmg, "points of damage! "
          "The remaining points is ", playerhp)
    if playerhp == 0:
        print("You just died and you not in the game!")
        """
    # This code without a break will continuosly learn
    # We are going to put the break so that the loop will break when
    # - we reach the minimum
    if playerhp <= 30:
        playerhp = 30
    print("This enmey strikes", dmg, "points of damage! "
                                     "The remaining points is ", playerhp)
    if playerhp > 30:
       # use continue to continue the loop
        # use pass here when you need avoid a python error
        print("You've reached your low points!")
        break
    # That's how we deal with break issues! Do you get it mofucker?
    # yes I understand

'''