#! python3

from publication import Publication
from data import Data, Author
from algorithm import algorithm
import params
from file_logger import FileLogger


def main():
    run_algorithm(params.FILENAME)


def run_algorithm(file_name):
    logger = FileLogger(file_name)
    authors = Data(file_name)
    logger.log_K(sum(authors.get_publications_numbers()))
    history, result = algorithm(authors)
    logger.log_max_list(history)
    logger.log_result(result.chromosome)

    for author_number, author in enumerate(authors):
        print(author.id, end=': [ ')
        for publication_number, publication in enumerate(author.publications):
            if result[author_number][publication_number] == 1:
                print(publication.id, end=' ')
        print(']')


if __name__ == "__main__":
    main()
