from functions import *
from Crossover.crossover import *
from Mutation.mutation import *
import matplotlib.pyplot as p
import time
import statistics
# a: float = -10
# b: float = 10
# power_number_intervals: int = 6  # 10^power_number_intervals - number of intervals to divide our range
# individual_amount: int = 7
# variable_amount = 1
# individual_selection_amount: int = 3
# individual_elitism_amount = 2
# individual_amount_no_elitism = individual_amount - individual_elitism_amount
# epochs_amount: int = 0
# minimisation = True
# Chromosome.size = chromosome_length(a, b, power_number_intervals)
# Individual.range_start = a
# Individual.range_end = b
a: float = 0.0
b: float = 0.0
power_number_intervals: int = 0  # 10^power_number_intervals - number of intervals to divide our range
individual_amount: int = 0
variable_amount: int = 0
individual_selection_amount: int = 0
individual_elitism_amount: int = 0
epochs_amount: int = 0
minimisation: bool = True
selection_type: int = 0
mutation_type: int = 0
crossover_type: int = 0
crossover_probability: float = 0.0
mutation_probability: float = 0.0
inversion_probability: float = 0.0


def evolutionary_algorithm(variable_amount, a, b, power_number_intervals, individual_amount,
                           individual_selection_amount,
                           individual_elitism_amount, epochs_amount, selection_type, mutation_type, crossover_type,
                           crossover_probability, mutation_probability, inversion_probability, minimisation, func_type):
    Selection.evaluation_min = minimisation
    individual_amount_no_elitism = individual_amount - individual_elitism_amount
    Individual.range_start = a
    Individual.range_end = b
    Individual.precision_point = power_number_intervals
    Individual.func_type = func_type

    start_time = time.time()
    selection = Selection(selection_type, individual_selection_amount)
    crossover = Crossover(crossover_type, crossover_probability, individual_amount, individual_elitism_amount)
    mutation = Mutation(mutation_type, mutation_probability)

    population = population_init(individual_amount, variable_amount)
    the_best_individuals = {}
    x = []
    y = []
    average = []
    standard_deviation = []
    with open('result.txt', 'w') as file:
        for i in range(0, epochs_amount):
            best_individuals = selection.selection(population)
            the_best_individuals[i] = best_individuals[0]
            file.write(f"{i + 1}: {best_individuals[0].fitness_function_value}\n")
            elitists = [best_individuals[j] for j in range(0, individual_elitism_amount)]
            population = crossover.crossover(best_individuals)
            mutation.mutation(population, individual_amount_no_elitism)
            update_data(population)
            for j in elitists:
                population.add_individual(j)
            x.append(i)
            y.append(best_individuals[0].fitness_function_value)
            suma: float = 0.0
            values_list = []
            for k in range(0, individual_amount):
                values_list.append(population.individuals[k].fitness_function_value)
                suma = sum(values_list)
            average.append(suma / individual_amount)
            standard_deviation.append(statistics.stdev(values_list))

    for key, value in the_best_individuals.items():
        print(key)
        value.display()

    timee = round((time.time() - start_time), 5)

    fig, axs = p.subplots(1, 3, figsize=(15, 5))

    # Pierwszy wykres
    axs[0].plot(x, y)
    axs[0].set_title("Wykres wartości funkcji")
    axs[0].set_xlabel("Iteracja")
    axs[0].set_ylabel("Wartość funkcji")

    # Drugi wykres
    axs[1].plot(x, average)
    axs[1].set_title("Wykres średniej wartości funkcji")
    axs[1].set_xlabel("Iteracja")
    axs[1].set_ylabel("Średnia wartość funkcji")

    # Trzeci wykres
    axs[2].plot(x, standard_deviation)
    axs[2].set_title("Wykres odchylenia standardowego")
    axs[2].set_xlabel("Iteracja")
    axs[2].set_ylabel("Odchylenie standardowe")

    # Wyświetlanie wykresów
    p.tight_layout()
    p.show()
    return the_best_individuals, timee
