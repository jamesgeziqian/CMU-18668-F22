import random
from typing import Tuple

from individual import Individual


class Population:
    """
        A class that describes a population of virtual individuals
    """

    def __init__(self, target, size, mutation_rate):
        self.population = []
        self.generations = 0
        self.target = target
        self.mutation_rate = mutation_rate
        self.best_ind = None
        self.finished = False
        self.perfect_score = 1.0
        self.max_fitness = 0.0
        self.average_fitness = 0.0
        self.mating_pool = []

        self.create_initial_population(size, target)

    # Create a initial population randomly
    def create_initial_population(self, size, target):
        for i in range(size + 1):
            ind = Individual(len(target))
            ind.calc_fitness(target)

            if ind.fitness > self.max_fitness:
                self.max_fitness = ind.fitness

            self.average_fitness += ind.fitness
            self.population.append(ind)
        self.average_fitness /= size

    def print_population_status(self):
        print("\nGeneration " + str(self.generations))
        print("Population Average fitness: " + str(self.average_fitness))
        print("Best individual: " + str(self.best_ind))

    # Generate a mating pool according to the probability of each individual
    def natural_selection(self):
        """
            Implementation suggestion based on Lab:
            Based on fitness, each member will get added to the mating pool a certain number of times.
                a higher fitness = more entries to mating pool = more likely to be picked as a parent
                a lower fitness = fewer entries to mating pool = less likely to be picked as a parent
        """
        self.mating_pool = []
        # Creating a mating pool with all the individuals based on their prob/fitness
        for idx, ind in enumerate(self.population):
            prob = int(round(ind.fitness * 100))
            self.mating_pool.extend([idx] * prob)
            # self.mating_pool.extend([idx for _ in range(prob)])

        self.generate_new_population()
        self.evaluate()

    # Select two individuals for crossover
    def selection(self) -> Tuple[Individual]:
        mating_pool_pen = len(self.mating_pool)

        try:
            i_partner_a = self.mating_pool[random.randint(0, mating_pool_pen - 1)]
            i_partner_b = self.mating_pool[random.randint(0, mating_pool_pen - 1)]
        except ValueError as e:
            print(self.population)
            print(self.mating_pool)
            raise e

        partner_a = self.population[i_partner_a]
        partner_b = self.population[i_partner_b]
        return partner_a, partner_b

    # Generate the new population based on the natural selection function
    def generate_new_population(self):
        population_len = len(self.population)
        self.average_fitness = .0

        new_population = []
        for i in range(population_len):
            partner_a, partner_b = self.selection()
            offspring = partner_a.crossover(partner_b)
            offspring.mutate(self.mutation_rate)
            offspring.calc_fitness(self.target)
            self.average_fitness += offspring.fitness
            new_population.append(offspring)

        self.population = new_population
        self.generations += 1
        self.average_fitness /= len(new_population)

    # Compute/Identify the current "most fit" individual within the population
    def evaluate(self):
        best_fitness = .0
        for ind in self.population:
            if ind.fitness > best_fitness:
                best_fitness = ind.fitness
                self.best_ind = ind

        if best_fitness == self.perfect_score:
            self.finished = True
