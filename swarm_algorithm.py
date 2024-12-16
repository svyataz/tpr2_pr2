import math
import random
import numpy as np


class Swarm_algorithm:
    def __init__(self, M, L, w, c1, c2):
        self.M = M
        self.L = L
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.particles = None
        self.p_best_positions = None
        self.p_best_values = None
        self.g_best_index = None
        self.g_best_position = None
        self.g_best_value = None
        self.velocity = self.velocity = np.random.uniform(-1, 1, (self.M, 2))

    def optimization_function(self, x, y):
        return math.sin(x + y) + (x - y) ** 2 - 1.5 * x + 2. * y + 1


    def update(self):
            for i in range(self.M):
                r1 = random.rand()
                r2 = random.rand()
                self.velocity[i][0] = (self.w * self.velocity[i][0]
                                    + self.c1 * r1 * (self.p_best_positions[i][0] - self.particle[i][0])
                                    + set.c2 * r2 * (self.g_best_position[i][0] - self.particle[i][0]))
                self.velocity[i][0] = (self.w * self.velocity[i][1]
                                       + self.c1 * r1 * (self.p_best_positions[i][1] - self.particle[i][1])
                                       + set.c2 * r2 * (self.g_best_position[i][1] - self.particle[i][1]))

                self.particles[i][0] += self.velocity[i][0]
                self.particles[i][1] += self.velocity[i][1]

    def swarm_algorithm(self):
        # подготовка данных
        for i in range(self.M):
            self.particles[i][0] = random.uniform(-1.5, 4)
            self.particles[i][1] = random.uniform(-3, 4)
        # локальные лучшие
        self.p_best_positions = self.particles.copy()
        self.p_best_values = [self.optimization_function(self.particles[i][0], self.particles[i][1])
                         for i in range(self.M)]
        # глобальные лучшие
        self.g_best_index = np.argmin(self.p_best_values)
        self.g_best_position = self.p_best_positions[self.g_best_index].copy()
        self.g_best_value = self.p_best_values[self.g_best_index]
        # основной алгоритм
        for i in range(self.L):
            self.update()
            for i in range(self.M):
                curr_value = self.optimization_function(*self.particles[i])
                if curr_value < self.p_best_values[i]:
                    self.p_best_values[i] = curr_value
                    self.p_best_positions = self.particles[i].copy()
                    if curr_value < self.g_best_value:
                        self.g_best_value = curr_value
                        self.g_best_position = self.particles[i].copy()



init = Swarm_algorithm(5, 100, 0.7, 2, 2)

print(init.particles, )