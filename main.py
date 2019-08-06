import json
from citiesGraph import citiesGraph

with open("exercise1.json") as file:
    data = json.load(file)

cities = data["cities"]
connections = data["connections"]

pepi = citiesGraph(cities, connections)

thing = list(filter(lambda x: x[-1] == "Madrid", pepi.getPossiblePaths("Madrid", [], 5)))

print(thing)
