# we are going to open a simple txt file

cities = ["Kigali", "Kampla", "Dar es Salaam", "Nairobi", "Buja"]

with open("cities.txt", 'w') as cities_file:
    for city in cities:
        print(city, file=cities_file)

# what if i want to append this by a times 2 table

with open("cities.txt", "a") as tables:
    for i in range(0, 13):
        for j in range(0, 13):
            print("{} times {} is {}".format(i, j, i * j), file=tables)
        print("--" * 10, file=tables)