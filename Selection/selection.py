from population import *


class Selection:
    selection_type_best = 1
    selection_type_tournament = 2
    selection_type_roulette = 3

    evaluation_min = True  # True for finding minimum, False for finding maximum

    def __init__(self, selection_type: int, individuals_best_amount: int):
        self.selection_type = selection_type
        self.individuals_best_amount = individuals_best_amount

    def selection(self, population: Population) -> list[Individual]:
        match self.selection_type:
            case Selection.selection_type_best:
                best_chromosomes = self.selection_best_method(population)
                return best_chromosomes
            case Selection.selection_type_tournament:
                best_chromosomes = self.selection_tournament_method(population)
                return best_chromosomes
            case Selection.selection_type_roulette:
                best_chromosomes = self.selection_roulette_method(population)
                return best_chromosomes

    def selection_best_method(self, population: Population) -> list[Individual]:

        if Selection.evaluation_min:
            individuals_sorted = sorted(population.individuals, key=lambda x: x.fitness_function_value)
            individuals_list = []
            for i in range(0, self.individuals_best_amount):
                individuals_list.append(individuals_sorted[i])
            return individuals_list
        else:
            individuals_sorted = sorted(population.individuals, key=lambda x: x.fitness_function_value, reverse=True)
            individuals_list = []
            for i in range(0, self.individuals_best_amount):
                individuals_list.append(individuals_sorted[i])
            return individuals_list

    def selection_roulette_method(self, population: Population) -> list[Individual]:
        individuals_list = []

        fitness_function_list_max = []
        for individual in population.individuals:
            fitness_function_list_max.append(individual.fitness_function_value)

        if Selection.evaluation_min:
            fitness_function_list_min = []
            for i in range(len(fitness_function_list_max)):
                fitness_function_list_min.append(1 / fitness_function_list_max[i])
            sum_fitness_function_min = sum(fitness_function_list_min)

            minimum_value_min = min(fitness_function_list_min)
            for i in range(len(fitness_function_list_max)):
                fitness_function_list_min[i] += minimum_value_min + 1

            sum_fitness_function_min = sum(fitness_function_list_min)

            for i in range(len(fitness_function_list_min)):
                fitness_function_list_min[i] /= sum_fitness_function_min

            running_sum = 0
            for i in range(len(fitness_function_list_min)):
                temp = fitness_function_list_min[i]
                fitness_function_list_min[i] += running_sum
                running_sum += temp

            for i in range(0, self.individuals_best_amount):
                drawn_probability = round(random.uniform(0, 1), 10)
                closest_index, closest_number = min(enumerate(fitness_function_list_min), key=lambda x: abs(x[1] - drawn_probability))
                is_in_list = any(obj.fitness_function_value == population.individuals[closest_index].fitness_function_value for obj in individuals_list)
                if is_in_list:
                    pass
                else:
                    individuals_list.append(population.individuals[closest_index])

            individuals_list.sort(key=lambda x: x.fitness_function_value)
        else:
            minimum_value_max = min(fitness_function_list_max)
            for i in range(len(fitness_function_list_max)):
                fitness_function_list_max[i] += minimum_value_max + 1

            sum_fitness_function_max = sum(fitness_function_list_max)

            for i in range(len(fitness_function_list_max)):
                fitness_function_list_max[i] /= sum_fitness_function_max

            running_sum = 0
            for i in range(len(fitness_function_list_max)):
                temp = fitness_function_list_max[i]
                fitness_function_list_max[i] += running_sum
                running_sum += temp

            for i in range(0, self.individuals_best_amount):
                drawn_probability = round(random.uniform(0, 1), 2)
                closest_index, closest_number = min(enumerate(fitness_function_list_max), key=lambda x: abs(x[1] - drawn_probability))
                is_in_list = any(obj.fitness_function_value == population.individuals[closest_index].fitness_function_value for obj in individuals_list)
                if is_in_list:
                    pass
                else:
                    individuals_list.append(population.individuals[closest_index])

            individuals_list.sort(key=lambda x: x.fitness_function_value, reverse=True)

        return individuals_list

    def selection_tournament_method(self, population: Population) -> list[Individual]:
        tournament_individual_amount = int(population.individual_amount / self.individuals_best_amount)
        tournament_size = len(population.individuals) // tournament_individual_amount
        random.shuffle(population.individuals)
        tournaments = []

        for i in range(0, len(population.individuals), tournament_size):
            sublist = population.individuals[i:i + tournament_size]
            tournaments.append(sublist)

        remainder = len(population.individuals) % tournament_individual_amount
        for i in range(remainder):
            tournaments[i].append(population.individuals.pop())

        if remainder != 0:
            tournaments.pop()

        individuals_list = []
        for tournament in tournaments:
            if Selection.evaluation_min:
                tournament_sorted = sorted(tournament, key=lambda x: x.fitness_function_value)
            else:
                tournament_sorted = sorted(tournament, key=lambda x: x.fitness_function_value, reverse=True)
            individuals_list.append(tournament_sorted[0])

        return individuals_list
