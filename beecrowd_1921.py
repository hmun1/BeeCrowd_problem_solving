def graph_kite(vertices):
    edges = (vertices * (vertices - 1)) / 2 - vertices     # for a kite graph with n vertices, the number of total edges (n*(n-1))/2 -n
    print(f'{edges:.0f}')

# read input
vertices = int(input())
if 3 <= vertices <= 100000:    # input valid or not?
    graph_kite(vertices)       # call and execute the program