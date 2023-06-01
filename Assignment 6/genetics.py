import numpy as np
from heapq import *

nV = input("Enter the number of words in vocalbulary: ")
V = input("Enter the words in vocalbulary in UPPER CASE: ")
K = int(input("Enter the number of strings: "))
# for loop to input the strings in a list
S = []
for _ in range(K):
    S.append(input)
    
CC = int(input("Enter the conversion cost: "))

def match_cost():
    # for loop to input the match cost as matrix
    MC = []
    for _ in range(nV+1):
        for _ in range(nV+1):
            MC.append(input)
    return MC

class Node:
    def __init__(self, word, cost, parent):
        self.word = word
        self.cost = cost
        self.parent = parent

class node:
    def __init__(self, str1, str2, parent, cost, pos) -> Node:
        self.str1 = str1
        self.str2 = str2
        self.parent = parent
        self.cost = cost
        self.pos = pos
        
    def __lt__(self, nxt):
        return self.cost < nxt.cost

    def matrix(node):
        # for loop to create the matrix
        matrix = []
        for i in range(len(node.str1)+1):
            matrix.append([])
            for j in range(len(node.str2)+1):
                matrix[i].append(0)
        return matrix
    
    def fill_matrix(node, matrix, MC):
        for i in range(1, len(node.str1)+1):
            matrix[i][0] = matrix[i-1][0] + CC
        for j in range(1, len(node.str2)+1):
            matrix[0][j] = matrix[0][j-1] + CC
        for i in range(1, len(node.str1)+1):
            for j in range(1, len(node.str2)+1):
                if node.str1[i-1] == node.str2[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    matrix[i][j] = min(matrix[i-1][j-1]+MC[V.index(node.str1[i-1])][V.index(node.str2[j-1])], matrix[i-1][j]+CC, matrix[i][j-1]+CC)
        return matrix
    
    def print_matrix(matrix):
        for i in range(len(matrix)):
            print(matrix[i])

    def print_path(node):
        if node.parent == None:
            print(node.str1)
            print(node.str2)
            return
        node.print_path(node.parent)
        print(node.str1)
        print(node.str2)
        return
    
    def heuristic(node, MC):
        h = 0
        for i in range(len(node.str1)):
            if node.str1[i] != node.str2[i]:
                h += MC[V.index(node.str1[i])][V.index(node.str2[i])]
        return h
    
    def succ(node, MC):
        ls = []
        if node.pos[0] < len(node.str1) and node.pos[1] < len(node.str2):
            if node.str1[node.pos[0]] == node.str2[node.pos[1]]:
                ls.append(node(node.str1, node.str2, node, node.cost, [node.pos[0]+1, node.pos[1]+1]))
            else:
                ls.append(node(node.str1, node.str2, node, node.cost+MC[V.index(node.str1[node.pos[0]])][V.index(node.str2[node.pos[1]])], [node.pos[0]+1, node.pos[1]+1]))
        if node.pos[0] < len(node.str1):
            ls.append(node(node.str1, node.str2, node, node.cost+CC, [node.pos[0]+1, node.pos[1]]))
        if node.pos[1] < len(node.str2):
            ls.append(node(node.str1, node.str2, node, node.cost+CC, [node.pos[0], node.pos[1]+1]))
        return ls
    
    def goal(node):
        if node.pos[0] == len(node.str1) and node.pos[1] == len(node.str2):
            return True
        return False
    
    def A_star(node, MC):
        visited = []
        q = []
        heappush(q, node)
        while len(q) != 0:
            curr = heappop(q)
            if curr.goal():
                return curr
            visited.append(curr)
            for i in curr.succ(MC):
                if i not in visited:
                    heappush(q, i)
        return None
    
    def main():
        MC = match_cost()
        for i in range(K):
            for j in range(i+1, K):
                node = node(S[i], S[j], None, 0, [0, 0])
                matrix = node.matrix()
                matrix = node.fill_matrix(matrix, MC)
                node.print_matrix(matrix)
                print("The cost is: ", matrix[len(node.str1)][len(node.str2)])
                print("The path is: ")
                node.print_path(node.A_star(MC))
                print("The heuristic is: ", node.heuristic(MC))
                print("The total cost is: ", matrix[len(node.str1)][len(node.str2)]+node.heuristic(MC))
                print()
        return
    
    if __name__ == "__main__":
        main()


        

