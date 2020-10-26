#Importing neccesarty libraries

import numpy as np
import random


# Add m mines to the grid

def add_mines(g, m):
    n = g.shape[0]
    l = [(random.randrange(0, d - 1), random.randrange(0, d - 1)) for i in range(m)]
    for i in l:
        g[i] = -1
    return g


# find if the adjacent cell is within dimensions
def check_dimentionality(adj, n):
    # Check if the adjacent value exixts in the grid.
    if adj[0] == -1 or adj[1] == -1 or adj[0] == n or adj[1] == n:
        return False
    else:
        return True


# Find no.of mines surrounding each cell.

def find_value(g, val):
    n = g.shape[0]
    c = 0
    i = val[0]
    j = val[1]
    adj = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
           (i + 1, j + 1)]
    for a in adj:
        if check_dimentionality(a, n):
            if g[a] == -1:
                c += 1
    return c


# Adding values to each cell in the grid

def add_values(g, n):
    for i in range(n):
        for j in range(n):
            if g[(i, j)] != -1:
                val = find_value(g, (i, j))
                g[(i, j)] = val
    return g


# Create a n*n grid with m mines

def create_grid(n, m):
    g = np.zeros((n, n))
    g = add_mines(g, m)
    g = add_values(g, n)
    return g

n = 5  # size of grid
m = 2  # number of mines

grid = create_grid(d, n)
print(grid)