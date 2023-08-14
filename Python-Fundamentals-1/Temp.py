def find_winner(votes):
    """
    Args:
     votes(list_str)
    Returns:
     str
    """
    results = {}
    for i in range(len(votes)):
        if votes[i] in results.keys():
            results[votes[i]] += 1
        else:
            results[votes[i]] = 1

    max_value = max(results.values())
    winner = []

    for j, k in results.items():
        if k == max_value:
            winner.append(j)
    winner.sort()
    return winner[0]


votes1 = ['sam', 'john', 'jamie', 'sam']
print(find_winner(votes1))
