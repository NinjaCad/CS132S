"""
    Deliverable: Homework09.py


    References:

        https://runestone.academy/runestone/books/published/pythonds3/Graphs/toctree.htmlLinks to an external site.
        (Sections 7.1-7.10)
    

    Sample Input/Output:

        >>> 
        RESTART: /Users/jeickemeyer/TMU/Courses/CS132S/_key/Homework09.py 

        Welcome to Flipper!  

        You begin with nine coins, showing "heads", arranged in a 3x3 grid:

        HHH    123
        HHH    456  <= Coin Choice Options 1-9
        HHH    789

        Choose a coin to flip it over, along with those vertically and 
        horizontally adjacent.

        The object of the game is to end up with all coins showing "tails".

        If you are stuck, choose Option 0 to show the solution.  :)


        HHH
        HHH
        HHH

        Option 0: Solve; Options 1-9: Choose Node
        Node 0 (000000000)
        Node 0 connectedTo: [11, 23, 38, 89, 186, 200, 308, 416, 464]

        Choose Option 0-9: 2

        TTT
        HTH
        HHH

        Option 0: Solve; Options 1-9: Choose Node
        Node 23 (000010111)
        Node 23 connectedTo: [0, 28, 49, 78, 173, 223, 291, 439, 455]

        Choose Option 0-9: 7

        TTT
        TTH
        TTH

        Option 0: Solve; Options 1-9: Choose Node
        Node 223 (011011111)
        Node 223 connectedTo: [23, 101, 134, 200, 212, 249, 271, 383, 491]

        Choose Option 0-9: 5

        THT
        HHT
        THH

        Option 0: Solve; Options 1-9: Choose Node
        Node 101 (001100101)
        Node 101 connectedTo: [60, 67, 110, 114, 173, 223, 337, 437, 453]

        Choose Option 0-9: 0

        THT
        HHT
        THH

        Computer Chooses Option 3:

        TTH
        HHH
        THH

        Computer Chooses Option 1:

        HHH
        THH
        THH

        Computer Chooses Option 2:

        TTT
        TTH
        THH

        Computer Chooses Option 9:

        TTT
        TTT
        TTT

        Success!  :)
        >>>
    

    To Do:

        1. Read all about Graphs and Breadth First Search in Chapter 7
        2. Copy the full version of the Queue code from Chapter 3.12
        3. Copy the full version of the Vertex code and the Graph code from Chapter 7.6
        4. Copy the bfs() function from Chapter 7.9
        5. Modify Vertex to add the three new instance variables described in Chapter 7.9
        6. Write code to create a graph, with each node corresponding to a possible configuration of the board, and each edge corresponding to a single legal move from one possible board configuration to another
        7. Write code to find the shortest path from any board configuration to the desired end board configuration via breadth-first search
        8. Write code to display the initial board, Node 0, ("000000000" in binary), with "1" in the ith least significant bit corresponding to the ith coin showing "tails"
        9. Write code to accept user moves "1"-"9", corresponding to flipping one of the nine coins, plus coins vertically and horizontally adjacent
        10. Write code to accept user move "0", corresponding to a command to display the shortest path from the current board configuration to the desired end board configuration, Node 511 ("111111111" in binary)
        11. Start early, work diligently, and ask me if you have any questions
        12. Submit the completed code via Canvas
    

    100	CS132S Rubric HW09:
        4	Use Queue, Vertex, Graph, bfs() code from textbook
        12	Modify Vertex to add instance variables distance, predecessor, color 
        12	Create Graph w/Node=board configuration, Edge=single legal move to new configuration
        12	Find shortest path from any board configuration to end goal via bfs
        12	Display initial board
        12	Change configuration via user moves
        12	Show solution via option 0
        4	Readability
        20	Quality of Solution
"""

class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)

class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        
        self.distance = 0
        self.previous = None
        self.color = "white"

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

