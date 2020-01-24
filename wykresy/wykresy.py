import re
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import math
from statistics import stdev
from mpl_toolkits.mplot3d import Axes3D


def average(values: list):
    return sum(values) / len(values)


def standard_deviation(values: list):
    return math.sqrt(
        # (len(values) / (len(values) + 1)) *
        average([x ** 2 for x in values]) - (average(values) ** 2))


def max_in_file(file_name, number=4):
    data = defaultdict(list)
    for i in range(1, number + 1):
        if number != 1:
            part = str(i)
        else:
            part = ""
        with open(file_name + part, mode='r') as file:
            lines = file.readlines()
            for line in lines:
                values = [float(n) for n in re.findall(r'\b\d+.?\d*\b', line)]
                if len(values) == 2:
                    data[values[0]].append(values[1])
    print(file_name)
    print(max([max(d[1]) for d in data.items()]))


def plot_files_points(file_name, number=4, begin=3, end=None, color=None, marker='.'):
    data = defaultdict(list)
    for i in range(1, number + 1):
        if number != 1:
            part = str(i)
        else:
            part = ""
        with open(file_name + part, mode='r') as file:
            lines = file.readlines()
            for line in lines:
                values = [float(n) for n in re.findall(r'\b\d+.?\d*\b', line)]
                if len(values) == 2:
                    data[values[0]].append(values[1])
    result = list(map(lambda entry: list(map(lambda value: (entry[0], value), entry[1])), data.items()))
    none_x, none_y = zip(*result[0])
    all_x, all_y = zip(*result[1])
    best_x, best_y = zip(*result[2])
    random_x, random_y = zip(*result[3])
    result2 = list(zip(result[0], result[1], result[2], result[3]))
    none = list(zip(*result2[0]))
    all = list(zip(*result2[1]))
    best = list(zip(*result2[2]))
    random = [list(zip(*result2[i])) for i in range(3, 28)]
    plt.scatter(none[0], none[1], label="None", marker="*")
    plt.scatter(all[0], all[1], label="All", marker="^")
    plt.scatter(best[0], best[1], label="Best", marker="+")
    plt.scatter([item for sublist in list(map(lambda x: x[0], random[3:])) for item in sublist],
                [item for sublist in list(map(lambda y: y[1], random[3:])) for item in sublist], label="Random",
                marker=".")
    # plt.scatter(none_x, none_y, label="None")
    # plt.scatter(all_x, all_y, label="All")
    # plt.scatter(best_x, best_y, label="Best")
    # plt.scatter(random_x, random_y, label="Random")


def plot_files(file_name, data_label, number=4, begin=3, end=None, color=None, marker='.'):
    data = defaultdict(list)
    for i in range(1, number + 1):
        if number != 1:
            part = str(i)
        else:
            part = ""
        with open(file_name + part, mode='r') as file:
            lines = file.readlines()
            for line in lines:
                values = [float(n) for n in re.findall(r'\b\d+.?\d+\b', line)]
                if len(values) == 2:
                    data[values[0]].append(values[1])
    if end is None or end - begin != 1:
        result = list(
            map(lambda entry: (entry[0], average(entry[1][begin:end]), stdev(entry[1][begin:end])), data.items()))
        x, y, e = zip(*result)
        plt.errorbar(x, y, e, linestyle='None', marker=marker, label=data_label)
    else:
        result = list(map(lambda entry: (entry[0], average(entry[1][begin:end])), data.items()))
        x, y = zip(*result)
        plt.scatter(x, y, linestyle='None', marker='.', label=data_label, c=color)


# def matematyka_all():
#     plt.title("Matematyka - porównanie punktów startowych(kara)")
#     plot_files("../logs/matematyka/matematyka-output-1-20-part", "Żadne", 2, 0, 1, 'r', '.')
#     plot_files("../logs/matematyka/matematyka-output-1-20-part", "Wszystkie", 2, 1, 2, 'g', '*')
#     plot_files("../logs/matematyka/matematyka-output-1-20-part", "Najlepsze", 2, 3, 4, 'b', '+')
#     plot_files("../logs/matematyka/matematyka-output-1-20-part", "Losowe", 2, 5, None, 'm', '^')

def filozofia_repair():
    plt.title("Filozofia - naprawa")
    plot_files("../logs/filozofia/filozofia_naprawa_", None, 2)


def filozofia_kara():
    plt.title("Filozofia - kara")
    plot_files("../logs/filozofia/filozofia-output-1-20-part", None)


def matematyka_repair_vs_punishment():
    plt.title("Matematyka - porównanie naprawy i kary")
    plot_files("../logs/matematyka/matematyka-output-1-20-repair-part", "Naprawa")
    plot_files("../logs/matematyka/matematyka-output-1-20-part", "Kara")


def informatyka_repair_vs_punishment():
    plt.title("Informatyka techniczna i telekomunikacja - porównanie naprawy i kary")
    plot_files("../logs/informatyka/itt", "Kara")
    plot_files("../logs/informatyka/informatyka_techniczna_telekomunikacja_naprawa_", "Naprawa")


def informatyka_20_vs_300():
    plt.title("Informatyka techniczna i telekomunikacja \n porównanie 20 i 300 chromosomów")
    plot_files("../logs/informatyka/itt", "20 chromosomów")
    plot_files("../logs/informatyka/informatyka_techniczna_telekomunikacja-output-1-300", "300 chromosomów", 1)


def matematyka_20_vs_300():
    plt.title("Matematyka - porównanie 20 i 300 chromosomów")
    plot_files("../logs/matematyka/matematyka-output-1-300-part", "300 chromosomów")
    # plot_files("../logs/matematyka/matematyka-output-1-20-repair-part", "20 chromosomów naprawa")
    plot_files("../logs/matematyka/matematyka-output-1-20-part", "20 chromosomów")


