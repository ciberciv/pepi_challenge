#### Name

Víctor Casas Moreno

### What is this

This code, written in Python, is my solution to the PEPI Challenge proposed by [The Workshop](https://github.com/The-Workshop-Inventors-of-play/pepi-challenge).

### How to run

The proposed solution takes two arguments: the (relative) path to a json file containing the map and the maximum number of days (restricted to values between 2 and 7 so a returning trip makes sense and matches the problem's restriction).

If no argument is given, it will take the default values "map.json" for the file path and 7 for the number of days. It can work with just the path parameter, again with 7 as default maxDays value, and providing both parameters. Hence, valid commands are:

```shell script
python main.py
python main.py file.json
python main.py file.json 5
```

For the solution to the challenge (that is, taking a week as the number of days), provide only the file path.

About the packages used, all of them are basic Python packages, so none of them needs to be installed assuming a Python3 distribution is used (tested in Python3 Conda distribution). Just in case, here is the list of modules used:
* sys
* json
* collections
* functools
* operator
* queue

### How does the code work

The entry point is main.py. It parses the given arguments and creates a TripGraph object based on them (or the default values). This object, on init, checks the restriction on the days, creates a CitiesGraph object (the basic graph model) and gets other values such as the starting city and the best path, using the class methods.

Once it is created, the best path will be available as its bestPath property and will be printed. Details on the implementation can be seen in comments. 

### Things to improve

First, a BFS is done to find the minimum days (nodes distance) it takes to go from each city to the starting city. The algorithm then performs a Depth-first search, jumping to next nodes at the same level whenever it reaches a node from which it can't return to the starting city. Considering weights as the difference between reward of the next city and the gas cost, it becomes a longest path problem, and using the negative weights, a shortest path problem.

Considering this "negative graph", Dijkstra's algorithm is not useful, since the problem can (and most likely will) have negative weights for any edge, and Bellman-Ford's algorithm can't be applied (at least directly) since weights change depending on whether or not a city has already been visited.

A better solution to this problem may be altering Bellman-Ford's algorithm to work with dynamic weights, but trying that takes more than the 48 hours given to complete the challenge.