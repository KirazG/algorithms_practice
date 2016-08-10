# Use Karger's randomized algorithm to count the number of crossing edges
# in a minimum cut of a given graph

# This program takes as input an adjacency list representation of an
# undirected graph that lists each node and then all nodes that it connects to.

import pandas as pd
import numpy as np
import random

# each row has a different length
# max length is 41
# cannot read directly into array

g = np.zeros([0,2])

with open('kargermincut.txt') as f:
    for line in f:

        # save each edge as a row in g
        # each edge goes from the first node in line to one of the others
        # don't worry about saving the vertices

        nodes = line.split('\t')
        node1 = nodes.pop(0)
        # Save each edge to array g
        for node in nodes[:-1]:
            # every edge is repeated twice since graph is nondirected
            # only save edges where leading node < following node
            if node < node1:
                g = np.vstack((g,[node1, node]))

# reserve original graph G
G = pd.DataFrame(g, columns=['v0', 'v1'])

# Save number of crossing edges in each iteration
crossings = []

def min_cut(g):

    global n

    # check if we are down to last 2 nodes
    if n == 2:

        return g.shape[0]

    # Pick an edge uniformly at random
    # Save vertices and delete edge from graph
    edge = random.choice(g.index)
    v0 = g.ix[edge,'v0']
    v1 = g.ix[edge,'v1']

    g.drop(edge, axis=0, inplace=True)

    # replace all instances of v1 with v0 in g
    g.replace(v1, v0, inplace=True)
    # print number of UNIQUE nodes remaining in g
    print g.v0.value_counts().shape

    # remove all self-looping edges
    g = g[g.v0!=g.v1]

    # decrement counter
    n += -1
    print n
    # make recursive call
    return min_cut(g)

for i in range(100):
    # save number of nodes
    # since we do not need to return the nodes in each cut
    # we will not track the individual nodes
    # we will decrement counter to track nodes remaining in graph
    n = 200
    # reserve original graph G
    # manipulate values of g
    g = G.copy()
    crossings.append(min_cut(g))


print crossings
print min(crossings)
