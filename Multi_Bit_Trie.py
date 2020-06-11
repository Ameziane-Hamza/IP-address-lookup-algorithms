#########Multi-Bit Trie####################
##########cette classe signifie un noeud dans l'arbre###########################
class Node():
    "Un noeud de l'arbre"
    def __init__(self,data):
        self.data=data
        self.inter=None
        self.route=None
        self._00=None
        self._01=None
        self._10=None
        self._11=None
##########cette classe signifie le noeud#########################
class Arbre(Node):
    "Arbre"
    def __init__(self):
        self.root=Node("Empty")
        self.default=dict()

    def insert_default(self,valeur,inter,route):
        self.default={
            "route": route,
            "destination": valeur+"0.0.0.0/0",
            "interface": inter
        }


    def insert(self,valeur,inter,route):
        return self._insert_(valeur,inter,route,self.root)

    a=-2
    def _insert_(self,valeur,inter,route,curr_node):
        self.a+=2
        if valeur[self.a:(self.a+2)]=='00':
            if curr_node._00==None:
                curr_node._00 = Node("Empty")
            return self._insert_(valeur,inter,route,curr_node._00)

        elif valeur[self.a:(self.a+2)]=='01':
            if curr_node._01==None:
                curr_node._01 = Node("Empty")
            return self._insert_(valeur,inter,route,curr_node._01)

        elif valeur[self.a:(self.a+2)]=='10':
            if curr_node._10==None:
                curr_node._10 = Node("Empty")
            return self._insert_(valeur,inter,route,curr_node._10)

        elif valeur[self.a:(self.a+2)]=='11':
            if curr_node._11==None:
                curr_node._11 = Node("Empty")
            return self._insert_(valeur,inter,route,curr_node._11)

        elif valeur[self.a]=='*':
            if curr_node.data != "Empty":
                if curr_node.inter.find(inter[1]) == -1:
                    curr_node.inter += " | " + inter
                curr_node.route+=" | "+ route
            else:
                curr_node.data = valeur
                curr_node.inter = inter
                curr_node.route = route
            self.a=-2
        ########Si longueurs de préfixe qui ne sont pas un multiple de 2 doivent être élargis
        elif valeur[self.a+1]=='*':
            v_0 = valeur[:len(valeur) - 1] + "0*"
            v_1 = valeur[:len(valeur) - 1] + "1*"
            self.a-=2
            return self._insert_(v_0,inter,route,curr_node),self._insert_(v_1,inter,route,curr_node)


    def find(self,valeur):
        return self._find_(valeur,self.root)
    b=-2
    def _find_(self,valeur,curr_node):
        ### ajout de l'etoil pour simplifier la recherche
        if self.b==-2:
            if valeur[-1]!="*":
                valeur+="*"
        self.b+=2
        if valeur[self.b:(self.b+2)]=='00'and curr_node._00!=None:
            return self._find_(valeur,curr_node._00)
        elif valeur[self.b:(self.b+2)]=='01'and curr_node._01!=None:
            return self._find_(valeur,curr_node._01)
        elif valeur[self.b:(self.b+2)]=='10'and curr_node._10!=None:
            return self._find_(valeur,curr_node._10)
        elif valeur[self.b:(self.b+2)]=='11'and curr_node._11!=None:
            return self._find_(valeur,curr_node._11)

        elif valeur[self.b]=='*':
            self.b=-2
            if curr_node.route == None:
                return self.default
            else:
                return {
                    "route": curr_node.route,
                    "destination": curr_node.data,
                    "interface": curr_node.inter
                }

        ########Si longueurs de préfixe qui ne sont pas un multiple de 2 doivent être élargis
        elif valeur[self.b+1] =='*':
            v_0 = valeur[:len(valeur) - 1] + '0*'
            v_1 = valeur[:len(valeur) - 1] + '1*'
            self.b -= 2
            return self._find_(v_0,curr_node) , self._find_(v_1,curr_node)
        else:
            self.b=-2
            return self.default
