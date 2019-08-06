class Node:
    def __init__(self, reward, isBase):
        self.reward = reward
        self.isBase = isBase


class Edge:
    def __init__(self, nextNode, cost):
        self.nextNode = nextNode
        self.cost = cost
