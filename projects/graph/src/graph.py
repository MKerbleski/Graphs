"""
Simple graph implementation compatible with BokehGraph class.
"""
import random
import math


class Queue: 
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if(self.size())>0:
            return self.queue.pop()
        else: 
            return None
    def size(self):
        return len(self.queue)

class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if(self.size()) > 0:
            return self.stack.pop(0)
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    # def add_vertex(self, v):
    #     self.vertices[v] = set()
    def add_vertex(self, v):
        self.vertices[v] = Vertex(v)
    def add_edge(self, v1, v2):
        self.vertices[v1].edges.add(v2)
        self.vertices[v2].edges.add(v1)
    def dfs_R(self, value, visited=None):
        if visited is None: 
            visited = []
        print(visited)
        visited.append(value)
        for vert in self.vertices:
            print(vert)
            if value == vert:
                print('true')
                return True 
            else:
                print(self.vertices[vert].edges, '26')
                for edge in self.vertices[vert].edges:
                    print(edge)
                    return self.dfs(edge, visited)
                # verts = self.vertices[vert].edges
                # print(verts, '28')
        return False 
    def bfs(self, value): 
        # do BfS 
        searched = []
        queue = [self.vertices[0]]
        return False
    def dfs(self, value):
        index = 0
        s = Stack()
        print(self.vertices[index].edges)
        k = list(self.vertices.keys())
        print(k,'k')
        s.push(k[0])
        print(s.stack,'s1')
        visited = []
        print(visited, 'visited')
        while  s.size() > 0:
            print(index, 'index', 'iteration')
            print(s.stack,'s2')
            node = s.pop()
            print(node,'node')
            if node == value:
                print('True')
                return True
            else: 
                visited.append(node)
                print(visited, 'visited')
                # print(self.vertices[index].edges,index,'edges')
                for each in self.vertices[index].edges:
                    if each not in visited:
                        print(each)
                        s.push(each)
                    else:
                        print('nope')
                index = index +1
        print('False')
        return False

class Vertex: 
    def __init__(self, vertex_id, x=None, y=None):
        self.id = vertex_id
        self.edges = set()
        if x is None: 
            self.x = math.floor(random.random() * 10 )+1
        else: 
            self.x = x
        if y is None: 
            self.y = math.floor(random.random() * 10)+1
        else:
            self.y = y
    def __repr__(self):
        return f"{self.edges}"

