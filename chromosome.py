import random
import params


class Chromosome:
    def __init__(self, author_publications_number):
        self.chromosome = generate_chromosome(author_publications_number)

    def cross(self, other):
        chromosome = [gene1 if _should_cross() else gene2 for (gene1, gene2) in
                      list(zip(self.chromosome, other.chromosome))]
        print(chromosome)

    def mutate(self):
        for gene in self.chromosome:
            for value in gene:
                if _should_mutate():
                    value = not value


# metoda generująca losową listę list zer i jedynek reprezentującą chromosom
def generate_chromosome(author_publications_number):
    chromosome = list()
    for author_publications in author_publications_number:
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
