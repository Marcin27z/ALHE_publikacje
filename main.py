#! python3

import random
from publication import Publication
from data import Data, Author

# do zmiany jak pojawią się pliki z danymi
#def process_input_data():
#    author1 = list()
#    for i in range(7):
#        author1.append(Publication(i, 50 + i, 0.95 + i*0.01))
#    author2 = [Publication(0, 20, 0.3)]
#    return [Author(author1, 1), Author(author2, 1)]


def main():
    authors = Data("filozofia-input.txt")
    for author in authors:
        for publication in author.publications:
            print(publication.id, end = ' ')
        print()

if __name__ == "__main__":
    main()
