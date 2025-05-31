import json

TotalEvents = 0
TotalFelt = 0
MostFeltEvent = ""
MostFeltCount = 0

"""
any() and all() >> Determines whether a dataset matches any or all criteria
sum() adds up all the values in the dataset 
filter() >> selectively removes and keeps data values

How to specify which property of a complex object to sort on when using the sorted and sort function?
-Specify a function with the 'Key' parameter which will sort the data on a particular property-
"""

def calc_summary():
    global TotalEvents, TotalFelt, MostFeltEvent, MostFeltCount

    with open("../data_files/30DayQuakes.json", "r") as datafile:
        data = json.load(datafile)

    felt = list(filter(t_felt, data["features"]))
    highest_quake = max(data["features"], key=most_felt_event)

    #calculate
    TotalEvents = int(data["metadata"]["count"])
    TotalFelt = len(felt)
    MostFeltEvent = highest_quake["properties"]["title"]
    MostFeltCount = int(highest_quake["properties"]["felt"])


def t_felt(d):
    f = d["properties"]["felt"]
    return(f is not None and f >=100)

def most_felt_event(e):
    ev = e["properties"]["felt"]
    if ev is not None:
        return ev
    return 0