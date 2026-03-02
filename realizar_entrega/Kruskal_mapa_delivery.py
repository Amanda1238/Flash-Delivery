#  auxiliar kruskal

class UnionFind:
    def __init__(self, vertices):
        self.pai = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.pai[v] != v:
            self.pai[v] = self.find(self.pai[v])
        return self.pai[v]

    def union(self, v1, v2):
        r1 = self.find(v1)
        r2 = self.find(v2)

        if r1 == r2:
            return False

        if self.rank[r1] < self.rank[r2]:
            self.pai[r1] = r2
        elif self.rank[r1] > self.rank[r2]:
            self.pai[r2] = r1
        else:
            self.pai[r2] = r1
            self.rank[r1] += 1

        return True


# Desenha a mapa do caminho (KRUSKAL)
def kruskal_cidade(listaAdj):

    vertices = list(listaAdj.keys())
    arestas = set()

    for u in listaAdj:
        for v, peso in listaAdj[u]:
            aresta = tuple(sorted([u, v])) + (peso,)
            arestas.add(aresta)

    arestas_ordenadas = [(peso, u, v) for u, v, peso in arestas]
    arestas_ordenadas.sort()

    uf = UnionFind(vertices)
    mst = {}

    for peso, u, v in arestas_ordenadas:
        if uf.union(u, v):
            mst.setdefault(u, []).append((v, peso))
            mst.setdefault(v, []).append((u, peso))

    return mst
