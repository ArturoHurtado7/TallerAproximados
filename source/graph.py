class Graph:

    def __init__(self, input) -> None:
        node_size = int(input.pop(0))
        self.edges = [int(i) for i in input]
