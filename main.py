import json
from TripGraph import TripGraph


with open("exercise1.json") as file:
    data = json.load(file)

cities = data["cities"]
connections = data["connections"]

pepi = TripGraph(cities, connections, 5)

print(pepi.bestPath)
