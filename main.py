import json
from graph import citiesGraph

with open("exercise1.json") as file:
    data = json.load(file)

cities = data["cities"]
connections = data["connections"]

pepi = citiesGraph(cities, connections)