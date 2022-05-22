
from random import randint
import csv, sys

def export_file(output: list, output_path: str) -> None:
    """
        Export the generated file to a csv file.
        :param output: The generated file.
        :param output_path: The path to the output file.
    """
    with open(output_path, 'w', encoding='UTF8', newline='') as f:
        write = csv.writer(f, delimiter = '\t')   
        write.writerows(output)


def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    limit, edges = (limit - 1), []
    nodes = set()
    cycles, cycles_limit = 0, (limit + 1) * (10 ** (len(str(limit)) - 4))
    while cycles < cycles_limit or len(nodes) < limit:
        node_a, node_b = randint(0, limit), randint(0, limit)
        while node_b == node_a: 
            node_b = randint(0, limit)
        edges.append([node_a, node_b]), edges.append([node_b, node_a])
        nodes.add(node_a), nodes.add(node_b)
        cycles += 1

    edges = sorted(edges)
    print('sored edges')
    edges = [edges[i] for i in range(1, len(edges)) if edges[i] != edges[i-1]]
    print('unique edges')
    export_file(edges, f'./data/input_{limit + 1}.csv')
    print('exported edges')

    print(cycles)
    print(len(edges))
    print(len(nodes))


if __name__ == "__main__":
    main()