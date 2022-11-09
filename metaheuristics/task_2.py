from sklearn import datasets
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from Population import Population


def main():
    raw_breast_cancer = datasets.load_breast_cancer(as_frame=True)

    pop_size = 200
    max_generations = 100
    target_acc = 0.99
    # regularized the data before feeding into SVC, no need to scale the gamma
    estimator = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    data_df = raw_breast_cancer.frame
    mutation_rate = 0.01
    random_state = 2

    pop = Population(target_acc, estimator, data_df,
                     pop_size, mutation_rate, random_state)

    pop.print_population_status()

    while not pop.finished and pop.generations < max_generations:
        pop.natural_selection()
        pop.print_population_status()


if __name__ == '__main__':
    main()
