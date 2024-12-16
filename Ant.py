import math
import random
import numpy as np


class Ant:
    def __init__(self, a, b, q):
        self.a = a
        self.b = b
        self.q = q
        self.graph = ["спавн", "ред", "камни", "птицы", "волки", "блю", "громп"]
        self.graph_coord = {"спавн": (7.700, 7.700),
                            "ред": (-0.330, 4.200),
                            "камни": (-1.100, 5.830),
                            "птицы": (0.530, 2.584),
                            "волки": (4.350, 1.060),
                            "блю": (4.400, -0.600),
                            "громп": (6.310, -1.150)}
        self.t = np.ones((len(self.graph), len(self.graph)))
        s
        def path_calculation(self, x, y):
            result = 0
            result += math.sqrt((self.graph_coord[x][0] -
                                 self.graph_coord[y][0]) ** 2 +
                                (self.graph_coord[x][1] -
                                 self.graph_coord[y][1]) ** 2)
            return round(result, 4)

