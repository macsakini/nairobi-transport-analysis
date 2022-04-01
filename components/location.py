import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json

#import datasets
f = open("../data/nairobi_sublocations.json")

data_locations = json.load(f)

data_populations =pd.read_csv("../data/census_volume_1_question_1_population_households_and_density_by.csv")

print(data_populations.head())

print(data_locations.keys())

print(data_locations["features"][12])

print(data_locations["features"][15])

for location in data_locations["features"]:
    print(location["properties"])
    for location2 in data_populations["area"]:
        #if it matches without any string processing
        if str(location2) == location:
            _dict = {
                "population":location2["population"], 
                "density":location2["density"], 
                "area":location2["area"]
            }
            location["properties"] = _dict
        
        elif(Preprocessing(location2).call()):
             _dict = {
                "population":location2["population"], 
                "density":location2["density"], 
                "area":location2["area"]
            }
            location["properties"] = _dict
    
    class Preprocessing():
        def __init__(self, string):
            self.string = string

        def lowercase(self):
            pass

        def remove_punctuations(self):
            pass

        def check_slash(self):
            pass

        def check_match_percentage(self):
            pass
        
        def call(self):
            pass