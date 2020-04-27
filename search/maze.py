class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def containsState(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if(self.empty):
            raise Exception("empty frontier.")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[-1]
            return node


class QueueFrontier(StackFrontier):
    def remove(self):
        if(self.empty):
            raise Exception("empty frontier.")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
class Maze:
    def __init__(self, filename):
        with open(filename) as f : 
            contents = f.read()
        if contents.count("A")!=1:
             raise Exception("Maize must have exatly one start point.")
        if contents.count("B")!=1:
             raise Exception("Maize must have exatly one end point.")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height): 
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] ==  "A":
                        self.start = (i,j)
                        row.append(False)
                    elif contents[i][j] ==  "B":
                        self.start = (i,j)
                        row.append(False)
                     elif contents[i][j] ==  " ":
                         row.append(False)
                    else:
                        row.append(True)
                except IndexError: 
                        row.append(False)
            self.walls.append(row)
        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col :
                    print(" ", end = "")
                elif (i,j) == self.start:
                    print("A",end="")
                elif (i,j) == self.goal:
                    print("B",end="")
                elif solution is not None and (i,j) in solution:
                    print("*",end="")
                else:
                    print(" ", end="")
            print()
        print()