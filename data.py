class Author:
    def __init__(self, publications: list, share):
        self.publications = publications
        self.share = share

    def __getitem__(self, item):
        return self.publications[item]


class Data:
    def __init__(self, authors: list):
        self.authors = authors

    def __getitem__(self, item):
        return self.authors[item]

    def get_publications_numbers(self):
        return [len(author.publications) for author in self.authors]

    def get_total_share_available(self):
        return sum(map(lambda a: a.share, self.authors))



