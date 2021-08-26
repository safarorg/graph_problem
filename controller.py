from classes import Candidate, Graph, Town
from collections import defaultdict

infinity = 9999999

class Controller:
    def __init__(self):
        self.graph_obj = Graph()

        self.graphLoaded = False
        self.startDijkstra = None
        self.wasDijkstraExecuted = False

        self.minimumWeight = defaultdict(int)
        self.predecessor = defaultdict(Town)
        self.candidates = set()
        self.visited = set()

        self.visitedDFS = defaultdict(bool)

    def start(self):
        pass
        #work in progress
    
    def computeDistanceAndValidate(self, inp):
        townsList = inp
        computedDistance = self.computeDistance(townsList)
        result = ''
        if computedDistance < 0:
            result = "NO SUCH ROUTE"
        else:
            result = str(computedDistance)

        return result
    
    def computeDistance(self, townsList):

        distance = 0
        for i in range(len(townsList)-1):
            if self.containsTown(townsList[i]) and self.containsDestinationTown(townsList[i], townsList[i+1]):
                distance += int(self.graph_obj.getGraph()[townsList[i]][townsList[i+1]])
            else:
                distance = -1
                break
        
        return distance

    def containsTown(self, town):
        return town in self.graph_obj.getGraph()

    def getTown(self, town):
        return self.graph_obj.getGraph()[town]

    def containsDestinationTown(self, townStart, townEnd):
        return townEnd in self.getTown(townStart)

    def numberDifferentRoutesAndValidate(self, inp):
        towns = inp
        start = Town(towns[0])
        end = Town(towns[1])

        return self.numberDifferentRoutes(start, end)
    
    def numberDifferentRoutes(self, start, destination):
        self.intializeDifferentRoutesStructures()
        result = 0
        if start.getName() in self.visitedDFS:
            result = self.numberDifferentRoutesRec(start, destination)
        
        return result


    def numberDifferentRoutesRec(self, current, destination):
        n = 0

        if current.getName() in self.visitedDFS:
            return 0
        
        if current.getName() == destination.getName():
            return 1

        self.visitedDFS[current.getName()] = True

        for neighbor in self.getNeighborTowns(current.getName()):
            n += self.numberDifferentRoutesRec(neighbor, destination)
        
        self.visitedDFS[current.getName()] = False
        return n

    def getNeighborTowns(self, town):
        return self.graph_obj.getGraphDFS[town]

    
    def intializeDifferentRoutesStructures(self):

        for k in self.graph_obj.getGraph():
            self.visitedDFS[k] = False
    
    def computeShortestRouteAndValidate(self, inp):

        towns = inp  #not sure if to use brackets
        start = Town(towns[0])
        end = Town(towns[1])

        if not self.wasDijkstraExecuted or (self.wasDijkstraExecuted and not self.isSameStartCity(start)):
            self.initializeStructuresDijkstra()
            self.computeShortestRoute(start)
            self.wasDijkstraExecuted = True
            self.startDijkstra = start
        
        return self.shortestRoute(start, end)

    def computeShortestRoute(self, start):

        self.minimumWeight[start.getName()] = 0

        while len(self.candidates) != 0:

            cand = self.getMinimumCand()

            self.candidates.remove(cand.getTown().getName())

            size = len(self.graph_obj.getGraphP()[cand.getTown().getName()])

            for i in range(size):
                neighbor = self.graph_obj.getGraphP()[cand.getTown().getName()][i]
                self.updateMinimumWeight(neighbor, cand)
            
            self.visited.add(cand.getTown().getName())


    def updateMinimumWeight(self, neighbor, cand):

        w  = self.minimumWeight[cand.getTown().getName()] + int(neighbor.getWeight())
        if w < self.minimumWeight[neighbor.getTown()]:
            self.minimumWeight[neighbor.getTown()] = w
            self.predecessor[neighbor.getTown()] = cand.getTown()
        
    
    def isSameStartCity(self, start):
        return self.startDijkstra.getName() == start.getName()

    
    def initializeStructuresDijkstra(self):
        self.minimumWeight = defaultdict(int)
        self.predecessor = defaultdict(Town)
        self.candidates = set()
        self.visited = set()

        for key in self.graph_obj.getGraphP():
            self.candidates.add(key)
        
        for k in self.candidates:
            self.minimumWeight[k] = infinity

        
    def getMinimumCand(self):
        minimum = infinity+1
        weight = infinity
        result = ''

        for cand in self.candidates:
            weight = self.minimumWeight[cand]
            if weight < minimum:
                result = cand
                minimum = weight

        return Candidate(Town(result), minimum)

    
    def shortestRoute(self, start, end):
        result = []
        predecessorTown = self.predecessor[end.getName()]
        result.append(end)

        if predecessorTown:
            result.append(predecessorTown)
            while predecessorTown.getName() != start.getName():
                predecessorTown = self.predecessor[predecessorTown.getName()]
                result.append(predecessorTown)

        return result

    def generateGraph(self, inp):
        return self.graph_obj.generateGraph(inp)

    def wasDijkstraExecuted(self):
        return self.wasDijkstraExecuted

    def setWasDijkstraExecuted(self, wasDijkstraExecuted):
        self.wasDijkstraExecuted = wasDijkstraExecuted
    

    def isGraphLoaded(self):
        return self.graphLoaded

    def setGraphLoaded(self, graphLoaded):
        self.graphLoaded = graphLoaded

    def getStartDijkstra(self):
        return self.startDijkstra

    def setStartDijkstra(self, startDijkstra):
        self.startDijkstra = startDijkstra