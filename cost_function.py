#! python3

from chromosome import Chromosome
from data import Data


class EndOfCalculations(Exception):

    def __init__(self, max_history):
        self.max_history = max_history


class CostCalculationsSupervisor:
    _k = 0
    _max = 0
    _call_count = 0
    _max_history = list()
    _tresholds = set()
    _stop_treshold = 0

    @staticmethod
    def set_k(k):
        CostCalculationsSupervisor._k = k
        CostCalculationsSupervisor._tresholds = {pow(10, t) * k for t in range(0, 3)}
        CostCalculationsSupervisor._stop_treshold = pow(10, 3) * k

    @staticmethod
    def update_max(new_value):
        if new_value > CostCalculationsSupervisor._max:
            CostCalculationsSupervisor._max = new_value
        if CostCalculationsSupervisor._call_count in CostCalculationsSupervisor._tresholds:
            CostCalculationsSupervisor._max_history.append(CostCalculationsSupervisor._max)

    @staticmethod
    def increase_call_count():
        if CostCalculationsSupervisor._k == 0:
            return
        CostCalculationsSupervisor._call_count += 1
        if CostCalculationsSupervisor._call_count == CostCalculationsSupervisor._stop_treshold + 1:
            raise EndOfCalculations(CostCalculationsSupervisor._max_history)


def log_call(func):
    def count_call(*args, **kwargs):
        call_result = func(*args, **kwargs)
        CostCalculationsSupervisor.increase_call_count()
        CostCalculationsSupervisor.update_max(call_result)
        return call_result

    return count_call


# metoda licząca punkty za publikacje wchodzące w skład chromosomu
# kara za niespełnienie warunków
@log_call
def calculate_points(chromosome: Chromosome, data: Data):
    total_share = 0
    total_points = 0
    for i, gene in enumerate(chromosome.chromosome):
        points = 0
        share = 0
        monograph_share = 0
        for j, subgene in enumerate(gene):
            points += subgene * data[i][j].points
            share += subgene * data[i][j].share
            monograph_share += subgene * data[i][j].share * data[i][j].is_monograph
        share_overflow = max(share - 4 * data[i].share_ratio, 0)
        monograph_share_overflow = max(monograph_share - 2 * data[i].share_ratio, 0)
        points -= share_overflow * 2.5 + monograph_share_overflow * 2.5
        total_points += points
        total_share += share
    total_share_overflow = max(total_share - 3 * data.get_N(), 0)
    total_points -= total_share_overflow * 2.5
    return total_points

@log_call
def calculate_points_with_repair(chromosome: Chromosome, data: Data):
    total_share = 0
    total_points = 0
    for i, gene in enumerate(chromosome.chromosome):
        points = 0
        share = 0
        monograph_share = 0
        for j, subgene in enumerate(gene):
            if data[i][j].is_monograph:
                if share + subgene * data[i][j].share < 4 * data[i].share_ratio and monograph_share + subgene * data[i][
                    j].share < 2 * data[i].share_ratio:
                    points += subgene * data[i][j].points
                    share += subgene * data[i][j].share
                    monograph_share += subgene * data[i][j].share
                else:
                    gene[j] = 0
            else:
                if share + subgene * data[i][j].share < 4 * data[i].share_ratio:
                    points += subgene * data[i][j].points
                    share += subgene * data[i][j].share
                else:
                    gene[j] = 0
        total_points += points
        total_share += share
    while total_share > 3 * data.get_N():
        worst_i, worst_j = delete_worst(chromosome, data)
        total_share -= data[worst_i][worst_j].share
        total_points -= data[worst_i][worst_j].points
    return total_points


def delete_worst(chromosome: Chromosome, data: Data):
    worst = 1000000
    worst_i = 0
    worst_j = 0
    for i, gene in enumerate(chromosome.chromosome):
        for j, subgene in enumerate(gene):
            if data[i][j].ratio < worst and subgene == 1:
                worst = data[i][j]
                worst_i, worst_j = (i, j)
    chromosome[worst_i][worst_j] = 0
    return worst_i, worst_j
