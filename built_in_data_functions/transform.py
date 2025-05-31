import json
import pprint
import datetime

"""
The map function: 
creates an iterator that takes one or more sequences of values and produces a new sequence by applying a given 
function to each value in the original sequeneces

It returns a new list with the results of applying a function to each item in a iterable object.
"""

with open("../data_files/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Filter the data down to the largest events
def bigmag(q):
    return q['properties']['mag'] is not None and q['properties']['mag'] >= 6

results = list(filter(bigmag,data['features']))

# TODO: transform the largest events into a simpler structure

def simplify(q):
    return{
        "place": q["properties"]["place"],
        "magnitude":q["properties"]["mag"],
        "date": str(datetime.date.fromtimestamp(q["properties"]["time"]/1000))
    }

results = list(map(simplify, results))
pprint.pp(results)