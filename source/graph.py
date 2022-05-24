
class Graph:

    def __init__(self, input_path: str) -> None:
        """
            :param input_path: ruta del archivo de entrada
            :return: None
            inicializa el grafo
        """
        try:
            input_file = open(input_path, "r") 
            text = input_file.read()
            rows = text.split('\n')
            self.old_edges, self.old_nodes = self.original_graph(rows)
            self.edges = self.coded_graph(self.old_edges, self.old_nodes)
            self.nodes = [i for i in range(len(self.old_nodes))]
        except Exception as e:
            print('Error: ', e)
            exit(1)


    def original_graph(self, rows: list) -> list:
        """
            :param rows: lista de filas del archivo de entrada
            :return: retorna el grafo original
        """
        nodes = set()
        edges = []
        for row in rows:
            node_a, node_b = self.row_items(row)
            nodes.add(node_a), nodes.add(node_b)
            edges.append([int(node_a), int(node_b)])
        nodes = list(nodes)
        return edges, nodes


    def coded_graph(self, edges: list, nodes: list) -> list:
        """
            :param edges: lista de aristas del grafo original
            :param nodes: lista de nodos del grafo original
            :return: lista de aristas del grafo codificado
        """
        new_edges = []
        # coded nodes by index position in the node list
        for u,v in edges:
            new_u, new_v = nodes.index(u), nodes.index(v)
            new_edges.append([new_u, new_v])
        # return the coded edges
        return new_edges


    def decode_edges(self, edges: list) -> list:
        """
            :param edges: lista de aristas codificadas
            :return: lista de aristas decodificadas
        """
        old_edges = []
        for u,v in edges:
            old_edges.append([self.old_nodes[u], self.old_nodes[v]])
        return old_edges


    def decode_nodes(self, nodes: list) -> list:
        """
            :param nodes: lista de nodos codificados
            :return: lista de nodos decodificados
        """
        old_nodes = []
        for node in nodes:
            old_nodes.append(self.old_nodes[node])
        return old_nodes


    def row_items(self, text: str) -> list:
        """
            :param text: linea de texto del archivo de entrada
            retorna los valores de la fila
        """
        text = ' '.join(text.split())
        text = text.replace('\t', ',').replace(';', ',').replace('|', ',').replace(' ', ',').replace('\n', '')
        item = text.split(',')
        return [int(item[0]), int(item[1])]

