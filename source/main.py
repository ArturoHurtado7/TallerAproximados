from vertex_cover import VertexCover
from graph import Graph
import sys

def main():
    args = sys.argv[1:]
    input_path = output_path = ''

    for i in range(0, len(args), 2):
        if args[i] == '-i' or args[i] == '--input':
            input_path = args[i + 1]
        elif args[i] == '-o' or args[i] == '--output':
            output_path = args[i + 1]
        else:
            print(f'Error: Argumento "{args[i]}" inválido')
            exit(1)
    
    if input_path == '' or output_path == '':
        print('Error: Faltan argumentos, por favor ingrese -i o --input y -o o --output')
        exit(1)

    # Crea el grafo
    graph = Graph(input_path)
    # Crea el objeto VertexCover
    print('graph.solution_type', graph.solution_type)
    cover = VertexCover(graph.edges, graph.nodes)
    # Ejecuta el algoritmo de VertexCover con el tipo de solución especificado en el archivo de entrada
    if graph.solution_type == 1:
        vertices = cover.arbitrary_vertex_pick()
    elif graph.solution_type == 2:
        vertices = cover.high_degree_pick()
    elif graph.solution_type == 3:
        vertices = cover.arbitrary_vertex_degree()
    elif graph.solution_type == 4:
        print('random_vertex_pick')
        vertices = cover.random_vertex_pick()

    # Imprime el resultado en el archivo de salida
    solution = graph.decode_nodes(vertices)
    input_vertices = graph.decode_nodes(graph.nodes)
    input_edges = graph.decode_edges(graph.edges)

    print('solution type', graph.solution_type)
    print('input edges', input_edges)
    print('input vertices', input_vertices)
    print('input vertices size', len(input_vertices))
    print('output vertices', solution)
    print('output vertices size', len(solution))


if __name__ == "__main__":
    main()