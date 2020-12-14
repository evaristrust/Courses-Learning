from roleplay.RPG import person, colors
magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 12, "dmg": 40},
         {"name": "Flood", "cost": 20, "dmg": 50}]
player = person(460, 65, 60, 34, magic)
enemy = person(1200, 65, 45, 25, magic)
running = True
i = 0
# print out enemy attacks with setting colors
print(colors.color1 + colors.color3 + "AN ENEMY ATTACKS!" + colors.color4)
while running:
    print("===================")
   # player.choose_action()
    player.choose_magic()
    choice = input("Choose Action")
   # print("You choose", choice)
    index = int(choice) - 1
    print("You choose", player.get_spell_name(int(choice)))
    running = False
    # i += 1
"""
print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
"""