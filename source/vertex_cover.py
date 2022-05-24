
from random import randint

class VertexCover:

    def __init__(self, edges, vertices) -> None:
        """
            :param edges: lista de aristas
            :param vertices: lista de vertices
        """
        self.vertices = vertices
        self.edges = edges


    def arbitrary_vertex_pick(self) -> list:
        """
            - Escoger arbitrariamente un eje.
            - Incluir los dos vértices conectados.
            - Descartar todos los demás ejes conectados por los vertices escogidos.
            - Repetir hasta que no queden ejes.
        """
        vertices = []
        prime_edges = self.edges.copy()
        while prime_edges:
            edge = prime_edges.pop()
            vertices.append(edge[0]), vertices.append(edge[1])
            prime_edges = [e for e in prime_edges if e[0] != edge[0] and e[1] != edge[0] and e[0] != edge[1] and e[1] != edge[1]]
        vertices.sort()
        return vertices


    def high_degree_pick(self) -> list:
        """
            - Escoger el vértice de mayor grado.
            - Incluir el vértice seleccionado.
            - Descartar los ejes que llegan al vertie escogido.
            - Repetir hasta que no queden ejes.
        """
        vertices = []
        prime_edges = self.edges.copy()
        while prime_edges:
            vertex = self.higher_degree_vertex(prime_edges)
            vertices.append(vertex)
            prime_edges = [e for e in prime_edges if e[0] != vertex and e[1] != vertex]
        vertices.sort()
        return vertices


    def arbitrary_vertex_degree(self) -> list:
        """
            - Escoger arbitrariamente un eje.
            - Incluir el vértice de mayor grado de los dos vértices conectados por el eje.
            - Descartar todos los demás ejes conectados por el vértice escogido.
            - Repetir hasta que no queden ejes.
        """
        vertices = []
        prime_edges = self.edges.copy()
        while prime_edges:
            edge = prime_edges.pop()
            vertex = self.higher_degree_from_edge(prime_edges, edge)
            vertices.append(vertex)
            prime_edges = [e for e in prime_edges if e[0] != vertex and e[1] != vertex]
        vertices.sort()
        return vertices


    def random_vertex_pick(self) -> list:
        """
            - Escoger aleatoriamente un eje.
            - Incluir aleatoriamente uno de los dos vértices conectados.
            - Descartar todos los demás ejes conectados por el vértices escogido.
            - Repetir hasta que no queden ejes.
        """
        vertices = []
        prime_edges = self.edges.copy()
        while prime_edges:
            edge = prime_edges.pop(randint(0, len(prime_edges)-1))
            vertex = edge[randint(0, 1)]
            vertices.append(vertex)
            prime_edges = [e for e in prime_edges if e[0] != vertex and e[1] != vertex]
        vertices.sort()
        return vertices


    # *****************************************************************************
    # Funciones Auxiliares
    # *****************************************************************************

    def vertices_degree(self, edges: list) -> list:
        """
           :param vertices: lista de vertices
           :return: lista de grados de los vertices
        """
        degree = [0]*len(self.vertices)
        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        return degree


    def higher_degree_vertex(self, edges: list) -> list:
        """
           :param edges: lista de aristas
           :return: vertice con mayor grado
        """
        vertex, count = 0, 0
        vertices = self.vertices_degree(edges=edges)
        for index, degree in enumerate(vertices):
            if degree > count:
                vertex, count = index, degree
        return vertex


    def higher_degree_from_edge(self, edges: list, edge: list) -> list:
        """
           :param edges: lista de aristas
           :return: vertice con mayor grado de los dos vertices conectados por el eje
        """
        vertices = self.vertices_degree(edges=edges)
        vertex = edge[1]
        if vertices[edge[0]] > vertices[edge[1]]:
            vertex = edge[0]
        return vertex