def nauki_fizyczne_all():
    plt.title("Nauki fizyczne - wartość funkcji celu")
    plot_files_points("../logs/nauki_fizyczne/nauki_fizyczne-output-1-300", 1)


def matematyka_all():
    plt.title("Matematyka - wartości funkcji celu")
    plot_files_points("../logs/matematyka/matematyka-output-1-300-part", 4)


def inzynieria_srodowiska_all():
    plt.title("Inżynieria środowiska - wartości funkcji celu")
    plot_files_points("../logs/inzynieria_srodowiska/inzynieria_srodowiska_gornictwo_energetyka-output-1-300", 1)


def inzynieria_materialowa_all():
    plt.title("Inżynieria materiałowa - wartości funkcji celu")
    plot_files_points("../logs/inzynieria_materiałowa/inzynieria_materialowa.txt", 1)


def inzynieria_mechaniczna_all():
    plt.title("Inżynieria mechaniczna - wartości funkcji celu")
    plot_files_points("../logs/inzynieria_mechaniczna/inzynieria_mechaniczna-output-1-300", 1)


def inzynieria_ladowa_transport():
    plt.title("Inżynieria lądowa transport - wartości funkcji celu")
    plot_files_points("../logs/inzynieria_ladowa_transport/inzynieria_ladowa_transport-output-1-300", 1)


def inzynieria_chemiczna():
    plt.title("Inżynieria chemiczna - wartości funkcji celu")
    plot_files_points("../logs/inzynieria_chemiczna/inzynieria_chemiczna.txt", 1)


def inzynieria_biomedyczna():
    plt.title("Inżynieria biomedyczna - wartości funkcji celu")
    plot_files_points("../logs/inzynieria_biomedyczna/inzynieria_biomedyczna.txt", 1)


def informatyka_all():
    plt.title("Informatyka techniczna telekomunikacja - wartości funkcji celu")
    plot_files_points("../logs/informatyka/informatyka_techniczna_telekomunikacja-output-1-300", 1)


def filozofia_all():
    plt.title("Filozofia - wartości funkcji celu")
    plot_files_points("../logs/filozofia/filozofia-output-1-20-part", 4)


def automatyka_all():
    plt.title("Filozofia - wartości funkcji celu")
    plot_files_points("../logs/automatyka/automatyka_elektronika_elektrotechnika-output-1-300", 1)


def architektura_all():
    plt.title("Architektura urbanistyka - wartości funkcji celu")
    plot_files_points("../logs/architektura_urbanistyka/architektura_urbanistyka.txt", 1)

def maxes():
    max_in_file("../logs/architektura_urbanistyka/architektura_urbanistyka.txt", 1)
    max_in_file("../logs/automatyka/automatyka_elektronika_elektrotechnika-output-1-300", 1)
    max_in_file("../logs/filozofia/filozofia-output-1-20-part", 4)
    max_in_file("../logs/informatyka/informatyka_techniczna_telekomunikacja-output-1-300", 1)
    max_in_file("../logs/inzynieria_biomedyczna/inzynieria_biomedyczna.txt", 1)
    max_in_file("../logs/inzynieria_chemiczna/inzynieria_chemiczna.txt", 1)
    max_in_file("../logs/inzynieria_ladowa_transport/inzynieria_ladowa_transport-output-1-300", 1)
    max_in_file("../logs/inzynieria_mechaniczna/inzynieria_mechaniczna-output-1-300", 1)
    max_in_file("../logs/inzynieria_materiałowa/inzynieria_materialowa.txt", 1)
    max_in_file("../logs/inzynieria_srodowiska/inzynieria_srodowiska_gornictwo_energetyka-output-1-300", 1)
    max_in_file("../logs/matematyka/matematyka-output-1-300-part", 4)
    max_in_file("../logs/nauki_fizyczne/nauki_fizyczne-output-1-300", 1)

if __name__ == '__main__':
    # plot_files("../logs/matematyka-output-1-50-part", "50 chromosomów")
    # plot_files("../logs/matematyka-output-1-20-part", "20 chromosomów")
    # plot_files("../logs/matematyka-output-1-100-part", "100 chromosomów")
    # plot_files("../logs/matematyka-output-1-200-part", "200 chromosomów")
    # plot_files("../logs/matematyka-output-1-1000-part", "1000 chromosomów")
    # plot_files("../logs/matematyka-output-1-300-part", "300 chromosomów")
    # plot_files("../logs/matematyka-output-2-300-cmp30-part", "30")
    # plot_files("../logs/matematyka-output-1-300-part", "70")
    # plot_files("../logs/matematyka-output-3-300-cmp85-part", "85")

    # matematyka_all()
    # inzynieria_ladowa_transport()
    # inzynieria_mechaniczna_all()
    # inzynieria_materialowa_all()
    # inzynieria_chemiczna()
    # inzynieria_biomedyczna()
    # inzynieria_srodowiska_all()
    # architektura_all()
    # nauki_fizyczne_all()
    # filozofia_all()
    # filozofia_repair()
    # filozofia_kara()
    # matematyka_repair_vs_punishment()
    # informatyka_repair_vs_punishment()
    # informatyka_20_vs_300()
    # matematyka_20_vs_300()

    # maxes()

    plt.xlabel("Liczba wywołań funkcji celu")
    plt.ylabel("Wartość funkcji celu")
    plt.grid()
    plt.xscale('log')
    plt.legend(loc="lower right")
    plt.show()
