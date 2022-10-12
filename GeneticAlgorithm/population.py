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
            pass
        """

    # Generate the new population based on the natural selection function
    def generate_new_population(self):
        pass

    # Compute/Identify the current "most fit" individual within the population
    def evaluate(self):
        pass
