#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def ranksort(rank):
    for i in range(len(rank)):
        for j in range(i+1, len(rank)):
            if rank[i] < rank[j]:
                temp = rank[i]
                rank[i] = rank[j]
                rank[j] = temp
    # print(rank)
    return rank


def ranking(q, ranked, l):
    count = 0
    for i in range(len(ranked)):
        if (count == 0):
            count = 1
        elif (ranked[i] != ranked[i-1]):
            count += 1

        if q == ranked[i]:
            return count
        if q > ranked[i]:
            return count
    # if len(ranked) < l:
    #     for i in range(l-len(ranked)):
    #         return count+1

    return count+1


def climbingLeaderboard(ranked, player):

    ranked = ranksort(ranked)

    arr = []
    for i in range(len(player)):
        arr.append(ranking(player[i], ranked, len(player)))
    return arr

    # Write your code here


if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
