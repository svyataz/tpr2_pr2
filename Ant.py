import math
import random
import numpy as np
from PIL.ImagePalette import sepia


class Ant:
    def __init__(self, a, b, q, epochs):
        self.a = a #влияние феромонов
        self.b = b #влияние эвристической информации
        self.q = q #коэффицент испарения
        self.epochs = epochs
        self.g_best_path = None
        self.g_best_length = float('inf')
        self.graph = ["спавн", "ред", "камни", "птицы", "волки", "блю", "громп"]
        self.distances = np.array([[np.inf, 8.759, 8.931, 8.808, 7.437, 8.931, 8.958],
                                     [8.759, np.inf, 1.802, 1.830, 5.635, 6.738, 8.527],
                                     [8.931, 1.802, np.inf, 3.632, 7.242, 8.461, 10.179],
                                     [8.808, 1.830, 3.632, np.inf, 4.112, 5.011, 6.881],
                                     [7.437, 5.635, 7.242, 4.112, np.inf, 1.660, 2.953],
                                     [8.931, 6.738, 8.461, 5.011, 1.660, np.inf, 1.987],
                                     [8.958, 8.527, 10.179, 6.881, 2.953, 1.987, np.inf]])
        self.n = 1 / self.distances
        np.fill_diagonal(self.n, 0)
        self.t = np.ones((len(self.graph), len(self.graph)))
        np.fill_diagonal(self.t, 0)
        self.probabilities = np.zeros(len(self.graph))

    #расчёт вероятностей
    def prob(self, x, graph):
        nb = self.n[x, graph] ** self.b
        ta = self.t[x, graph] ** self.a
        evr = ta * nb
        probabilities = evr / sum(evr)
        return probabilities

    def ant(self):
        for j in range(self.epochs):
            paths = []
            lengths = np.zeros(len(self.graph))

            #муравьи идут
            for ant in range(len(self.graph)):
                curr_node = 0
                start_node = 0
                path = [self.graph[curr_node]]
                unvisited_nodes = list(range(1, len(self.graph)))
                while unvisited_nodes:
                    probabilities = self.prob(curr_node, unvisited_nodes)
                    next_node = np.random.choice(unvisited_nodes, p=probabilities)
                    path.append(self.graph[next_node])
                    unvisited_nodes.remove(next_node)
                    lengths[ant] += self.distances[curr_node,next_node]
                    curr_node = next_node
                path.append(self.graph[start_node])
                lengths[ant]+= self.distances[curr_node,start_node]
                paths.append(path)
                #вывод 1
                print("путь муравья ", ant , ": ", path, " длина пути: ", round(lengths[ant], 2), sep='')

            #изменение феромонов
            self.t *= (1 - self.q)
            for length, path in zip(lengths, paths):
                dt = 1 / length
                for i in range(len(path) - 2):
                    self.t[self.graph.index(path[i])][self.graph.index(path[i + 1])] += dt
                    self.t[self.graph.index(path[i + 1])][self.graph.index(path[i])] += dt
            #изменение минимумов
            l_best_length = min(lengths)
            l_best_path = paths[np.argmin(lengths)]
            if l_best_length < self.g_best_length:
                self.g_best_length = l_best_length
                self.g_best_path = l_best_path

            #вывод 2
            print("лучшая длина шага ", j + 1, ": ", round(self.g_best_length, 2), " путь: ", self.g_best_path, sep='')

inst = Ant(2, 0.00005, 0.0000009, 5000)
inst.ant()