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

    # Start creating a MST
    min_spanning_tree = {}

    # A forest consisting of trees with single nodes is initialized. Each
    # tree is represented in a different number.
    tree = {}
    index = 1
    for i in G.keys():
        tree[i] = index
        index += 1

    for edge in edges:

        # If this edge is connecting two vertices which belong to the same
        # tree (having the same number), then it is ignored. Adding such an
        # edge to the result would form a cycle.

        if len(set(tree.values())) == 1:
            break

        elif tree[edge[0]] is not tree[edge[1]]:
            value_list = [tree[edge[1]], tree[edge[0]]]
            for key, value in tree.items():
                if value in value_list:
                    tree[key] = tree[edge[0]]

            # Create an adjacency matrix
            if min_spanning_tree.get(edge[0]):
                min_spanning_tree[edge[0]].append(tuple((edge[1], edge[2])))
            else:
                min_spanning_tree[edge[0]] = [tuple((edge[1], edge[2]))]

            if min_spanning_tree.get(edge[1]):
                min_spanning_tree[edge[1]].append(tuple((edge[0], edge[2])))
            else:
                min_spanning_tree[edge[1]] = [tuple((edge[0], edge[2]))]

    print(min_spanning_tree)


# Algorithm and example referred from
# https://www-m9.ma.tum.de/graph-algorithms/mst-kruskal/index_en.html
G = {'A': [('I', 464), ('F', 343), ('H', 1435)],
     'B': [('F', 879), ('H', 811), ('G', 954), ('J', 524)],
     'C': [('F', 1054), ('E', 1364)],
     'D': [('G', 433), ('J', 1053)],
     'E': [('C', 1364), ('F', 1106), ('J', 766)],
     'F': [('A', 343), ('G', 1054), ('B', 879), ('E', 1106)],
     'G': [('H', 837), ('B', 954), ('D', 433)],
     'H': [('A', 1435), ('B', 811), ('G', 837)],
     'I': [('A', 464)],
     'J': [('B', 524), ('D', 1053), ('E', 766)]}
question3(G)
