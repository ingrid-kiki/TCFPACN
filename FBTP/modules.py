# coding=utf-8

import numpy as np




def cal_similarity(network_name, player_attributes):
    """
    :params player_attributes --> dict()
        player id : [team, nationality]
	
- Calculates the similarity matrix between players (similarity).
Receive:
--> network_name: Network name (Back or Forward) for display purposes.
--> player_attributes: Dictionary with the attributes of each player (team and nationality).
- For each pair of players, calculate the Jaccard similarity
    (jaccard(attr_i, attr_j)), which measures the proportion of attributes in common between two players.
- Fills the similarity matrix with the calculated similarities
    (symmetric, since sim(i, j) = sim(j, i)).
- Calculates and displays the density of the adjacency matrix, which indicates
    the proportion of existing connections in relation to the total possible.
    """

    no = len(player_attributes)
    similarity = np.zeros((no, no))
    edge = 0

    for i in range(0, no-1):
        attr_i = player_attributes[i]
        for j in range(i, no-1):
            attr_j = player_attributes[j]
            sim = jaccard(attr_i, attr_j)  # calculate the similarity
            if sim > 0:
                edge += 1
            similarity[i][j] = sim
            similarity[j][i] = sim  # sim(i,j) = sim(j,i)

    density = (edge*2) / (no*no)  # the density of the players' adjacent matrix
    edge = edge - no

    print("The %s network includes %d vertex and %d edges, the density is %f" 
          % (network_name, no, edge, density)
         )

    return similarity


def jaccard(array_1, array_2):
"""
- Auxiliary function that calculates the Jaccard similarity between two attribute arrays.
- Finds the intersection and union of arrays.
- Returns the ratio between the intersection size and the union size.
"""
    inter = [val for val in array_1 if val in array_2] 
    union = list(set(array_1).union(set(array_2)))
    ja = len(inter) / len(union)
    return ja


def cal_ability_avg(player_abilities_name):
"""
- Calculates the average of each player's abilities (ability_avg) for each ability present in player_abilities_name.
Receive:
--> player_abilities_name: Dictionary with each player's abilities.

- For each skill:
--> Adds up the skill values for all players.
--> Divide the sum by the number of players to obtain the average.
"""

    ability_avg = {}

    for ability in player_abilities_name:
        total = 0
        c = 0
        for value in player_abilities_name[ability].values():
            total = total + value
            c += 1
        ability_avg[ability] = total / c

    return ability_avg
