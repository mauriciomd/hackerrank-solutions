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

def climbingLeaderboard(ranked, player):
    current_position = 1
    current_position_score = ranked[0]
    
    ranked_len = len(ranked)
    player_len = len(player)
    ranked_index = 0
    player_index = player_len - 1
    
    new_players_ranking = []
    is_last_position = False
    
    while player_index >= 0:
        if player[player_index] >= ranked[ranked_index]:
            new_players_ranking.append(current_position)
            player_index -= 1
        elif ranked_index == ranked_len - 1 and player[player_index] <= ranked[ranked_index]:
            
            if not is_last_position:
                current_position += 1
                is_last_position = True
                
            new_players_ranking.append(current_position)
            player_index -= 1
        else:
            if ranked_index < ranked_len - 1:
                ranked_index += 1
        
        if ranked[ranked_index] != current_position_score:
            current_position_score = ranked[ranked_index]
            current_position += 1
            
    return reversed(new_players_ranking)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
