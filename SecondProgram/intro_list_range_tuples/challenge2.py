# Create a list of items
# then create an iterator using the iter() function
# use a for loop to loop "n" times, when n is the number of items in your list
# Hint: use the len() functionr ather than counting the number of items in the list

items = ["hello", "dear", "hi", "holla", "Salute"]
my_items = iter(items)
n = len(items)

for x in range(0, n):
    next_item = next(my_items)
    print(next_item)