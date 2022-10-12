import random
import string


class Individual:
    """
        Individual in the population
    """

    def __init__(self, size):
        self.fitness = 0
        self.genes = self.generate_random_genes(size)

    @staticmethod
    def generate_random_genes(size):
        genes = []

        for i in range(size):
            genes.append(random.choice(string.printable))

        return genes

    def __repr__(self):
        return ''.join(self.genes) + " -> fitness: " + str(self.fitness)

    # Fitness function: returns a floating points of "correct" characters
    def calc_fitness(self, target):
        score = 0

        # insert your logic to calculate the individual fitness here

        self.fitness = score

    # The crossover function selects pairs of individuals to be mated, generating a third individual (child)
    def crossover(self, partner):
        # Crossover suggestion: child with half genes from one parent and half from the other parent
        ind_len = len(self.genes)
        child = Individual(ind_len)

        return child

    # Mutation: based on a mutation probability, the function picks a new random character and replace a gene with it
    def mutate(self, mutation_rate):
        # code to mutate the individual here
        pass



