import simplejson as json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:
   old_file = open("./ages.json", "r+")
   data = json.loads(old_file.read())
   print("My current age is:", data["age"])
   data["age"] += 1
   print("New age is:", data["age"])

else:
    old_file = open("./ages.json", "w+")
    # generate object data
    data = {"Name": "Evariste", "age": 24}
    print("The file was not found ", "The age is :", data["age"] )

old_file.seek(0)
old_file.write(json.dumps(data))