#! python3

import random
import params
import copy
from data import Data, greedy_select_worst_publications, select_random_publications, calculate_share_sum


class Chromosome:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.points = 0

    @classmethod
    def from_list(cls, chromosome):
        return cls(chromosome)

    @classmethod
    def random(cls, authors):
        return cls(generate_chromosome(authors))

    @classmethod
    def best(cls, authors):
        return cls(generate_best_chromosome(authors))

    @classmethod
    def full(cls, author_publications_numbers: list):
        return cls(generate_full_chromosome(author_publications_numbers))

    @classmethod
    def empty(cls, author_publications_numbers: list):
        return cls(generate_empty_chromosome(author_publications_numbers))

    def __getitem__(self, item):
        return self.chromosome[item]

    def cross(self, other):
        chromosome = [copy.deepcopy(gene1) if _should_cross() else copy.deepcopy(gene2) for (gene1, gene2) in
                      list(zip(self.chromosome, other.chromosome))]
        return Chromosome.from_list(chromosome)

    def cross_one_point(self, other):
        locus = random.randint(0, len(self.chromosome))
        chromosome = copy.deepcopy(self.chromosome[:locus]) + copy.deepcopy(other.chromosome[locus:])
        return Chromosome.from_list(chromosome)

    def mutate(self):
        self.points = 0
        for gene in self.chromosome:
            for i, value in enumerate(gene):
                if _should_mutate():
                    gene[i] = not value

        return self


# metoda generująca losową listę list zer i jedynek reprezentującą chromosom
def generate_chromosome(authors):
    chromosome = list()
    for author in authors:
        share_sum = calculate_share_sum(author)
        share_limit = 4 * author.share_ratio
        if share_sum > share_limit:
            to_be_omitted_set = select_random_publications(author, share_sum, share_limit)
            gene = [1 if not publication.id in to_be_omitted_set else 0 for publication in author]
        else:
            gene = [1] * len(author.publications)
        chromosome.append(gene)
    return chromosome

# metoda generująca listę list zer i jedynek reprezentującą chromosom (najwyższa funkcja celu)
def generate_best_chromosome(authors):
    chromosome = list()
    for author in authors:
        share_sum = calculate_share_sum(author)
        share_limit = 4 * author.share_ratio
        if share_sum > share_limit:
            to_be_omitted_set = greedy_select_worst_publications(author, share_sum, share_limit)
            gene = [1 if not publication.id in to_be_omitted_set else 0 for publication in author]
        else:
            gene = [1] * len(author.publications)
        chromosome.append(gene)
    return chromosome

# metoda generująca losową listę list jedynek reprezentującą chromosom
def generate_full_chromosome(author_publications_numbers: list):
    chromosome = list()
    for author_publications in author_publications_numbers:
        chromosome.append([1] * author_publications)
    return chromosome

# metoda generująca losową listę list zer reprezentującą chromosom
def generate_empty_chromosome(author_publications_numbers: list):
    chromosome = list()
    for author_publications in author_publications_numbers:
        chromosome.append([0] * author_publications)
    return chromosome

def _should_cross():
    return random.randint(0, 99) < params.GENE_CROSS_PROBABILITY


def _should_mutate():
    return random.randint(0, 99) < params.GENE_MUTATION_PROBABILITY

