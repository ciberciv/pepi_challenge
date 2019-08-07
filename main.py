import json
from citiesGraph import citiesGraph


with open("exercise1.json") as file:
    data = json.load(file)

cities = data["cities"]
connections = data["connections"]

pepi = citiesGraph(cities, connections)

print(pepi.getBestPath(5))
