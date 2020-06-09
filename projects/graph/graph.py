"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # add verts
        # set of edges from this vert
        self.vertices[vertex_id] = set()
        # a set is just like a list in python
        # except you can get O(1) look ups by id
        # just like a hashtable. And you cannot
        # have any duplicates


    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # when you add an edge between 2 verts
        # that means that we're gonna add one 
        # vertex id to the set of the source vertex.
        # so the destination vertex, v2, is added to
        # the set for v1

        # self.vertices[v1].add(v2)
        # .add() is a built in method on a set
        # v2 got added as a neighbor to v1.
        # [v1] gives us a O(1) lookup

        # fix to check that we are only connecting to 
        # verts that exist 
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            return IndexError("Vertex does not exist")




    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):

        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        q.enqueue(starting_vertex)


        # create an empty set to store visited vertices
        visited = set()

        # while the queue is not empty...
        while q.size() > 0:
            # dequeue the first vertex
            vertex = q.dequeue()

            # if that vertex hasn't been visited...
            if vertex not in visited:
                # visit it
                print(vertex)
                # and add to visited set
                visited.add(vertex)

                # then enqueue all it's neighbors
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # create empty stack, and push starting index/vertex
        s = Stack()
        s.push(starting_vertex)

        # create empty set to store visited verticies
        visited = set()

        # while stakc isn't empty
        while s.size() > 0:
            # pop off last vertex
            vertex = s.pop()

            # if vertex has not been visited
            if vertex not in visited:
                # visit it
                print(vertex)
                # and add it to the visited set
                visited.add(vertex)

                # then push all it's neighbors onto the stack
                for neighbor in self.get_neighbors(vertex):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited = {}
        # init visited hashtable to false for all verts
        for i in self.vertices:
            visited[i] = False

        def recurse(vert_id, visited):
            # traversal operation
            print(vert_id)
            # mark as visited
            visited[vert_id] = True

            # base case = everything has been visited already
            if False not in visited.values():
                return
            else:
                for neighbor in self.get_neighbors(vert_id):
                    # only recurse for unvisited verts
                    if visited[neighbor] == False:
                        recurse(neighbor, visited)

        # initial recursive call
        recurse(starting_vertex, visited)  


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
		# Create a Set to store visited vertices
        visited = set()
		# While the queue is not empty...
        while q.size() > 0:
			# Dequeue the first PATH
            path = q.dequeue()
			# Grab the last vertex from the PATH
            lastvertex = path[-1]
			# If that vertex has not been visited...
            if lastvertex not in visited:
				# CHECK IF IT'S THE TARGET
                if lastvertex == destination_vertex:
				  # IF SO, RETURN PATH
                  return path
				# Mark it as visited...
                visited.add(lastvertex)
				# Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(lastvertex):
				  # COPY THE PATH
                  copied_path = [*path]
				  # APPEND THE NEIGHOR TO THE BACK
                  copied_path.append(neighbor)
                  # Add list back inside queue
                  q.enqueue(copied_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # stacks
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            path = s.pop()
            lastvertex = path[-1]

            if lastvertex not in visited:
                if lastvertex == destination_vertex:
                    return path

                visited.add(lastvertex)

                for neighbor in self.get_neighbors(lastvertex):
                    copied_path = [*path]
                    copied_path.append(neighbor)
                    s.push(copied_path)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
