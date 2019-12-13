#! python3

from chromosome import Chromosome
from data import Data


# calculate points for publication in chromosome
# reduce points if shares don't meet constraints
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

# def calculate_points2(chromosome, publications):
#     def calculate(args):
#         subgene, i, j = args
#         return subgene * publications[i][j].points, subgene * publications[i][j].share
#
#     total_cost = 0
#     total_points = 0
#     for i, gene in enumerate(chromosome):
#         points, cost = reduce(lambda a, b: (a[0] + b[0], a[1] + b[1]),
#                               map(calculate, [(subgene, i, j) for j, subgene in enumerate(gene)]))
#         cost_overflow = max(cost - 400, 0)
#         points -= cost_overflow * 2.5
#         total_points += points
#         total_cost += cost
#
#     total_cost_overflow = max(total_cost - len(chromosome) * 300, 0)
#     total_points -= total_cost_overflow * 2.5
#     return total_points


# for i, gene in enumerate(chromosome):
#     points = 0
#     cost = 0
#     # for j in range(len(chromosome[i])):
#     points, cost = [sum(q) for q in zip(*map(calculate, [(subgene, i, j) for j, subgene in enumerate(gene)]))]
#     # points += subgene * publications[i][j].points
#     # cost += subgene * publications[i][j].share
#     cost_overflow = max(cost - 400, 0)
#     points -= cost_overflow * 2.5
#     total_points += points
#     total_cost += cost

# for i, gene in enumerate(chromosome):
#     points = 0
#     cost = 0
#     # for j in range(len(chromosome[i])):
#     for j, subgene in enumerate(gene):
#         points += subgene * publications[i][j].points
#         cost += subgene * publications[i][j].share
#     cost_overflow = max(cost - 400, 0)
#     points -= cost_overflow * 2.5
#     total_points += points
#     total_cost += cost

# def calculate_points(chromosome: Chromosome, data: Data):
#     total_cost = 0
#     total_points = 0
#     for author in zip(chromosome.chromosome, data):
#         points, cost = [sum(i) for i in zip(*[(v * p.points, v * p.share) for (v, p) in zip(*author)])]
#         cost_overflow = max(cost - 4 * author[1].share_ratio, 0)
#         points -= cost_overflow * 2.5
#         total_points += points
#         total_cost += cost
#
#     total_cost_overflow = max(total_cost - len(chromosome.chromosome) * 3 * data.get_total_share_available(), 0)
#     total_points -= total_cost_overflow * 2.5
#     return total_points
