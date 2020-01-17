#! python3

import random

import params
from cost_function import calculate_points as calculate_points_punishment
from cost_function import calculate_points_with_repair as calculate_points_repair
from chromosome import Chromosome
from data import Data
from mode import Mode
from mode import StartingPoint
from cost_function import EndOfCalculations
from cost_function import CostCalculationsSupervisor
from typing import List


def calculate_points(chromosome: Chromosome, data: Data):
    if params.MODE == Mode.PUNISHMENT:
        return calculate_points_punishment(chromosome, data)
    return calculate_points_repair(chromosome, data)


# 1124.15
# najlepiej działa select_best z dodawaniem losowych + cross_random

def algorithm(data: Data, starting_point: StartingPoint):
    CostCalculationsSupervisor.set_k(sum(data.get_publications_numbers()))
    try:
        if starting_point == StartingPoint.RANDOM:
            chromosomes = gen_random_chromosomes(data, params.NUMBER_OF_CHROMOSOMES)
        elif starting_point == StartingPoint.BEST:
            chromosomes = gen_best_chromosomes(data, params.NUMBER_OF_CHROMOSOMES)
        elif starting_point == StartingPoint.ALL:
            chromosomes = gen_full_chromosomes(data, params.NUMBER_OF_CHROMOSOMES)
        else:
            chromosomes = gen_empty_chromosomes(data, params.NUMBER_OF_CHROMOSOMES)

        # chromosomes = select_best(chromosomes, data)
        while True:
            calculate_chromosomes_points(chromosomes, data)
            # print([chromosome.points for chromosome in chromosomes])
            chromosomes = operate(chromosomes)
            chromosomes = mutate(chromosomes)
    except KeyboardInterrupt:
        return [], sorted(chromosomes, key=lambda c1: calculate_points(c1, data), reverse=True)[0]
    except EndOfCalculations as end_of_calculation:
        return end_of_calculation.max_history, \
               sorted(chromosomes, key=lambda c1: calculate_points(c1, data), reverse=True)[0]


def select_best(chromosomes: list, data: Data, can_be_sorted=True, add_random=False, number_of_random=5):
    number = params.NUMBER_OF_CHROMOSOMES - number_of_random if add_random else params.NUMBER_OF_CHROMOSOMES
    for chromosome in chromosomes:
        if chromosome.points == 0:
            chromosome.points = calculate_points(chromosome, data)
    sorted_chromosomes = sorted(chromosomes, key=lambda c1: c1.points, reverse=True)
    if can_be_sorted:
        result = sorted_chromosomes[0:number]
    else:
        chromosomes_to_be_selected = set(sorted_chromosomes[0:number])
        result = [chromosome for chromosome in chromosomes if chromosome in chromosomes_to_be_selected]
    chromosomes_to_add = gen_random_chromosomes(data, number_of_random if add_random else 0)
    for chromosome_to_add in chromosomes_to_add:
        chromosome_to_add.points = calculate_points(chromosome_to_add, data)
    return result + chromosomes_to_add


def cross_pairwise(chromosomes: list):
    return [c1.cross(c2) for c1, c2 in zip(chromosomes[0::2], chromosomes[1::2])]


def cross_random(chromosomes: list, number_of_offspring: int):
    offspring = list()
    for _ in range(0, number_of_offspring):
        c1 = chromosomes[random.randint(0, len(chromosomes) - 1)]
        c2 = chromosomes[random.randint(0, len(chromosomes) - 1)]
        offspring.append(c1.cross(c2))
    return offspring


def gen_random_chromosomes(data: Data, number: int):
    return [Chromosome.random(data.authors) for _ in range(number)]


def gen_best_chromosomes(data: Data, number: int):
    return [Chromosome.best(data.authors) for _ in range(number)]


def gen_full_chromosomes(data: Data, number: int):
    return [Chromosome.full(data.get_publications_numbers()) for _ in range(number)]


def gen_empty_chromosomes(data: Data, number: int):
    return [Chromosome.empty((data.get_publications_numbers())) for _ in range(number)]


def calculate_chromosomes_points(chromosomes: list, data: Data):
    for chromosome in chromosomes:
        if chromosome.points == 0:
            chromosome.points = calculate_points(chromosome, data)


def play_tournament(chromosomes: list, size: int):
    contestants = random.choices(chromosomes, k=size)
    return sorted(contestants, key=lambda c1: c1.points, reverse=True)[0]


def should_cross_chromosomes():
    return params.CHROMOSOME_MUTATION_PROBABILITY > random.randint(0, 99)


def select_tournament(chromosomes: list, number: int, size_of_tournament: int = 5):
    return [play_tournament(chromosomes, size_of_tournament) for _ in range(0, number)]


def cross(chromosomes: list):
    # return [c1.cross(c2) for c1, c2 in zip(chromosomes[0::2], chromosomes[1::2])]
    result = list()
    crossed_chromosomes = 0
    for c1, c2 in zip(chromosomes[0::2], chromosomes[1::2]):
        if should_cross_chromosomes():
            result.append(c1.cross(c2))
        else:
            result.append(c1)
            result.append(c2)
    return result


def mutate(chromosomes: list):
    return [c.mutate() for c in chromosomes]


def operate(chromosomes: list):
    result = list()
    for i in range(0, len(chromosomes)):
        if should_cross_chromosomes():
            c1, c2, *_ = select_tournament(chromosomes, 2)
            result.append(c1.cross(c2))
        else:
            result.append(select_tournament(chromosomes, 1)[0])
    return result



