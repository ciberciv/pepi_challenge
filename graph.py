from collections import defaultdict


class citiesGraph:
    def __init__(self, cities, connections):
        self.nodes = defaultdict(list)
        self.edges = defaultdict(list)

        for city in cities:
            self.addCity(city)

        for connection in connections:
            self.addConnection(connection)

    def addCity(self, cityObject):
        city = {"reward": cityObject["reward"], "isBase": cityObject.get("base", False)}
        self.nodes[cityObject["name"]] = city

    def addConnection(self, connectionObject):
        vertex1 = connectionObject["from"]
        vertex2 = connectionObject["to"]
        cost = connectionObject["cost"]

        self.edges[vertex1].append({vertex2: cost})
        self.edges[vertex2].append({vertex1: cost})
