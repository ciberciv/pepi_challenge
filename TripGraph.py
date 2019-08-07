from CitiesGraph import CitiesGraph
from collections import defaultdict
import functools
import operator
import queue


class TripGraph(CitiesGraph):
    def __init__(self, cities, connections, maxDays):
        assert 2 <= maxDays <= 7, "Trip has to be between 2 and 7 days long"
        CitiesGraph.__init__(self, cities, connections)
        self.startingCity = list(filter(lambda city: self.nodes[city].isBase, self.nodes))[0]
        self.maxDays = maxDays
        self.daysToStartingCity = self.getDaysToCities()
        self.bestPath = self.getBestPath()

    def getDaysToCities(self):
        """
        Return a dictionary with cities as keys and minimum days to go back to the starting city as values using BFS.
        :return : dict(int)
        """
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

        return distances

    def getPossiblePaths(self, path, daysLeft):
        """
        In each recursive call, returns a list of lists with the possible paths developing over time. In the end,
        returns a list of lists of correct paths (that is, ends in startingCity and in less than the initial days.
        :param path: list<str>
        :param daysLeft: int
        :return: list<list<str>>
        """
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

    def calculatePathReward(self, path):
        """
        Given a path, gets the actual reward considering the reward and the cost of the trip
        :param path: list<str>
        :return: int
        """
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

    def getBestPath(self):
        """
        Selects the best path out of the possible paths
        :return: (list<str>, int)
        """
        bestPath = sorted([(path, self.calculatePathReward(path))
                           for path in self.getPossiblePaths([], self.maxDays)],
                          key=lambda x: x[1], reverse=True)[0]

        bestPath[0].insert(0, self.startingCity)

        return bestPath
