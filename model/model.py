import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getAllProducts()
        self._idMap = {}
        for el in self._nodes:
            self._idMap[el.Product_number] = el

    def get_colori(self):
        return DAO.get_colori()

    def buildgraph(self, color, anno):
        #self._graph.clear()
        self._nodes = DAO.getAllNodesFromColor(color)
        self._graph.add_nodes_from(self._nodes)
        self.getAllEdges(int(anno), color)


    def getAllEdges(self, anno, colore):
        allEdges = DAO.getAllEdges(anno,colore)
        for e in allEdges:
            self._graph.add_edge(self._idMap[e[0]], self._idMap[e[1]], weight=e[2])

    def getNumNodi(self):
        return len(self._graph.nodes)

    def getNumArchi(self):
        return len(self._graph.edges)

    def getArchiGraficoMigliori(self):
        archi =  self._graph.edges
        print(archi)

