from collections import defaultdict
from graphUtils import Node, Edge
import functools
import operator
import queue


class CitiesGraph:
    def __init__(self, cities, connections):
        self.nodes = defaultdict(Node)
        self.edges = defaultdict(list)
        self.daysToStartingCity = defaultdict(int)

        for city in cities:
            self.addCity(city)

        for connection in connections:
            self.addConnection(connection)

        for city in self.nodes:
            if self.nodes[city].isBase:
                self.startingCity = city

        self.getDaysToCities()

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
                             for nextCity in self.edges[currentCity]
                             if self.daysToStartingCity[currentCity] <= daysLeft]

            if shorterPath:
                possiblePaths.append([shorterPath])

            return functools.reduce(operator.iconcat, possiblePaths, [])
        elif path[-1] == self.startingCity:
            return [path]
        else:
            return []

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
                           for path in self.getPossiblePaths([], days)],
                          key=lambda x: x[1], reverse=True)[0]

        bestPath[0].insert(0, self.startingCity)

        return bestPath

    def getDaysToCities(self):
        visited = []
        distances = defaultdict(int)

        q = queue.Queue()
        distances[self.startingCity] = 0

        q.put(self.startingCity)
        visited.append(self.startingCity)

        while not q.empty():
            currentCity = q.get()

            for adjacentCity in self.edges[currentCity]:
                nextCityName = adjacentCity.nextNode

                if nextCityName in visited:
                    continue

                distances[nextCityName] = distances[currentCity] + 1
                q.put(nextCityName)
                visited.append(nextCityName)

        self.daysToStartingCity = distances
