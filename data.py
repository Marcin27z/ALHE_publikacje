#! python3

import params
from data_loader import load_data
from publication import Publication

class Author:
    def __init__(self, publications: list, share_ratio: float, id, is_phd_candidate, is_worker, is_N):
        self.publications = publications
        self.share_ratio = share_ratio
        self.id = id
        self.is_phd_candidate = is_phd_candidate
        self.is_worker = is_worker
        self.is_N = is_N

    def __getitem__(self, item):
        return self.publications[item]


class Data:
    def __init__(self, input_file_name):
        authors = load_authors(load_data(input_file_name))
        greedy_delete_worst_publications(authors)
        self.authors = authors

    def __getitem__(self, item):
        return self.authors[item]

    def get_publications_numbers(self):
        return [len(author.publications) for author in self.authors]

    def get_total_share_available(self):
        return sum(map(lambda a: a.share_ratio, self.authors))

# policzenie sumy udziałów danego autora
def calculate_share_sum(author: list):
    share_sum = 0
    for publication in author:
        share_sum += publication.share
    return share_sum

# metoda zwracająca listę numerów publikacji do usunięcia dla danego autora (numery wybierane zachłannie)
def greedy_select_worst_publications(author: list, share_sum: float, limit: float):
    sorted_publications = sorted(author)  # sorted tworzy kopię listy w przeciwieństwie do sort
    to_be_deleted = set()
    while share_sum > limit:
        share_sum -= sorted_publications[0].share
        to_be_deleted.add(sorted_publications[0].id)
        sorted_publications.pop(0)
    return to_be_deleted

# metoda usuwająca "najgorsze" publikacje metodą zachłanną
def greedy_delete_worst_publications(authors: list):
    for author in authors:
        share_sum = calculate_share_sum(author)
        share_limit = author.share_ratio * params.GREEDY_SELECTION_SHARE_LIMIT
        if share_sum > share_limit:
            to_be_deleted = greedy_select_worst_publications(author, share_sum, share_limit)
            author.publications = [publication for publication in author if not publication.id in to_be_deleted]

# metoda tworząca i zwracająca listę autorów (wraz z publikacjami)
def load_authors(parameters: dict):
    authors = list()
    for author_number in range(parameters['A']):
        publications = list()
        for publication_number in range(len(parameters['u'][author_number])):
            if parameters['w'][author_number][publication_number] > 0:
                publications.append(Publication(parameters['publicationIdList'][publication_number], parameters['w'][author_number][publication_number], parameters['u'][author_number][publication_number], parameters['monografia'][publication_number]))
        authors.append(Author(publications, parameters['udzial'][author_number], parameters['authorIdList'][author_number], parameters['doktorant'][author_number], parameters['pracownik'][author_number], parameters['czyN'][author_number]))
    return authors
