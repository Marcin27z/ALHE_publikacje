#! python3

from publication import Publication
from data import Data, Author
from algorithm import algorithm
import params
from mode import StartingPoint
from file_logger import FileLogger
import sys


def main():
    if len(sys.argv) < 7:
        print("Proszę podać wszystkie argumenty")
        return
    none = int(sys.argv[1])
    all = int(sys.argv[2])
    best = int(sys.argv[3])
    random = int(sys.argv[4])
    input = sys.argv[5]
    output = sys.argv[6]
    run_algorithm(input, output, none, all, best, random)


def run_algorithm(file_name, output, none=0, all=0, best=0, random=0):
    logger = FileLogger(output)
    authors = Data(file_name)
    logger.log_K(sum(authors.get_publications_numbers()))

    for _ in range(none):
        logger.log_start_point(StartingPoint.NONE)
        history, result = algorithm(authors, StartingPoint.NONE)
        logger.log_max_list(history)
        logger.log_result(authors.full_result_for_chromosome(result.chromosome))

    for _ in range(all):
        logger.log_start_point(StartingPoint.ALL)
        history, result = algorithm(authors, StartingPoint.ALL)
        logger.log_max_list(history)
        logger.log_result(authors.full_result_for_chromosome(result.chromosome))

    for _ in range(best):
        logger.log_start_point(StartingPoint.BEST)
        history, result = algorithm(authors, StartingPoint.BEST)
        logger.log_max_list(history)
        logger.log_result(authors.full_result_for_chromosome(result.chromosome))

    for _ in range(random):
        logger.log_start_point(StartingPoint.RANDOM)
        history, result = algorithm(authors, StartingPoint.RANDOM)
        logger.log_max_list(history)
        logger.log_result(authors.full_result_for_chromosome(result.chromosome))

    for author_number, author in enumerate(authors):
        print(author.id, end=': [ ')
        for publication_number, publication in enumerate(author.publications):
            if result[author_number][publication_number] == 1:
                print(publication.id, end=' ')
        print(']')


if __name__ == "__main__":
    main()
