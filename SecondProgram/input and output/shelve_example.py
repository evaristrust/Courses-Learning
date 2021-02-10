import shelve

with shelve.open("ShelfTest") as fruits: # opening a persistant dictionary fruits
    fruits["lemon"] = "sweet and happiness generator"
    fruits["orange"] = "highly testing and also for dates"
    fruits["mango"] = "ate when i was young at mom fields"
    fruits["pineapple"] = "so and so sweet one in the globe"

    print(fruits['lemon'])
    print(fruits['orange'])
    print(fruits['mango'])
    print(fruits['pineapple'])

