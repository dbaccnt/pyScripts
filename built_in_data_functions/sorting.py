import json

"""
What is the main difference between the sorted function and the sort function
-The sorted function takes an iterable object as an argument and returns a new sorted list,
the sort function sorts a list in-place-
"""

with open("../data_files/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)