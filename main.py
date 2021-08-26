
from controller import Controller

def main():
    c = Controller()
    graph_string = 'AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'
    graph = graph_string.replace(' ', '').split(',')
    # initial_command = input()
    # if initial_command == '2':
    c.generateGraph(graph)
    c.setGraphLoaded(True)
    print('The graph have been generated successfully')
    command = '6'
    if command == '4':
        if c.isGraphLoaded():
            # route_string = input()
            route_string = 'A-E-D'
            route = route_string.replace(' ', '').split('-')
            result = c.computeDistanceAndValidate(route)
            print(result)
        else:
            print('First you need to load the graph')
    if command == '5':
        if c.isGraphLoaded():
            print("Please introduce the start town and destination town to calculate the number of routes: ")
            start_end_string = 'C,C'
            start_end = start_end_string.replace(' ', '').split(',')
            result = c.numberDifferentRoutesAndValidate(start_end)
            print(result)
        else:
            print('First you need to load the graph')
    if command == '6':
        if c.isGraphLoaded():
            print('Please introduce the start town and destination town to calculate the shortest route:')
            start_end_string = 'B, B'
            start_end = start_end_string.replace(' ', '').split(',')
            result = c.computeShortestRouteAndValidate(start_end)
            for i in result:
                print(i.getName())
        else:
            print('First you need to load the graph')




if __name__ == '__main__':
    main()


# 4. Calculate distance along route
# 5. Number of different routes between two towns
# 6. Shortest route between two towns