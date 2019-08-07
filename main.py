import json
from citiesGraph import CitiesGraph


with open("exercise1.json") as file:
    data = json.load(file)

cities = data["cities"]
connections = data["connections"]

pepi = CitiesGraph(cities, connections)

print(pepi.getBestPath(5))
