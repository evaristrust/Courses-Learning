# going to learn few methods in dict
# Creating two dicts
champions_euro = {"epl": "Arsenal, Chelsea, Man utd",
                  "laliga": "Barcelona, Real Madrid, Atletico",
                  "serie_a": "Juventus, Inter, Ac Milan"}

champions_afro = {"rda":"APR, MUKURA, RAYON SPORT",
                  "burundi": "Atletic, Muzinga, Vitalo",
                  "Tznia": "Simba, Yanga, Azam"}
# I want to join these two champions, I will use update

print(champions_afro.update(champions_euro)) # this will return none.... # but..

champions_afro.update(champions_euro)
print(champions_afro) # this works

# want to combine two dictionaries but don't wanna modify any of the original dicts
# we use copy method

champions_afro_copy = champions_afro.copy()
champions_afro_copy.update(champions_euro)
print(champions_afro_copy) # this works without modifying the original dictionaries above

# just to comfirm: print each dict below and see

print(champions_afro)
print(champions_euro)
