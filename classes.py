from collections import defaultdict

class Route:
    def __init__(self, town, weight):
        self.town = town
        self.weight = weight

    def getTown(self):
        return self.town

    def getWeight(self):
        return self.weight


class Candidate(Route):
    pass

class Destination(Route):
    pass

class Town:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class Visited:
    def __init__(self, town, visited):
        self.town = town
        self.visited = visited

    def getTown(self):
        return self.town

    def isVisited(self):
        return self.visited

    def setVisited(self, visited):
        self.visited = visited

class Graph:
    def __init__(self):
        #compute distance following a route
        self.graph = defaultdict(lambda: defaultdict(int))
        #compute shortest distance
        self.graphP = defaultdict(list)
        #compute number of different routes
        self.graphDFS = defaultdict(list)

    def generateGraph(self, routes):

        for route in routes:

            start = route[0]
            end = route[1]
            weight = route[2]

            if start in self.graph:
                if end not in self.graph[start]:
                    town = Town(end)
                    desination = Destination(town, weight)
                    self.graph[start][end] = weight
                    self.graphP[start].append(desination)
                    self.graphDFS[start].append(town)
                else:
                    print("The route from", str(start), "to", str(end), "already exists.")
                    break
            else:
                self.initializeDestinationsGraph(start,end,weight)
                self.initializeDestinationsGraphP(start,end,weight)
                self.initializeDestinationsGraphDFS(start,end)
    
    def initializeDestinationsGraph(self, start, end, weight):
        dict_ = defaultdict(int)
        dict_[end] = weight
        self.graph[start] = dict_
        
    def initializeDestinationsGraphP(self, start, end, weight):
        self.graphP[start] = [Destination(end, weight)]

    def initializeDestinationsGraphDFS(self, start, neighborTown):
        self.graphDFS[start] = [Town(neighborTown)]

    def getGraph(self):
        return self.graph

    def getGraphP(self):
        return self.graphP

    def getGraphDFS(self):
        return self.graphDFS


