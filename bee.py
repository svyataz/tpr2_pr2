import random
import numpy as np


class Bee:
    def __init__(self, s, t, euc, delta):
        self.t = t
        self.s = s
        self.delta = delta
        self.euc = euc
        self.bees = np.zeros(s)
        self.values = np.zeros(s)
        self.g_best_bee = None
    def optimization_function(self, x, y):
        return np.sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1

    def euclidean_distance(self, x, y):
        return np.sqrt(np.sum((x - y) ** 2))

    def sending_bees(self):
        for i in range(self.s):
            self.bees[i][0] = random.uniform(-1.5, 4)
            self.bees[i][1] = random.uniform(-3, 4)
            self.values[i] = self.optimization_function(*self.bees[i])

    def get_g_best_bee(self):
        self.g_best_bee = self.values.index(min(self.values))
        return self.g_best_bee

    def bee(self):
        best_bee = self.get_g_best_bee()
        for i in range(self.s):
            distance = self.euclidean_distance(self.bees[best_bee], self.bees[i])
            if distance < self.euc:
                