def bfs(start):
    start.distance = 0
    start.previous = None
    vert_queue = Queue()
    vert_queue.enqueue(start)
    while vert_queue.size() > 0:
        current = vert_queue.dequeue()
        for neighbor in current.get_neighbors():
            if neighbor.color == "white":
                neighbor.color = "gray"
                neighbor.distance = current.distance + 1
                neighbor.previous = current
                vert_queue.enqueue(neighbor)
        current.color = "black"

def update_table(state, move):
    #   8 7 6
    #   5 4 3
    #   2 1 0
    binary = list(format(state, "09b"))
    if move == 9:
        flip(binary, 0)
        flip(binary, 1)
        flip(binary, 3)
    elif move == 8:
        flip(binary, 0)
        flip(binary, 1)
        flip(binary, 2)
        flip(binary, 4)
    elif move == 7:
        flip(binary, 1)
        flip(binary, 2)
        flip(binary, 5)
    elif move == 6:
        flip(binary, 0)
        flip(binary, 3)
        flip(binary, 4)
        flip(binary, 6)
    elif move == 5:
        flip(binary, 1)
        flip(binary, 3)
        flip(binary, 4)
        flip(binary, 5)
        flip(binary, 7)
    elif move == 4:
        flip(binary, 2)
        flip(binary, 4)
        flip(binary, 5)
        flip(binary, 8)
    elif move == 3:
        flip(binary, 3)
        flip(binary, 6)
        flip(binary, 7)
    elif move == 2:
        flip(binary, 4)
        flip(binary, 6)
        flip(binary, 7)
        flip(binary, 8)
    elif move == 1:
        flip(binary, 5)
        flip(binary, 7)
        flip(binary, 8)
    return int(''.join(binary), 2)

def create_graph():
    g = Graph()
    for i in range(512):
        g.set_vertex(i)
    for i in range(512):
        for move in range(1, 10):
            g.add_edge(i, update_table(i, move))
    return g

def flip(node, spot):
    node[spot] = "1" if node[spot] == "0" else "0"

def display(node):
    display_list = []
    for n in node:
        if n == "1":
            display_list.append("T")
        if n == "0":
            display_list.append("H")
    return f"{display_list[8]}{display_list[7]}{display_list[6]}\n{display_list[5]}{display_list[4]}{display_list[3]}\n{display_list[2]}{display_list[1]}{display_list[0]}"

def solve(g, start):
    bfs(g.get_vertex(start))
    path = []
    cur = g.get_vertex(511)
    while cur is not None:
        path.append(cur.key)
        cur = cur.previous
    path.reverse()
    return path

def find_move(old, new):
    for move in range(1, 10):
        if update_table(old, move) == new:
            return move
    return None

def main():
    print("\nWelcome to Flipper!\n")
    print('You begin with nine coins, showing "heads", arranged in a 3x3 grid:\n')
    print("HHH    123")
    print("HHH    456  <= Coin Choice Options 1-9")
    print("HHH    789\n")
    print("Choose a coin to flip it over, along with those vertically and horizontally adjacent.\n")
    print('The object of the game is to end up with all coins showing "tails".\n')
    print("If you are stuck, choose Option 0 to show the solution.  :)\n\n")

    g = create_graph()
    state = 0

    while True:
        binary = format(state, "09b")
        print(display(binary))
        print()
        print("Option 0: Solve; Options 1-9: Choose Node")
        print(f"Node {g.get_vertex(state).key} ({binary})")
        print(f"Node {g.get_vertex(state)}")

        answer = int(input("\nChoose Option 0-9: ").strip())
        if answer not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("\nPlease enter a number from 0 to 9.\n")
            continue
        
        if answer == 0:
            path = solve(g, state)
            cur = path[0]
            for node in path[1:]:
                move = find_move(cur, node)
                print(f"\nComputer Chooses Option {move}:\n")
                binary = format(node, "09b")
                print(display(binary))
                cur = node

            print("\nSuccess!  :)")
            break

        state = update_table(state, answer)

        if state == 511:
            print("Success!  :)")
            break

if __name__ == "__main__":
    main()