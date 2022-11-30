class Closure:
    def __init__(self, initial):
        self.__relations__ = set(initial)

    def transitive(self):
        closure = set(self.__relations__)
        while True:
            new_relations = set(
                (x, z)
                for (x, y1) in closure
                for (y2, z) in closure
                if y1 == y2
            )
            if new_relations.issubset(closure):
                self.__relations__ = closure
                return None

            closure = new_relations | closure

    def add(self, x, y):
        self.__relations__.add((x, y))
        self.__relations__.add((y, x))
        self.transitive()

    def contains(self, x, y):
        return (x, y) in self.__relations__

