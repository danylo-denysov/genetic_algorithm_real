from population import *
import random


class Mutation:
    mutation_type_even = 1
    mutation_type_index_swap = 2
    mutation_type_gauss = 3

    def __init__(self, mutation_type: int, probability: float):
        self.mutation_type = mutation_type
        self.probability = probability

    def mutation(self, population: Population, individual_amount_no_elitism: int):

        match self.mutation_type:
            case Mutation.mutation_type_even:
                self.mutation_type_even_method(population, individual_amount_no_elitism)
            case Mutation.mutation_type_index_swap:
                self.mutation_type_index_swap_method(population, individual_amount_no_elitism)
            case Mutation.mutation_type_gauss:
                self.mutation_type_gauss_method(population, individual_amount_no_elitism)

    def mutation_type_even_method(self, population: Population, individual_amount_no_elitism: int):
        chromosomes_amount = len(population.individuals[0].chromosome)  # amount of chromosomes in individual
        for i in range(0, individual_amount_no_elitism):
            chance_mutation = round(random.uniform(0, 1), 2)
            if 0 <= chance_mutation <= self.probability:
                chromosome_change = random.randint(0, chromosomes_amount - 1)
                new_value = round(random.uniform(Individual.range_start, Individual.range_end), Individual.precision_point)
                population.individuals[i].chromosome[chromosome_change].set_gene(new_value)

    def mutation_type_index_swap_method(self, population: Population, individual_amount_no_elitism: int):
        for i in range(0, individual_amount_no_elitism):
            chance_mutation = round(random.uniform(0, 1), 2)
            if 0 <= chance_mutation <= self.probability:
                population.individuals[i].chromosome[0].gene_value, population.individuals[i].chromosome[1].gene_value \
                    = population.individuals[i].chromosome[1].gene_value, population.individuals[i].chromosome[0].gene_value,

    def mutation_type_gauss_method(self, population: Population, individual_amount_no_elitism: int):
        chromosomes_amount = len(population.individuals[0].chromosome)  # amount of chromosomes in individual
        for i in range(0, individual_amount_no_elitism):
            chance_mutation = round(random.uniform(0, 1), 2)
            if 0 <= chance_mutation <= self.probability:
                for j in range(chromosomes_amount):
                    n = round(random.uniform(0, 1), Individual.precision_point)
                    new_value = population.individuals[i].chromosome[j].gene_value + n
                    while not (Individual.range_start < new_value < Individual.range_end):  # if value is beyond the range draw again
                        n = round(random.uniform(0, 1), Individual.precision_point)
                        new_value = population.individuals[i].chromosome[j].gene_value + n
                    population.individuals[i].chromosome[j].set_gene(new_value)
