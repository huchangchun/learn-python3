#coding:utf-8
"""
https://www.python-course.eu/graphs_python.php
A Python Class
A simple Python graph class,demonstrating the essential
facts and functionalities of graphs
"""
class Graph(object):
    def __init__(self,graph_dict = None):
        """
        initializes a graph object
        If no dictionary or None is given,
        an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict
        
    def vertices(self):
        """returns the vectices of a graph"""
        return list(self.__graph_dict.keys())
    def edges(self):
        """return the edges of a graph"""
        return self.__generate_edges()
    def __generate_edges(self):
        
        """"A Static method generating the edges of the graph ,Edges are represendted as sets with one or two vertices"""
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour,vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    def add_vertex(self, vertex):
        """If the vertex "vertex" is not in self.__graph_dict, a key "vertex" with an empty
        list as a value is added to the dictionary.
        Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
    def add_edge(self, edge):
        """
        assumes that edge is of type set ,tuple or list,
        between two vertices can be multiple edges!
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:  #如果存在key，则在对应的list中增加
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2] #否则生成新的key
    
    
    def __str__(self):
        res = "vertices:"
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges:"
        for edge in self.__generate_edges():
            res += str(edge)+" "
        return res

    def find_path(self,start_vertex,end_vertex,path=None):
        """
        (a, c, e) is a simple path in our graph, as well as (a,c,e,b). (a,c,e,b,c,d) is a path but not a simple path, because the node c appears twice. 
    
        """ 
        if path==None:
            path = []
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vectex in graph[start_vertex]:
            if vectex not in path:
                extend_path = self.find_path(vectex,end_vertex,path)
                if extend_path:
                    return extend_path
        return None
        
    
if __name__ == "__main__":
    
    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }    
    graph = Graph(g)
    print("Vertices of graph:")
    print(graph.vertices())
    
    print("Edges of graph")
    print(graph.edges())
    
    print("Add vertex")
    print(graph.add_vertex("z"))
    
    print("Vertices of graph:")
    print(graph.vertices())
    
    print("Edges of graph")
    print(graph.edges())
    
    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x","y"})
    
    print("vertices of graph:")
    print(graph.vertices())
    print("Edges of graph")
    print(graph.edges()) 
    print("find path")
    print(graph.find_path("c","e"))