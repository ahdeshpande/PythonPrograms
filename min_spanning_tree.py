def question3(graph):
    # Check if the type if input is graph
    if type(graph) is not dict:
        return "Invalid input! Input must be an adjacency matrix as a " \
               "dictionary!"

    # Check if the count of nodes is greater than 1
    if len(graph.items()) < 2:
        return "Cannot form an edge with just one vertex!"

    # Get all edges
    edges = set()
    for vertex, adjacent_vertices in graph.items():
        for adjacent_vertex in adjacent_vertices:
            # Add edge as [to, from, wt] where to is small than from
            if ord(vertex) < ord(adjacent_vertex[0]):
                edges.add((vertex, adjacent_vertex[0], adjacent_vertex[1]))
            else:
                edges.add((adjacent_vertex[0], vertex, adjacent_vertex[1]))

    # Sort all the edges on weights
    edges = sorted(edges, key=lambda x: x[2])

    print(edges)

    # Start creating a MST
    min_spanning_tree = {}

    for edge in edges:

        if edge[0] in min_spanning_tree.keys() and edge[1] in \
                min_spanning_tree.keys():
            pass
        else:
            if min_spanning_tree.get(edge[0]):
                min_spanning_tree[edge[0]].append(tuple((edge[1], edge[2])))
            else:
                min_spanning_tree[edge[0]] = [tuple((edge[1], edge[2]))]

            if min_spanning_tree.get(edge[1]):
                min_spanning_tree[edge[1]].append(tuple((edge[0], edge[2])))
            else:
                min_spanning_tree[edge[1]] = [tuple((edge[0], edge[2]))]

    print(min_spanning_tree)


G = {'A': [('B', 7), ('D', 5)],
     'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
     'C': [('B', 8), ('E', 5)],
     'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
     'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
     'F': [('D', 6), ('E', 8), ('G', 11)],
     'G': [('E', 9), ('F', 11)]}
question3(G)
