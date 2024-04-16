from population import *

import math


def population_init(individual_amount: int, variables_amount: int) -> Population:
    population = Population(individual_amount, variables_amount)
    for i in range(0, population.individual_amount):
        our_individual = Individual()
        for j in range(0, population.variables_amount):
            our_chromosome = Chromosome()
            our_chromosome.create_gene()
            our_individual.add_chromosome(our_chromosome)
        our_individual.update_values()
        population.add_individual(our_individual)

    return population


def update_data(population: Population):
    for individual in population.individuals:
        individual.update_values()
