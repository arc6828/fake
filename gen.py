import json 
from faker import Faker
import random
from random import randint
fake = Faker('en_US')
a = []
mode_option = {
    "20KB" : 82,
    "200KB" : 826,
    "2000KB" : 8310,
    "1000KB" : 4150,
    "500KB" : 2100,
}
# key = "20KB"
# key = "200KB"
# key = "2000KB"
# key = "1000KB"
key = "500KB"

for _ in range(mode_option[key]):
    # my_dict = {    'foo': randint(0, 100),    'bar': {'baz': fake.name(),       'poo': float(random.randrange(155, 389))/100   } }
    # print(my_dict)
    my_dict = {
        "name" : fake.name(),
        "address" : fake.address(),
        "text" : fake.text(),
    }
    a.append(my_dict)

with open("dataset-"+key+".json", "w") as f:
    json.dump(a, f)