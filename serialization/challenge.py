import json
import csv
import datetime
from os import write

# open the data file and load the JSON
with open("../data_files/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# create a csv file with the following information
# 40 most significant seismic events, ordered by most recent
# header row: Magnitude, place, felt reports date, and google map link
# date should be in the format of YYYY-MM-DD

def getsig(x):
    sig = x["properties"]["sig"]
    return 0 if sig is None else sig

significantevents = sorted(data["features"], key=getsig, reverse=True)
significantevents = significantevents[:40]
significantevents.sort(key=lambda e: e["properties"]["time"], reverse=True)

header = ["Magnitude","Place","Felt Reports","Date","Link"]
rows = []

for event in significantevents:
    thedate = datetime.date.fromtimestamp(
        int(event["properties"]["time"]) / 1000)
    lat = event["geometry"]["coordinates"][1]
    long = event["geometry"]["coordinates"][0]
    gmaplink = f"https://maps.google.com/maps/search/?api=1&query={lat}%2C{long}"

    rows.append([event["properties"]["mag"],
                 event["properties"]["place"],
                 0 if event["properties"]["felt"] is None else event["properties"]["felt"],
                 thedate,
                 gmaplink])

with open("significantevents.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerow(rows)
