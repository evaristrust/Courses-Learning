import random

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