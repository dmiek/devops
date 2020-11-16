""" Module to evaluate if card is OK to remove or not. """


A = 14
K = 13
Q = 12
J = 11
T = 10


def OK_to_remove(row, pos):
    """ Method to evaluate if card is OK to remove or not. """
    # check if there is anything to remove
    # void:
    if len(row) == 0:
        print('row is void, nothing to remove')
        status_ok = 0
        return status_ok

    # position empty:
    if row[pos] == '- ':
        print('position empty, nothing to remove')
        status_ok = 0
        return status_ok


    # get the colour and rank of the card
    colour = row[pos][1]
    rank = row[pos][0]
    row.pop(pos)

    # convert rank to int value
    if rank == 'A':
        rank = A
    elif rank == 'K':
        rank = K
    elif rank == 'Q':
        rank = Q
    elif rank == 'J':
        rank = J
    elif rank == 'T':
        rank = T
    else:
        rank = int(rank)

    # is there any other card of the same colour as the card to be removed?
    gov_colour = []
    gov_rank = []
    for i in range(len(row)):
        if row[i][1] == colour:
            gov_colour.append(row[i])
    if len(gov_colour) == 0:
        status_ok = 0
        return status_ok

    # check the ranks of the cards of the same colour
    for j in range(len(gov_colour)):
        gov_rank.append(gov_colour[j][0])
    for k in range(len(gov_rank)):
        if gov_rank[k] == 'A':
            gov_rank[k] = A
        elif gov_rank[k] == 'K':
            gov_rank[k] = K
        elif gov_rank[k] == 'Q':
            gov_rank[k] = Q
        elif gov_rank[k] == 'J':
            gov_rank[k] = J
        elif gov_rank[k] == 'T':
            gov_rank[k] = T
        else:
            gov_rank[k] = int(gov_rank[k])

    # check if any value of the other cards exceed
    for m in range(len(gov_rank)):
        if gov_rank[m] > rank:
            print('card OK to remove')
            status_ok = 1
            return status_ok
    print('card NOK to remove')
    status_ok = 0
    return status_ok

rows = ['TS', '- ', '2H', 'KD']
test = OK_to_remove(rows, 1)
print(test)
