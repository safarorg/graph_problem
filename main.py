
from controller import Controller

def main():
    print('Please enter the input graph data separated by commas:')
    # route_information = input()
    route_information = 'AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7'
    route = route_information.replace(' ', '').split(',')
    c = Controller()
    c.generateGraph(route)
    c.setGraphLoaded(True)
    print('hello')

if __name__ == '__main__':
    main()