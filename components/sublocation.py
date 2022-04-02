import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from preprocess import Preprocess

#import datasets
f = open("../data/nairobi_sublocations.json")

data_locations = json.load(f)

data_populations =pd.read_csv("../data/census_volume_1_question_1_population_households_and_density_by.csv")

print(data_populations.head())

counter_a = 0
counter_b = 0
counter_c = 0

for location in data_locations["features"] :
    str_loc = location["properties"]["DISPLAY_NAME"]
    for index, _location in data_populations.iterrows():
        #if it matches without any string processing
        if str(_location["area_name"]) == str(str_loc):
            _dict = {
                "population":_location["population"], 
                "density":_location["density"], 
                "area_km":_location["area_km"]
            }
            location["properties"].update(_dict)
            print(location["properties"])
            break
        #if id doesnt match preprocess it using regex
        elif Preprocess(_location["area_name"]).call() == Preprocess(str_loc).call():
            _dict = {
                "population":_location["population"], 
                "density":_location["density"], 
                "area_km":_location["area_km"]}
            location["properties"].update(_dict)
            print(location["properties"])
            counter_a += 1
            break
        #check if word is in the other
        elif Preprocess(_location["area_name"]).call() in Preprocess(str_loc).call() or Preprocess(str_loc).call() in Preprocess(_location["area_name"]).call():
            _dict = {
                    "population":_location["population"], 
                    "density":_location["density"], 
                    "area_km":_location["area_km"]}
            location["properties"].update(_dict)
            print(location["properties"])
            counter_a += 1
            break
        #else just pass
        else:
            pass
        
f.close()



    
