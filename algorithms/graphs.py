from collections import deque

class Node(object):
    adjacent = []

    def __init__(self, id):
        self.id = id

    def add(self, node):
        self.adjacent.append(node)

    def __str__(self):
        return str(self.id)


class Graph(object):
    @classmethod
    def hasPathDFS(cls, source, destination):
        s = Node(source)
        d = Node(destination)
        visited = set()
        return cls._hasPathDFS(s, d, visited)

    @classmethod
    def _hasPathDFS(cls, source, destination, visited):
        if (source.id == destination.id):
            return True

        if (source.id in visited):
            return False
        visited.add(source.id)

        for child in source.adjacent:
            if cls._hasPathDFS(child, destination, visited):
                return True

        return False

    @classmethod
    def hasPathBFS(cls, source, destination):
        queue = deque()
        s = Node(source)
        queue.append(s)
        visited = set()
        d = Node(destination)

        while (queue):
            node = queue.popleft()
            if node.id in visited:
                continue
            visited.add(node.id)
            if (node.id == d.id):
                return True

            for child in node.adjacent:
                queue.append(child)

        return False


if __name__ == "__main__":
    nodeA = Node(1)
    nodeA.add(Node(3))
    nodeA.add(Node(4))
    nodeB = Node(10)
    nodeB.add(nodeA)

    assert Graph.hasPathDFS(1, 3)
    assert Graph.hasPathDFS(10, 1)
    assert Graph.hasPathDFS(3, 10) == False

    assert Graph.hasPathBFS(1, 3)
    assert Graph.hasPathBFS(10, 1)
    assert Graph.hasPathBFS(3, 10) == False
