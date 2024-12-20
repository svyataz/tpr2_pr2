import itertools
import math
import random

import numpy as np


class Simulated_annealing:
    def __init__(self, a = 0.9, epochs = 1000, start_t = 100):
        self.epochs = epochs
        self.t = start_t
        self.start_t = start_t
        self.x = None
        self.y = None
        self.energy = None
        self.a = a
        self.graph = ["спавн", "ред", "камни", "птицы", "волки", "блю", "громп"]
        self.graph_coord = {"спавн": (7.700, 7.700),
                            "ред":(-0.330, 4.200),
                            "камни":(-1.100, 5.830),
                            "птицы":(0.530, 2.584),
                            "волки":(4.350, 1.060),
                            "блю":(4.400, -0.600),
                            "громп":(6.310, -1.150)}

    def optimization_function(self, x, y):
        return math.sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1

    def f_simulated_annealing(self):
        self.x = random.uniform(-1.5, 4)
        self.y = random.uniform(-3, 4)
        self.energy = self.optimization_function(self.x, self.y)
        for i in range(self.epochs):
            new_x = random.uniform(-1.5, 4)
            new_y = self.y = random.uniform(-3, 4)
            new_energy = self.optimization_function(new_x, new_y)
            delta = new_energy - self.energy
            if delta > 0:
                p = self.start_t * math.exp((-delta) / self.t)
                random_p = random.random() * 100
                if random_p <= p:
                    self.x = new_x
                    self.y = new_y
                    self.energy = new_energy
            else:
                self.x = new_x
                self.y = new_y
                self.energy = new_energy
            self.t = self.start_t / ((i + 1) ** 2)
            print("текущее решение шага ", i + 1, ": x=", self.x, "; y=", self.y, "; f=", self.energy, sep='')
    def path_calculation(self, graph):
        result = 0
        for i in range(0, len(graph) - 1):
            result += math.sqrt((self.graph_coord[graph[i]][0] -
                                      self.graph_coord[graph[i + 1]][0]) ** 2 +
                                (self.graph_coord[graph[i]][1] -
                                      self.graph_coord[graph[i + 1]][1]) ** 2)
        return round(result, 4)
    def swap_graph(self, graph):
        index= np.random.choice(range(len(graph)),size=2)
        new_graph = list(graph)
        new_graph[index[0]], new_graph[index[1]] = new_graph[index[1]], new_graph[index[0]]
        return new_graph

    def graph_simulated_annealing(self):
        self.energy = self.path_calculation(self.graph)
        for i in range(self.epochs):
            new_graph = self.swap_graph(self.graph)
            new_energy = self.path_calculation(new_graph)
            delta = new_energy - self.energy
            if delta > 0:
                p = self.start_t * math.exp((-delta) / self.t)
                random_p = random.random() * 100
                if random_p <= p:
                    self.graph = new_graph
                    self.energy = new_energy
            else:
                self.graph = new_graph
                self.energy = new_energy
            self.t *= self.a
            print("выбранный граф шага ", i + 1, ": ", self.graph, "\nдлина пути: ", self.energy,sep='')

inst = Simulated_annealing()
inst.f_simulated_annealing()
print("найденное решение: ", "x=", inst.x, "; y=", inst.y, "; f=", inst.energy, sep='')
inst = Simulated_annealing(0.9, 1000)
inst.graph_simulated_annealing()
print("выбранный граф: ", inst.graph, "\nдлина пути: ", inst.energy, sep='')
