# demonstrate how to serialize data to a csv file
import csv
import json
import datetime

# read in the contents of the json file
with open("../data_files/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 5

# filter the data by quakes that are larger than 5 magnitude
largequakes = list(filter(isbig, data["features"]))

#print(largequakes)

# TODO: Create the header and row structures for the data
header = ["Place", "Magnitude", "Link", "Date"]
rows = []

# TODO: Populate the rows with the resulting quake data
for quake in largequakes:
    thedate = datetime.date.fromtimestamp(
        int(quake["properties"]["time"]/1000))
    rows.append([quake["properties"]["place"],
                 quake["properties"]["mag"],
                 quake["properties"]["url"],
                 thedate])

print(rows)
# TODO: write the results to the csv file
#with open("../data_files/largequakes.csv", "w") as csvfile:
#    writer = csv.writer(csvfile, delimiter=",")
#    writer.writerow(header)
#    writer.writerow(rows)