import os
from multiprocessing import Process
from main import main
import params


def pr(name):
    print(name)


def test():
    test_files = os.listdir("./input_data")
    processes = list()
    for test_file in test_files:
        p = Process(target=pr, args=("input_data/" + test_file,))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()


if __name__ == '__main__':
    test()
