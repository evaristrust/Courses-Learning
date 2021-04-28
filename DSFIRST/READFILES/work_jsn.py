import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import json

jason_obj = """{"zoo": "Lion",
             "food": ["Meat", "Veggies", "Honey"],
             "fur": "Golden",
             "clothes": null,
             "diet": [{"zoo": "Gazelle", "food": "Grass", "fur": "Brown"}]
             }
             """

data = json.loads(jason_obj) #loading the json object
print(data)
print(json.dumps(data)) #saved as json

#create a df from json object
dframe = DataFrame(data['diet'])
print(dframe)