#! python3

import params

class Author:
    def __init__(self, publications: list, share_ratio: float):
        self.publications = publications
        self.share_ratio = share_ratio

    def __getitem__(self, item):
        return self.publications[item]


class Data:
    def __init__(self, authors: list):
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
    to_be_deleted = list()
    while share_sum > limit:
        share_sum -= sorted_publications[0].share
        to_be_deleted.append(sorted_publications[0].publication_number)
        sorted_publications.pop(0)
    to_be_deleted.sort()
    return to_be_deleted

def greedy_delete_worst_publications(authors: list):
    for author in authors:
        share_sum = calculate_share_sum(author)
        share_limit = author.share_ratio * params.GREEDY_SELECTION_SHARE_LIMIT
        if share_sum > share_limit:
            to_be_deleted = greedy_select_worst_publications(author, share_sum, share_limit)
            index = 0
            while len(to_be_deleted) != 0:
                if author[index].publication_number == to_be_deleted[0]:
                    author.publications.pop(index)
                    to_be_deleted.pop(0)
                else:
                    index += 1


