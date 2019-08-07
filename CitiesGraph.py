from collections import defaultdict
from graphUtils import Node, Edge


# Graph model for this particular problem. Allows to add nodes and edges.
class CitiesGraph:
    def __init__(self, cities, connections):
        self.nodes = defaultdict(Node)  # Node objects have reward and isBase properties
        self.edges = defaultdict(list)  # Edge objects have nextNode (the node connected) and cost properties

        for city in cities:
            self.addCity(city)

        for connection in connections:
            self.addConnection(connection)

    def addCity(self, cityObject):
        """
        :param cityObject: {'name': str, 'base': bool, 'reward': int}
        """
        city = Node(cityObject["reward"], cityObject.get("base", False))
        self.nodes[cityObject["name"]] = city

    def addConnection(self, connectionObject):
        """
        :param connectionObject: {'from': str, 'to': str, 'cost': int}
        """
        vertex1 = connectionObject["from"]
        vertex2 = connectionObject["to"]
        cost = connectionObject["cost"]

        self.edges[vertex1].append(Edge(vertex2, cost))  # The edges property is a dict with cities as keys and lists of
        self.edges[vertex2].append(Edge(vertex1, cost))  # Edge objects as values to where the city connects
