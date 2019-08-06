from collections import defaultdict
from graphUtils import Node, Edge
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

        for city in self.nodes:
            if self.nodes[city].isBase:
                self.startingCity = city

    def addCity(self, cityObject):
        city = Node(cityObject["reward"], cityObject.get("base", False))
        self.nodes[cityObject["name"]] = city

    def addConnection(self, connectionObject):
        vertex1 = connectionObject["from"]
        vertex2 = connectionObject["to"]
        cost = connectionObject["cost"]

        self.edges[vertex1].append(Edge(vertex2, cost))
        self.edges[vertex2].append(Edge(vertex1, cost))

    def getPossiblePaths(self, path, daysLeft):
        currentCity = self.startingCity
        shorterPath = []

        if path:
            currentCity = path[-1]

            if path[-1] == self.startingCity:
                shorterPath = path

        if daysLeft:
            possiblePaths = [self.getPossiblePaths(path + [nextCity.nextNode], daysLeft - 1)
                             for nextCity in self.edges[currentCity]]

            if shorterPath:
                possiblePaths.append([shorterPath])

            return functools.reduce(operator.iconcat, possiblePaths, [])
        else:
            return [path]

    def calculatePathWeight(self, path):
        visited = []
        netReward = 0
        currentCity = self.startingCity

        for city in path:
            reward = self.nodes[city].reward * (city not in visited)
            cost = [edge.cost for edge in self.edges[currentCity] if edge.nextNode == city][0]
            visited.append(city)
            currentCity = city
            netReward += reward - cost

        return netReward

    def getBestPath(self, days):
        bestPath = sorted([(path, self.calculatePathWeight(path))
                           for path in filter(lambda x: x[-1] == self.startingCity, self.getPossiblePaths([], days))],
                          key=lambda x: x[1], reverse=True)[0]

        bestPath[0].insert(0, self.startingCity)

        return bestPath
