from vertex_cover import VertexCover
from graph import Graph
import sys, time

def main():
    args = sys.argv[1:]
    input_path = algorith = ''

    for i in range(0, len(args), 2):
        if args[i] == '-i' or args[i] == '--input':
            input_path = args[i+1]
        elif args[i] == '-a' or args[i] == '--algoritm':
            try:
                algorith = int(args[i+1])
            except:
                print('Error: invalid algorith')
                exit(1)
        else:
            print(f'Error: Argumento "{args[i]}" inválido')
            exit(1)

    if not input_path or not algorith:
        print('Error: Faltan argumentos, por favor ingrese -i o --input y -a o --algoritm')
        exit(1)

    # Crea el grafo
    graph = Graph(input_path)
    print('algorith', algorith)

    # Crea el objeto VertexCover
    cover = VertexCover(graph.edges, graph.nodes)
    start = time.time()

    # Ejecuta el algoritmo de VertexCover con el tipo de solución especificado en el archivo de entrada
    if algorith == 1:
        vertices = cover.arbitrary_vertex_pick()
    elif algorith == 2:
        vertices = cover.high_degree_pick()
    elif algorith == 3:
        vertices = cover.arbitrary_vertex_degree()
    elif algorith == 4:
        vertices = cover.random_vertex_pick()
    else:
        print('Error: Algoritmo inválido')
        exit(1)

    # Imprime el resultado en el archivo de salida
    end = time.time()
    solution = graph.decode_nodes(vertices)
    print('output vertices', solution)
    print('output vertices size', len(solution))
    print(f'time elapsed: {end - start} seconds')


if __name__ == "__main__":
    main()
