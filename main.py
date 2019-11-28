#! python3

import random
from publication import Publication

# do zmiany jak pojawią się pliki z danymi
def process_input_data():
    author1 = list()
    for i in range(7):
        author1.append(Publication(i, 50+i,95+i))
    author2 = [Publication(0,20,30)]
    return [author1, author2]

# przygotowanie listy list zer i jedynek
def prepare_inclusion_matrix(publications):
    inclusion_matrix = list()
    for author in publications:
        inclusion_matrix.append([1] * len(author))
    return inclusion_matrix

# policzenie sumy udziałów danego autora
def calculate_share_sum(author_publications):
    share_sum = 0
    for publication in author_publications:
        share_sum += publication.share
    return share_sum

# metoda zwracająca listę numerów publikacji do usunięcia (numery wybierane zachłannie)
def greedy_select_worst_publications(author_publications, share_sum, limit):
    sorted_publications = sorted(author_publications)  # sorted tworzy kopię listy w przeciwieństwie do sort
    to_be_deleted = list()
    while share_sum > limit:
        share_sum -= sorted_publications[0].share
        to_be_deleted.append(sorted_publications[0].publication_number)
        sorted_publications.pop(0)
    to_be_deleted.sort()
    return to_be_deleted

# metoda generująca losową listę list zer i jedynek repreentującą chromosom
def generate_chromosome(author_publications_number):
    chromosome = list()
    for author_publications in author_publications_number:
        gene = list()
        for _ in range(author_publications):
            gene.append(random.randint(0,1))
        chromosome.append(gene)
    return chromosome

def main():
    publications = process_input_data()
    inclusion_matrix = prepare_inclusion_matrix(publications)
    author_publications_number = list()

    # zachłanna wstępna selekcja dla każdego z autorów z osobna (modyfikacja listy list zer i jedynek)
    for author_number, author in enumerate(publications):
        share_sum = calculate_share_sum(author)
        if share_sum > 550:
            to_be_deleted = greedy_select_worst_publications(author, share_sum, 550)
            index = 0
            while len(to_be_deleted) != 0:
                if author[index].publication_number == to_be_deleted[0]:
                    inclusion_matrix[author_number].pop(index)
                    author.pop(index)
                    to_be_deleted.pop(0)
                else:
                    index += 1
        author_publications_number.append(len(author))

    # prosty test - działa
    for author in publications:
        for publication in author:
            print(publication.publication_number, end = '')
        print()


if __name__ == "__main__":
    main()
