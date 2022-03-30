# Graph using adjacency Matrix

class Graph:
    def __init__(self, numVertex):
        self.adjMatrix = [[-1]*numVertex for x in range(numVertex)]
        self.numVertex = numVertex
        self.vertices = {}
        self.verticeslist = [0]*numVertex

    def set_vertex(self, vtx, id):
        if 0 <= vtx <= self.numVertex:
            self.vertices[id] = vtx
            self.verticeslist[vtx] = id

    def set_edge(self, frm, to):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to] = 0
        self.adjMatrix[to][frm] = 0

    def get_vertex(self):
        return self.verticeslist

    def get_edges(self):
        edges= []
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if  self.adjMatrix[i][j] != -1:
                    edges.append(self.verticeslist[i], self.verticeslist)


