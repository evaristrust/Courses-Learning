from rpg import person, colors

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 12, "dmg": 40},
         {"name": "Flood", "cost": 20, "dmg": 50}]
player = person(460, 65, 60, 34, magic)
enemy = person(1200, 65, 45, 25, magic)
running = True
i = 0
# print out enemy attacks with setting colors
print(colors.FAIL + colors.BOLD + "AN ENEMY ATTACKS!" + colors.ENDC)
while running:
    print("===================" + colors.OKBLUE)
    player.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
       dmg = player.generate_damage()
       enemy.take_damge(dmg)
       print("You attacked for ", dmg, "points of damage. Enemy hp:", enemy.get_hp())
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic")) - 1
        magic_dmg = player.generate_spell_damge(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()
        if cost > current_mp:
            print (colors.FAIL + "\n Not enough MP \n" + colors.ENDC)
            continue
        player.reduce_mp(cost)

        # Tell enemy to take damage

        enemy.take_damge(magic_dmg)
        print(colors.OKBLUE + "\n" + spell + "Deals", str(magic_dmg), "points of damage" + colors.ENDC)


    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damge(enemy_dmg)
    print("Enemy attacked for ", enemy_dmg)

    print("================================")
    print("Enemy HP: ", colors.FAIL +str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + colors.ENDC)
    print("Your HP: ", colors.OKBLUE + str(player.get_hp()) + "/" +str(player.get_maxhp()) + colors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(colors.OKBLUE + "You win" + colors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(colors.FAIL + "Enemy defeated you" +colors.ENDC)
        running = False

# N.B : Just advanced on the course and will come back to playing this funny game!!!!
# Will resume at Healing our player
# There is still an error on the choose magic! 2
"""
    player.choose_magic()
    choice = input("Choose Action: ")
    print("You choose", choice)
    index = int(choice) - 1
    print("You choose", player.get_spell_name(int(choice)))
    running = False
    i += 1
    
    
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())

"""
