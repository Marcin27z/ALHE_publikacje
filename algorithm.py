#! python3

import functools
import random

import params
from cost_function import calculate_points
from chromosome import Chromosome
from data import Data, Author
from publication import Publication


def algorithm(data: Data):
    chromosomes = [Chromosome.random(data.get_publications_numbers()) for _ in range(params.NUMBER_OF_CHROMOSOMES)]
    while True:
        offspring = [c1.cross(c2) for c1, c2 in zip(chromosomes[0::2], chromosomes[1::2])]
        offspring = [o.mutate() for o in offspring]
        chromosomes = select_best(chromosomes + offspring, data)
        print([calculate_points(chromosome, data) for chromosome in chromosomes])


def select_best(chromosomes: list, data: Data):
    number = params.NUMBER_OF_CHROMOSOMES
    sorted_chromosomes = sorted(chromosomes, key=lambda c1: calculate_points(c1, data), reverse=True)
    return sorted_chromosomes[0:number]


if __name__ == "__main__":
    d = Data("filozofia-input.txt")
    algorithm(d)
