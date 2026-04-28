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

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertex in self:
            vertex.color = "white"
            vertex.previous = -1
        for vertex in self:
            if vertex.color == "white":
                self.dfs_visit(vertex)

    def dfs_visit(self, start_vertex):
        start_vertex.color = "gray"
        self.time = self.time + 1
        start_vertex.discovery_time = self.time
        for next_vertex in start_vertex.get_neighbors():
            if next_vertex.color == "white":
                next_vertex.previous = start_vertex
                self.dfs_visit(next_vertex)
        start_vertex.color = "black"
        self.time = self.time + 1
        start_vertex.closing_time = self.time

    def topological_sort(self):
        self.dfs()

        remaining = list(self.vertices.values())
        ordered = []

        while len(remaining) > 0:
            max_i = 0
            i = 1
            while i < len(remaining):
                if remaining[i].closing_time > remaining[max_i].closing_time:
                    max_i = i
                i += 1

            ordered.append(remaining[max_i].key)
            remaining.pop(max_i)

        return ordered
    
def create_graph():
    print('Reading input file "prereq.txt"...')

    try:
        text = open("./prereq.txt", "r")
    except FileNotFoundError:
        print("Error: prereq.txt does not exist or it can't be opened for input.")
        print("Program exiting now...")

    g = DFSGraph()
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
            
            course = current_line[0].rstrip(":")
            # verticies
            g.set_vertex(course)
            # edges
            if len(current_line) > 1:
                for prereq in current_line[1:]:
                    prereq = prereq.rstrip(":")
                    g.add_edge(prereq, course)

    return g


def main():
    print(
        "This program reads in a list of courses and prerequisites, and determines\n"
        "a valid ordering subject to prerequisite constraints via topological sort.\n"
    )

    g = create_graph()

    print("Performing topological sort...")

    ordered = g.topological_sort()

    print("Ordered list:")
    print(ordered)

if __name__ == "__main__":
    main()