"""
I got this A* algorithm from geeksforgeeks.org. I changed added k to account for a 3_D plane.
My greatest concern is that the algorithm might think it can fly, when really I just want it to keep track of its current height so it knows if it's going up or down and account that in it's estimated cost.
It also needs  code to include the map Jonathan has made. It had code for a map, but it was 2-D.
Here: is the link to the website with the original code: https://www.geeksforgeeks.org/dsa/a-search-algorithm/
"""

import math
import heapq

# Define the Cell class
class Cell:
    def __init__(self):
        self.parent_i = 0  # Parent cell's row index
        self.parent_j = 0  # Parent cell's column index
        self.f = math.inf  # Total cost of the cell (g + h)
        self.g = math.inf  # Cost from start to this cell
        self.h = 0  # Heuristic cost from this cell to destination

# Check if a cell is valid (within the grid)
def is_valid(x, y, maxX, maxY):
    return (x >= 0) and (x < maxX) and (y >= 0) and (y < maxY)

# Check if a cell is the destination
def is_destination(x, y, dest):
    return x == dest[0] and y == dest[1]

def length3D(x, y, z):
    return math.sqrt(x*x + y*y + z*z)

def length2D(x, y):
    return math.sqrt(x*x + y*y)

def dist2D(a, b):
    return length2D(b[0] - a[0], b[1] - a[1])

# Calculate the heuristic value of a cell (3D Euclidean distance to destination)
def calculate_h_value(x, y, z, dest, destZ):
    return length3D(dest[0] - x, dest[1] - y, destZ - z)*1.5

def calculate_g_value(xSrc, ySrc, xDest, yDest, Z, get_coords):
    zdiff = Z[yDest][xDest] - Z[ySrc][xSrc]
    dist = dist2D(get_coords(xSrc, ySrc), get_coords(xDest, yDest))
    slope = abs(zdiff / dist)

    if zdiff > 0:
        # Going uphill
        return math.sqrt(1 + slope*slope) / dist
    else:
        return dist

# Trace the path from source to destination
def trace_path(cell_details, dest):
    path = []
    x = dest[0]
    y = dest[1]

    # Trace the path from destination to source using parent cells
    while not (cell_details[x][y].parent_i == x and cell_details[x][y].parent_j == y):
        path.append((x, y))
        temp_x = cell_details[x][y].parent_i
        temp_y = cell_details[x][y].parent_j
        x = temp_x
        y = temp_y

    # Add the source cell to the path
    path.append((x, y))
    # Reverse the path to get the path from source to destination
    path.reverse()

    return path


# Implement the A* search algorithm
def a_star_search(maxX, maxY, Z, src, dest, get_coords):
    # Check if the source and destination are valid
    if not is_valid(src[0], src[1], maxX, maxY) or not is_valid(dest[0], dest[1], maxX, maxY):
        print("Source or destination is invalid")
        return

    # Check if we are already at the destination
    if is_destination(src[0], src[1], dest):
        print("We are already at the destination")
        return

    # Initialize the details of each cell
    cell_details = [[Cell() for _ in range(maxY)] for _ in range(maxX)]

    # Initialize the start cell details
    i = src[0]
    j = src[1]
    cell_details[i][j].f = 0
    cell_details[i][j].g = 0
    cell_details[i][j].h = 0
    cell_details[i][j].parent_i = i
    cell_details[i][j].parent_j = j

    destZ = Z[dest[1]][dest[0]]

    # Initialize the open list (cells to be visited) with the start cell
    open_list = []
    heapq.heappush(open_list, (0.0, i, j))  # (f, row, col)

    # Initialize the flag for whether destination is found
    found_dest = False

    # Main loop of A* search algorithm
    while len(open_list) > 0:
        # Pop the cell with the smallest f value from the open list
        p = heapq.heappop(open_list)

        i = p[1]
        j = p[2]
        curr_details = cell_details[i][j]
        curr_g = curr_details.g

        # For each direction, check the successors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0),
                      (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dir in directions:
            new_i = i + dir[0]
            new_j = j + dir[1]

            if not is_valid(new_i, new_j, maxX, maxY):
                continue
            # If the successor is valid
            successor = cell_details[new_i][new_j]

            # If the successor is the destination
            if is_destination(new_i, new_j, dest):
                # Set the parent of the destination cell
                successor.parent_i = i
                successor.parent_j = j
                # Trace the path from source to destination
                found_dest = True
                return trace_path(cell_details, dest)
            else:
                # Calculate the new f, g, and h values
                g_new = curr_g + calculate_g_value(i, j, new_i, new_j, Z, get_coords)
                h_new = calculate_h_value(new_i, new_j, Z[new_j][new_i], dest, destZ)
                f_new = g_new + h_new

                # If the new f value is smaller
                if successor.f > f_new:
                    # Add the cell to the open list if it is not already present
                    if successor not in open_list:
                        heapq.heappush(open_list, (f_new, new_i, new_j))

                    # Update the cell details
                    successor.f = f_new
                    successor.g = g_new
                    successor.h = h_new
                    successor.parent_i = i
                    successor.parent_j = j

    # If the destination is not found after visiting all cells
    if not found_dest:
        print("Failed to find the destination cell")

