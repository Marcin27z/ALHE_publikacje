#! python3

import functools
import random

import params
from cost import calculate_points
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
    a1 = Author([Publication(0, 10, 0.1), Publication(1, 10, 0.2)], 1)
    a2 = Author([Publication(2, 10, 0.1), Publication(3, 20, 0.2)], 0.5)
    a3 = Author([Publication(4, 10, 0.1), Publication(5, 30, 0.2)], 0.75)
    d = Data([a1, a2, a3])
    algorithm(d)
