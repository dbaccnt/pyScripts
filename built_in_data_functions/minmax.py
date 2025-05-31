import json

with open("../data_files/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

print(data["metadata"]["title"])
print(len(data["features"])) #contains all the earthquakes


def getmag(dataitem):
    magnitude = dataitem["properties"]["mag"]
    if (magnitude is None):
        magnitude = 0
    return float(magnitude)

print(min(data["features"], key=getmag))
print(max(data["features"], key=getmag))

#print(getmag(data["features"][1]))