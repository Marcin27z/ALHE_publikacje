#! python3

from publication import Publication
from data import Data, Author
from algorithm import algorithm
import params

def main():
    authors = Data(params.FILENAME)
    result = algorithm(authors)

    for author_number, author in enumerate(authors):
        print(author.id, end=': [ ')
        for publication_number, publication in enumerate(author.publications):
            if result[author_number][publication_number] == 1:
                print(publication.id, end = ' ')
        print(']')

if __name__ == "__main__":
    main()
