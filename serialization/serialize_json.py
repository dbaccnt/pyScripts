import json
import datetime

# read in the contents of the json file
with open("../data_files/30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def isbig(x):
    mag = x["properties"]["mag"]
    return mag is not None and mag > 6

# TODO: define a function to transform complex JSON to simpler JSON
def simplequake(q):
    return{
        "place": q["properties"]["place"],
        "mag" : q["properties"]["mag"],
        "link" : q["properties"]["url"],
        "date": str(datetime.date.fromtimestamp(int(q["properties"]["time"])/1000))
    }

# filter the data to only include large quakes
largequakes = list(filter(isbig,data["features"]))
# TODO: transform the data to a JSON format we want to save
largequakes = list(map(simplequake, largequakes))

# TODO: use the dumps() function to write json to a string
str = json.dumps(largequakes, sort_keys=True, indent=4)
print(str)

# TODO: use the dump() function to write json to a file
with open("largequakes.json", "w") as outfile:
    json.dump(largequakes, outfile, sort_keys=True, indent=4)