import random

from typing import Tuple

import numpy as np

from Individual import Individual


class Population:
    '''
    This class describes a population of virtual individuals.
    '''

    def __init__(self, target_acc, estimator, data_df, size, mutation_rate, random_state=1) -> None:
        self.population = []
        self.generations = 0
        self.target_acc = target_acc
        self.estimator = estimator
        self.data_df = data_df
        # this random state is just for consistent train test split
        self.random_state = random_state
        self.mutation_rate = mutation_rate
        self.best_ind = None
        self.finished = False
        self.average_fitness = 0.0
        self.mating_pool = []

        self.create_initial_population(size)

    def create_initial_population(self, size):
        for _ in range(size + 1):
            ind = Individual(len(self.data_df.columns) - 1)
            ind.calc_fitness(self.estimator, self.data_df, self.random_state)
            self.population.append(ind)
        self.average_fitness = np.mean([i.fitness for i in self.population])

    def print_population_status(self):
        print(f'''
        Generation: {self.generations}
        Population average fitness: {self.average_fitness}
        Best individual {self.best_ind}
        ''')

    def natural_selection(self):
        self.mating_pool = []
        # Creating a mating pool with all the individuals based on their prob/fitness
        for i, ind in enumerate(self.population):
            prob = int(round(ind.fitness * 100))
            self.mating_pool += [i] * prob

        self.generate_new_population()
        self.evaluate()

    def selection(self) -> Tuple[Individual]:
        '''
        Select two individuals to crossover.
        '''
        i_partner_a = random.choice(self.mating_pool)
        i_partner_b = random.choice(self.mating_pool)
        return self.population[i_partner_a], self.population[i_partner_b]

    def generate_new_population(self):
        self.average_fitness = .0
        new_population = []
        for _ in range(len(self.population)):
            partner_a, partner_b = self.selection()
            offspring = partner_a.crossover(partner_b)
            offspring.mutate(self.mutation_rate)
            offspring.calc_fitness(
                self.estimator, self.data_df, self.random_state)
            new_population.append(offspring)

        self.average_fitness = np.mean([i.fitness for i in new_population])
        self.population = new_population
        self.generations += 1

    def evaluate(self):
        '''
        Compute/Identify the current "most fit" individual within the population.
        '''
        best_ind_i = np.argmax([ind.fitness for ind in self.population])
        self.best_ind = self.population[best_ind_i]

        if self.best_ind.fitness >= self.target_acc:
            self.finished = True
