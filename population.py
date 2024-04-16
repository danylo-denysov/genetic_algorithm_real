import random
import benchmark_functions as bf


class Chromosome:
    def __init__(self):
        self.gene_value = None

    def create_gene(self):
        new_value = round(random.uniform(Individual.range_start, Individual.range_end), Individual.precision_point)
        self.set_gene(new_value)

    def set_gene(self, new_gene: float):
        self.gene_value = new_gene


class Individual:
    range_start = None
    range_end = None
    precision_point = None
    func_type = None

    def __init__(self):
        self.chromosome = []  # [Chromosome1, Chromosome2]
        self.chromosome_values = []  # [value1, value2]
        self.fitness_function_value = None

    def add_chromosome(self, new_chromosome: Chromosome):
        self.chromosome.append(new_chromosome)
        # value = self.chromosome_decode(Individual.range_start, Individual.range_end, new_chromosome)
        # self.chromosome_values.append(value)

    def update_values(self):
        for chromosome in self.chromosome:
            self.chromosome_values.append(chromosome.gene_value)
        self.set_fitness_function()

    def set_fitness_function(self):
        self.fitness_function_value = self.fitness_function(self.chromosome_values)

    @staticmethod
    def fitness_function(variables: list) -> float:  # variables = [variable1, variable2, variable3]
        variables_amount = len(variables)
        match Individual.func_type:
            case 1:
                return variables[0] ** 3 - 7 * variables[0] ** 2 + -10 * variables[0] - 4
            case 2:
                return variables[0] ** 3 * variables[1] ** 3 - 2 * variables[0] ** 2
            case 3:
                function = bf.Hypersphere(variables_amount)
                return function(variables)
            case 4:
                function = bf.Hyperellipsoid(variables_amount)
                return function(variables)
            case 5:
                function = bf.Schwefel(variables_amount)
                return function(variables)
            case 6:
                function = bf.Ackley(variables_amount)
                return function(variables)
            case 7:
                function = bf.Michalewicz(variables_amount)
                return function(variables)
            case 8:
                function = bf.Rastrigin(variables_amount)
                return function(variables)
            case 9:
                function = bf.Rosenbrock(variables_amount)
                return function(variables)
            case 10:
                function = bf.DeJong3(variables_amount)
                return function(variables)
            case 11:
                function = bf.DeJong5()
                return function(variables)
            case 12:
                function = bf.MartinGaddy()
                return function(variables)
            case 13:
                function = bf.Griewank(variables_amount)
                return function(variables)
            case 14:
                function = bf.Easom()
                return function(variables)
            case 15:
                function = bf.GoldsteinAndPrice()
                return function(variables)
            case 16:
                function = bf.PichenyGoldsteinAndPrice()
                return function(variables)
            case 17:
                function = bf.StyblinskiTang(variables_amount)
                return function(variables)
            case 18:
                function = bf.McCormick()
                return function(variables)
            case 19:
                function = bf.Rana(variables_amount)
                return function(variables)
            case 20:
                function = bf.EggHolder(variables_amount)
                return function(variables)
            case 21:
                function = bf.Keane(variables_amount)
                return function(variables)
            case 22:
                function = bf.Schaffer2()
                return function(variables)
            case 23:
                function = bf.Himmelblau()
                return function(variables)
            case 24:
                function = bf.PitsAndHoles()
                return function(variables)

    def display(self):
        for i in range(0, len(self.chromosome)):
            print(self.chromosome_values[i])
        print(f"Wartosc fitness_function: {self.fitness_function_value}")


class Population:

    def __init__(self, individual_amount: int, variables_amount: int):
        self.individual_amount = individual_amount
        self.individuals = []
        self.variables_amount = variables_amount

    def add_individual(self, new_individual: Individual):
        self.individuals.append(new_individual)


