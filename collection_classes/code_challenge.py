import json
from collections import defaultdict

# open the data file and load the json
def get_event_classification():
    with open("../data_files/30DayQuakes.json", "r") as datafile:
        data = json.load(datafile)

    #use a defaultdict to categorize each event and count each one
    totals = defaultdict(int)
    for event in data["features"]:
        totals[event["properties"]["type"]] += 1

    return dict(totals)

get_event_classification()