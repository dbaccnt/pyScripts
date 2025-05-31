# Read data from a CSV file into an object structure

import csv
import pprint

# read the contents of a csv file into an object structure
result = []

# TODO: open the csv file for reading
with open("../data_files/largequakes.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    sniffer = csv.Sniffer()
    sample = csvfile.read(1024)
    csvfile.seek(0)

    if(sniffer.has_header(sample)):
        next(reader)

    for row in reader:
        #print(row)
        result.append(
            {
                "place": row[0],
                "magnitude": row[1],
                "date": row[2],
                "link": row[3]

            }
        )

pprint.pp(result)