import json

"""
any() and all() >> Determines whether a dataset matches any or all criteria
sum() adds up all the values in the dataset 
filter() >> selectively removes and keeps data values
"""
with open("../data_files/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# TODO: are there any quake reports that were felt by more than 25,000 people?
print(any(quake["properties"]["felt"] is not None and quake["properties"]["felt"] > 25000
          for quake in data["features"]))

# TODO: how many quakes were felt by more than 500 people?
print(sum(quake["properties"]["felt"] is not None and quake["properties"]["felt"] >= 500
          for quake in data["features"]))

# TODO; how many quakes had a magnitude of 6 or larger?
print(sum(quake["properties"]["mag"] is not None and quake["properties"]["mag"] >= 6
          for quake in data["features"]))