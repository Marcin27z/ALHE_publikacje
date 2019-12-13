#! python3

import random

import params
from cost_function import calculate_points
from chromosome import Chromosome
from data import Data


# 1124.15
# najlepiej działa select_best z dodawaniem losowych + cross_random

def algorithm(data: Data):
    chromosomes = gen_random_chromosomes(data, params.NUMBER_OF_CHROMOSOMES)
    # chromosomes = select_best(chromosomes, data)
    while True:
        offspring = cross_random(chromosomes, params.NUMBER_OF_CHROMOSOMES)
        offspring = [o.mutate() for o in offspring]
        chromosomes = select_best(chromosomes + offspring, data, add_random=True)
        print([calculate_points(chromosome, data) for chromosome in chromosomes])


def select_best(chromosomes: list, data: Data, can_be_sorted=True, add_random=False, number_of_random=5):
    number = params.NUMBER_OF_CHROMOSOMES - number_of_random if add_random else params.NUMBER_OF_CHROMOSOMES
    sorted_chromosomes = sorted(chromosomes, key=lambda c1: calculate_points(c1, data), reverse=True)
    if can_be_sorted:
        result = sorted_chromosomes[0:number]
    else:
        chromosomes_to_be_selected = set(sorted_chromosomes[0:number])
        result = [chromosome for chromosome in chromosomes if chromosome in chromosomes_to_be_selected]
    return result + gen_random_chromosomes(data, number_of_random if add_random else 0)


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
    return [Chromosome.random(data.get_publications_numbers()) for _ in range(number)]


if __name__ == "__main__":
    d = Data("filozofia-input.txt")
    algorithm(d)

# def select_ranked(chromosomes: list, data: Data):
#     number = params.NUMBER_OF_CHROMOSOMES
#     sorted_chromosomes = sorted(chromosomes, key=lambda c1: calculate_points(c1, data), reverse=True)
