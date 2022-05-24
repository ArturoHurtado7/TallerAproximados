from vertex_cover import VertexCover
from graph import Graph
import sys, time

def main():
    args = sys.argv[1:]
    input_path = ''

    for i in range(0, len(args), 2):
        if args[i] == '-i' or args[i] == '--input':
            input_path = args[i+1]
        else:
            print(f'Error: Argumento "{args[i]}" inválido')
            exit(1)

    if not input_path:
        print('Error: Faltan argumentos, por favor ingrese -i o --input')
        exit(1)

    # Crea el grafo
    graph = Graph(input_path)
    print('solution type', graph.solution_type)

    # Crea el objeto VertexCover
    cover = VertexCover(graph.edges, graph.nodes)
    start = time.time()

    # Ejecuta el algoritmo de VertexCover con el tipo de solución especificado en el archivo de entrada
    if graph.solution_type == 1:
        vertices = cover.arbitrary_vertex_pick()
    elif graph.solution_type == 2:
        vertices = cover.high_degree_pick()
    elif graph.solution_type == 3:
        vertices = cover.arbitrary_vertex_degree()
    elif graph.solution_type == 4:
        vertices = cover.random_vertex_pick()

    # Imprime el resultado en el archivo de salida
    end = time.time()
    solution = graph.decode_nodes(vertices)
    print('output vertices', solution)
    print('output vertices size', len(solution))
    print(f'time elapsed: {end - start} seconds')


if __name__ == "__main__":
    main()
