import shelve

with shelve.open("ShelfTest") as frutis:
    fruits["lemon"] = "sweet and happiness generator"
    fruits["orange"] = "highly testing and also for dates"
    fruits["mango"] = "ate when i was young at mom fields"
    fruits["pineapple"] = "so and so sweet one in the globe"

print(fruits["lemon"])
print(fruits["mango"])