#! python3

import random
import params
import copy

class Chromosome:
    def __init__(self, chromosome):
        self.chromosome = chromosome

    @classmethod
    def random(cls, author_publications_numbers: list):
        return cls(generate_chromosome(author_publications_numbers))

    @classmethod
    def from_list(cls, chromosome):
        return cls(chromosome)

    def cross(self, other):
        chromosome = [copy.deepcopy(gene1) if _should_cross() else copy.deepcopy(gene2) for (gene1, gene2) in
                      list(zip(self.chromosome, other.chromosome))]
        return Chromosome.from_list(chromosome)

    def cross_one_point(self, other):
        locus = random.randint(0, len(self.chromosome))
        chromosome = copy.deepcopy(self.chromosome[:locus]) + copy.deepcopy(other.chromosome[locus:])
        return Chromosome.from_list(chromosome)

    def mutate(self):
        for gene in self.chromosome:
            for value in gene:
                if _should_mutate():
                    value = not value
        return self


# metoda generująca losową listę list zer i jedynek reprezentującą chromosom
def generate_chromosome(author_publications_numbers: list):
    chromosome = list()
    for author_publications in author_publications_numbers:
        gene = list()
        for _ in range(author_publications):
            gene.append(random.randint(0, 1))
        chromosome.append(gene)
    return chromosome


def _should_cross():
    return random.randint(0, 99) < params.GENE_CROSS_PROBABILITY


def _should_mutate():
    return random.randint(0, 99) < params.GENE_MUTATION_PROBABILITY


def test():
    c = Chromosome([3, 2, 3, 2, 2, 2])
    c1 = Chromosome([3, 2, 3, 2, 2, 2])
    print(c.chromosome)
    print(c1.chromosome)
    c.cross(c1)


if __name__ == "__main__":
    test()
