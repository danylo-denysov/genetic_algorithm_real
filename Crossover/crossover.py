from population import *
from functions import *
from Selection.selection import *
import copy


class Crossover:
    crossover_type_arithmetic = 1
    crossover_type_blend = 2
    crossover_type_blend_beta = 3
    crossover_type_average = 4
    crossover_type_flat = 5
    crossover_type_heuristic = 6
    crossover_type_linear = 7

    def __init__(self, crossover_type: int, probability: float, individual_amount: int, individual_elitism_amount: int):
        self.crossover_type = crossover_type
        self.individual_amount = individual_amount
        self.individuals_amount_create = individual_amount - individual_elitism_amount
        self.probability = probability

    def crossover(self, individuals_list: list[Individual]):
        match self.crossover_type:
            case Crossover.crossover_type_arithmetic:
                population = self.crossover_type_arithmetic_method(individuals_list)
                return population
            case Crossover.crossover_type_blend:
                population = self.crossover_type_blend_method(individuals_list)
                return population
            case Crossover.crossover_type_blend_beta:
                population = self.crossover_type_blend_beta_method(individuals_list)
                return population
            case Crossover.crossover_type_average:
                population = self.crossover_type_average_method(individuals_list)
                return population
            case Crossover.crossover_type_flat:
                population = self.crossover_type_flat_method(individuals_list)
                return population
            case Crossover.crossover_type_heuristic:
                population = self.crossover_type_heuristic_method(individuals_list)
                return population
            case Crossover.crossover_type_linear:
                population = self.crossover_type_linear_method(individuals_list)
                return population

    def crossover_type_arithmetic_method(self, individuals_list: list[Individual]):  # 2 new individuals
        chromosomes_amount = len(individuals_list[0].chromosome)  # amount of chromosomes in individual

        population = Population(self.individual_amount, chromosomes_amount)

        individuals_amount_create_copy = self.individuals_amount_create
        while individuals_amount_create_copy > 0:
            index1, index2 = random.sample(range(len(individuals_list)), 2)  # indices of individuals to cross
            chance_crossover = round(random.uniform(0, 1), 2)  # chance of crossover
            if 0 <= chance_crossover <= self.probability:
                new_individual1 = Individual()
                for i in range(0, chromosomes_amount):
                    new_chromosome = Chromosome()
                    k = round(random.uniform(0, 1), Individual.precision_point)
                    new_value = k * individuals_list[index1].chromosome[i].gene_value + (1 - k) * individuals_list[index2].chromosome[i].gene_value
                    while not (Individual.range_start < new_value < Individual.range_end):  # if value is beyond the range draw again
                        k = round(random.uniform(0, 1), Individual.precision_point)
                        new_value = k * individuals_list[index1].chromosome[i].gene_value + (1 - k) * individuals_list[index2].chromosome[i].gene_value
                    new_chromosome.set_gene(new_value)
                    new_individual1.add_chromosome(new_chromosome)
                population.add_individual(new_individual1)
                individuals_amount_create_copy -= 1

                if individuals_amount_create_copy != 0:
                    new_individual2 = Individual()
                    for i in range(0, chromosomes_amount):
                        new_chromosome = Chromosome()
                        k = round(random.uniform(0, 1), Individual.precision_point)
                        new_value = (1 - k) * individuals_list[index1].chromosome[i].gene_value + k * individuals_list[index2].chromosome[i].gene_value
                        while not (Individual.range_start < new_value < Individual.range_end):  # if value is beyond the range draw again
                            k = round(random.uniform(0, 1), Individual.precision_point)
                            new_value = (1 - k) * individuals_list[index1].chromosome[i].gene_value + k * individuals_list[index2].chromosome[i].gene_value
                        new_chromosome.set_gene(new_value)
                        new_individual2.add_chromosome(new_chromosome)
                    population.add_individual(new_individual2)
                    individuals_amount_create_copy -= 1
            elif self.probability < chance_crossover <= 1:
                continue

        return population

    def crossover_type_blend_method(self, individuals_list: list[Individual]):
        # TODO
        pass

    def crossover_type_blend_beta_method(self, individuals_list: list[Individual]):
        # TODO
        pass

    def crossover_type_average_method(self, individuals_list: list[Individual]):  # 1 new individual
        chromosomes_amount = len(individuals_list[0].chromosome)  # amount of chromosomes in individual

        population = Population(self.individual_amount, chromosomes_amount)

        individuals_amount_create_copy = self.individuals_amount_create
        while individuals_amount_create_copy > 0:
            index1, index2 = random.sample(range(len(individuals_list)), 2)  # indices of individuals to cross
            chance_crossover = round(random.uniform(0, 1), 2)  # chance of crossover
            if 0 <= chance_crossover <= self.probability:
                new_individual = Individual()
                for i in range(0, chromosomes_amount):
                    new_chromosome = Chromosome()
                    new_value = (individuals_list[index1].chromosome[i].gene_value + individuals_list[index2].chromosome[i].gene_value) / 2
                    new_chromosome.set_gene(new_value)
                    new_individual.add_chromosome(new_chromosome)
                population.add_individual(new_individual)
                individuals_amount_create_copy -= 1
            elif self.probability < chance_crossover <= 1:
                continue

        return population

    def crossover_type_flat_method(self, individuals_list: list[Individual]):  # 1 new individual
        chromosomes_amount = len(individuals_list[0].chromosome)  # amount of chromosomes in individual

        population = Population(self.individual_amount, chromosomes_amount)

        individuals_amount_create_copy = self.individuals_amount_create
        while individuals_amount_create_copy > 0:
            index1, index2 = random.sample(range(len(individuals_list)), 2)  # indices of individuals to cross
            chance_crossover = round(random.uniform(0, 1), 2)  # chance of crossover
            if 0 <= chance_crossover <= self.probability:
                new_individual = Individual()
                for i in range(0, chromosomes_amount):
                    new_chromosome = Chromosome()
                    new_value = round(random.uniform(individuals_list[index1].chromosome[i].gene_value, individuals_list[index2].chromosome[i].gene_value), Individual.precision_point)
                    new_chromosome.set_gene(new_value)
                    new_individual.add_chromosome(new_chromosome)
                population.add_individual(new_individual)
                individuals_amount_create_copy -= 1
            elif self.probability < chance_crossover <= 1:
                continue

        return population

    def crossover_type_heuristic_method(self, individuals_list: list[Individual]):  # 1 new individual
        chromosomes_amount = len(individuals_list[0].chromosome)  # amount of chromosomes in individual

        population = Population(self.individual_amount, chromosomes_amount)

        individuals_amount_create_copy = self.individuals_amount_create
        while individuals_amount_create_copy > 0:
            index1, index2 = random.sample(range(len(individuals_list)), 2)  # indices of individuals to cross
            if Selection.evaluation_min:
                while individuals_list[index1].fitness_function_value < individuals_list[index2].fitness_function_value:
                    index1, index2 = random.sample(range(len(individuals_list)), 2)
            else:
                while individuals_list[index1].fitness_function_value > individuals_list[index2].fitness_function_value:
                    index1, index2 = random.sample(range(len(individuals_list)), 2)
            chance_crossover = round(random.uniform(0, 1), 2)  # chance of crossover
            if 0 <= chance_crossover <= self.probability:
                new_individual = Individual()
                for i in range(0, chromosomes_amount):
                    new_chromosome = Chromosome()
                    k = round(random.uniform(0, 1), Individual.precision_point)
                    new_value = (k * (individuals_list[index2].chromosome[i].gene_value - individuals_list[index1].chromosome[i].gene_value)
                                 + individuals_list[index1].chromosome[i].gene_value)
                    while not (Individual.range_start < new_value < Individual.range_end):  # if value is beyond the range draw again
                        k = round(random.uniform(0, 1), Individual.precision_point)
                        new_value = (k * (individuals_list[index2].chromosome[i].gene_value - individuals_list[index1].chromosome[i].gene_value)
                                     + individuals_list[index1].chromosome[i].gene_value)
                    new_chromosome.set_gene(new_value)
                    new_individual.add_chromosome(new_chromosome)
                population.add_individual(new_individual)
                individuals_amount_create_copy -= 1
            elif self.probability < chance_crossover <= 1:
                continue

        return population

    def crossover_type_linear_method(self, individuals_list: list[Individual]):  # 2 new individuals TODO check if values are in range
        chromosomes_amount = len(individuals_list[0].chromosome)  # amount of chromosomes in individual

        population = Population(self.individual_amount, chromosomes_amount)

        individuals_amount_create_copy = self.individuals_amount_create
        while individuals_amount_create_copy > 0:
            index1, index2 = random.sample(range(len(individuals_list)), 2)  # indices of individuals to cross
            chance_crossover = round(random.uniform(0, 1), 2)  # chance of crossover
            if 0 <= chance_crossover <= self.probability:
                new_individual1 = Individual()
                new_individual2 = Individual()
                new_individual3 = Individual()
                for i in range(0, chromosomes_amount):
                    new_chromosome = Chromosome()
                    new_value = 0.5 * individuals_list[index1].chromosome[i].gene_value + 0.5 * individuals_list[index2].chromosome[i].gene_value
                    new_chromosome.set_gene(new_value)
                    new_individual1.add_chromosome(new_chromosome)

                for i in range(0, chromosomes_amount):
                    new_chromosome = Chromosome()
                    new_value = 1.5 * individuals_list[index1].chromosome[i].gene_value - 0.5 * individuals_list[index2].chromosome[i].gene_value
                    new_chromosome.set_gene(new_value)
                    new_individual2.add_chromosome(new_chromosome)

                for i in range(0, chromosomes_amount):
                    new_chromosome = Chromosome()
                    new_value = -0.5 * individuals_list[index1].chromosome[i].gene_value + 1.5 * individuals_list[index2].chromosome[i].gene_value
                    new_chromosome.set_gene(new_value)
                    new_individual3.add_chromosome(new_chromosome)

                new_individual1.update_values()
                new_individual2.update_values()
                new_individual3.update_values()

                new_individuals = [new_individual1, new_individual2, new_individual3]
                if Selection.evaluation_min:
                    sorted_new_individuals = sorted(new_individuals, key=lambda x: x.fitness_function_value)
                else:
                    sorted_new_individuals = sorted(new_individuals, key=lambda x: x.fitness_function_value, reverse=True)

                population.add_individual(sorted_new_individuals[0])
                individuals_amount_create_copy -= 1

                if individuals_amount_create_copy != 0:
                    population.add_individual(sorted_new_individuals[1])
                    individuals_amount_create_copy -= 1
            elif self.probability < chance_crossover <= 1:
                continue

        return population
