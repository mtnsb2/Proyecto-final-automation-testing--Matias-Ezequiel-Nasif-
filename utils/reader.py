import csv
import json

def lector_users_csv():
    with open("data/users.csv",newline="") as file:
        lector = csv.DictReader(file)
        return list(lector)
    
'''data = lector_users_csv()
print(data)'''

def read_products_json():
    with open("data/products.json") as file:
        return json.load(file)
    
data = read_products_json()
print(data)
