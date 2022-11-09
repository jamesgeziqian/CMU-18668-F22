import random

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split


class Individual:
    '''
    This class represents an Individual in the population.
    '''

    def __init__(self, size) -> None:
        self.fitness = 0
        self.precision = 0
        self.recall = 0
        self.f1_score = 0
        self.genes = self.generate_random_genes(size)

    @staticmethod
    def generate_random_genes(size):
        return [random.choice([False, True]) for _ in range(size)]

    def __repr__(self) -> str:
        return f'accuracy: {self.fitness} precision: {self.precision} recall: {self.recall} f1_score: {self.f1_score}'

    def calc_fitness(self, estimator, data_df, random_state=1):
        '''
        Calculate and update the fitness of this individual.

        Fitness is defined as the accuracy on the current selection.
        '''
        data = data_df.drop('target', axis=1)
        target = data_df['target']
        selected_features = data.loc[:, self.genes]
        X_train, X_test, y_train, y_test = train_test_split(
            selected_features, target, random_state=random_state)

        estimator.fit(X_train, y_train)
        predicted = estimator.predict(X_test)
        self.fitness = accuracy_score(y_test, predicted)
        self.precision = precision_score(y_test, predicted)
        self.recall = recall_score(y_test, predicted)
        self.f1_score = f1_score(y_test, predicted)

    def crossover(self, partner: 'Individual'):
        # Crossover suggestion: child with half genes from one parent and half from the other parent
        ind_len = len(self.genes)
        child = Individual(ind_len)

        midpoint = random.randint(0, ind_len)
        child.genes = self.genes[:midpoint] + partner.genes[midpoint:]

        return child

    def mutate(self, mutation_rate):
        '''
        Based on mutaion rate, this function choose to flip the selection of features.
        '''
        for i, gene in enumerate(self.genes):
            if random.uniform(0, 1) < mutation_rate:
                self.genes[i] = not gene
