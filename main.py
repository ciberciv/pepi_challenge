import sys
import json
from TripGraph import TripGraph


# This takes care of arguments to run the script from the command line. Default is "map.json" and 7 days.
# You can specify only the file or both file and number of days too.
if len(sys.argv) == 1:
    filename = "map.json"
    maxDays = 7
elif len(sys.argv) == 2:
    filename = sys.argv[1]
    maxDays = 7
else:
    filename = sys.argv[1]
    maxDays = int(sys.argv[2])

with open(filename) as file:
    data = json.load(file)

cities = data["cities"]
connections = data["connections"]

pepi = TripGraph(cities, connections, maxDays)

(path, profit) = pepi.bestPath

print("Cities (in order):", path)
print("Profit:", profit)
