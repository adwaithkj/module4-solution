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


def playersort(player):
    for i in range(len(player)):
        for j in range(i+1, len(player)):
            if player[i] < player[j]:
                temp = player[i]
                player[j] = player[i]
                player[i] = temp
    return player


def ranking(q, ranked):
    count = 0
    for i in range(len(ranked)):
        # print("count:" + str(count))
        if (ranked[i] != ranked[i-1]):
            count += 1

        if q >= ranked[i]:
            return count
    return count+1


def climbingLeaderboard(ranked, player):
    arr = []
    for i in range(len(player)):
        arr.append(ranking(player[i], ranked))

    return arr

    # Write your code here


if __name__ == '__main__':

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print('\n'.join(map(str, result)))
