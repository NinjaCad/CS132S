"""
    To Do:

    1. Read all about Graphs and Depth First Search in Chapter 7
    2. Copy the full version of the Vertex code and the Graph code from Chapter 7.6
    3. Copy the DFSGraph code from Chapter 7.15
    5. Modify Vertex to add the three new instance variables described in Chapter 7.9, as well as the two new instance variables described in Chapter 7.15
    6. Write code to create a graph, with each node corresponding to a course, and each incoming edge corresponding to a prerequisite for that course
    7. Write code implementing the topological sort via depth-first search algorithm described in Chapter 7.17
    8. Write code to read the course prerequisite information from a file, create a corresponding graph, perform a topological sort, and output an ordering consistent with the prerequisite constraints
"""

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

        self.distance = 0
        self.previous = None
        self.color = "white"

        self.discovery_time = 0
        self.closing_time = 0

    def get_neighbor(self, other):
        return self.neighbors.get(other, None)

    def set_neighbor(self, other, weight=0):
        self.neighbors[other] = weight

    def __repr__(self):
        return f"Vertex({self.key})"

    def __str__(self):
        return (
            str(self.key)
            + " connected to: "
            + str([x.key for x in self.neighbors])
        )

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_key(self):
        return self.key
    
class Graph:
    def __init__(self):
        self.vertices = {}

    def set_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        return self.vertices.get(key, None)

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, from_vert, to_vert, weight=0):
        if from_vert not in self.vertices:
            self.set_vertex(from_vert)
        if to_vert not in self.vertices:
            self.set_vertex(to_vert)
        self.vertices[from_vert].set_neighbor(self.vertices[to_vert], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())
    
def create_graph():
    print('Reading input file "prereq.txt"...')

    try:
        text = open("./prereq.txt", "r")
    except FileNotFoundError:
        print("Error: prereq.txt does not exist or it can't be opened for input.")
        print("Program exiting now...")

    g = Graph()
    with open("./prereq.txt", "r") as infile:
        for line in infile:
            current_line = None
            line = line.strip()
            if not line:
                current_line = None
                continue
            else:
                print("Processing input file line->" + line)
                current_line = line.split()

            # verticies
            g.set_vertex(current_line[0])
            # edges
            if len(current_line) > 1:
                for prereq in current_line[1:]:
                    g.add_edge(current_line[0], prereq)

    return g


def main():
    g = create_graph()
    for v in g:
        print(v)

if __name__ == "__main__":
    main()