import itertools
import math
import random


class Simulated_annealing:
    def __init__(self, a = 0.9, epochs = 1000, start_t = 100, step_size = 0.1):
        self.epochs = epochs
        self.t = start_t
        self.start_t = start_t
        self.step_size = step_size
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
            self.t *= self.a
        return self.x, self.y, self.energy

    def path_calculation(self, graph):
        result = 0
        for i in range(0, len(graph) - 1):
            result += math.sqrt((self.graph_coord[graph[i]][0] -
                                      self.graph_coord[graph[i + 1]][0]) ** 2 +
                                (self.graph_coord[graph[i]][1] -
                                      self.graph_coord[graph[i + 1]][1]) ** 2)
        return round(result, 4)

    def graph_simulated_annealing(self):
        self.energy = self.path_calculation(self.graph)
        gen = itertools.permutations(self.graph)
        for _ in range(self.epochs):
            new_graph = next(gen)
            new_graph += (new_graph[0],)
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
        return self.graph, self.energy
inst = Simulated_annealing()
print(inst.f_simulated_annealing())
inst = Simulated_annealing(0.95, 50)
print(inst.graph_simulated_annealing())

