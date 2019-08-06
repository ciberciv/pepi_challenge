from collections import defaultdict
import functools
import operator


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

    def getPossiblePaths(self, startingCity, path, daysLeft):
        currentCity = startingCity
        shorterPath = []

        if path:
            currentCity = path[-1]

            if path[-1] == startingCity:
                shorterPath = path

        if daysLeft:
            possiblePaths = [self.getPossiblePaths(startingCity, path + [nextCity], daysLeft - 1)
                            for item in self.edges[currentCity]
                            for nextCity, _ in item.items()]

            if shorterPath:
                possiblePaths.append([shorterPath])

            return functools.reduce(operator.iconcat, possiblePaths, [])
        else:
            return [path]
