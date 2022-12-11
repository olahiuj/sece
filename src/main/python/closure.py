"""
This module provides closure for equivalence relations.
"""


class Closure:
    """equivalence relations closure"""
    def __init__(self, initial):
        self.__relations__ = set(initial)

    def transitive(self):
        """computes transitive closure

        Returns:
            Set[Tuple[Any, Any]]: set of related pairs
        """
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

    def add(self, elem1, elem2):
        """add related pair

        Args:
            elem1 (Any): the first related element
            elem2 (Any): the second related element
        """
        self.__relations__.add((elem1, elem2))
        self.__relations__.add((elem2, elem1))
        self.transitive()

    def contains(self, elem1, elem2):
        """check if the related pair is contained in closure

        Args:
            elem1 (Any): the first related element
            elem2 (Any): the second related element

        Returns:
            bool: if the related pair is contained in closure
        """
        return (elem1, elem2) in self.__relations__
