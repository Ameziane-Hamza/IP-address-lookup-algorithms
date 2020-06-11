class Node:
    def __init__(self, addr=None):
        self.inter = None
        self.addr = addr
        self.route = None
        self.left = None
        self.right = None


class Creatarbre(Node):

    def __init__(self):
        self.root = Node("Empty")
        self.default = dict()

    def insert_default(self,addr,route,inter):
        self.default={
            "route": route,
            "destination": addr+"0.0.0.0/0",
            "interface": inter
        }

    numberOfNode = 1

    a = -1

    def insert(self, addr, route, inter):
        return self._insert(self.root, addr, route, inter)

    def _insert(self, noeud, addr, route, inter):
        self.a += 1
        if addr[self.a] == '0':
            if noeud.left == None:
                noeud.left = Node("Empty")
                self.numberOfNode += 1
            return self._insert(noeud.left, addr, route, inter)
        elif addr[self.a] == '1':
            if noeud.right == None:
                noeud.right = Node("Empty")
                self.numberOfNode += 1
            return self._insert(noeud.right, addr, route, inter)
        elif addr[self.a] == '*':
            noeud.addr = addr
            noeud.route = route
            noeud.inter = inter
            self.a = -1

    b = -1

    def lookup(self, addr):
        return self._lookup(self.root, addr)

    def _lookup(self, noeud, addr):
        self.b += 1
        if addr[self.b] == '0' and noeud.left != None:
            return self._lookup(noeud.left, addr)
        elif addr[self.b] == '1' and noeud.right != None:
            return self._lookup(noeud.right, addr)
        elif addr[self.b] == '*':
            self.b = -1
            if noeud.route == None:
                return self.default
            else:
                return {
                    "route": noeud.route,
                    "destination": noeud.addr,
                    "interface": noeud.inter
                }
        else:
            self.b = -1
            return self.default


