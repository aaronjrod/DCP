def num_attacks(bishops, N):
    total = 0
    board = [[0 for j in range(N)] for i in range(N)]

    for bishop in bishops:
        board[bishop[0]][bishop[1]] = 1

    for s in range(2, (2 * N) + 1):
        count = 0
        i = 1
        j = s - i
        while(max(i, j) <= min(N, s - 1)):
            if board[j][i - j]:
                count += 1
            i += 1
            j -= 1

        if count > 1:
            total += ((count + 1) * count) // 2
        
    for s in range(2, (2 * N) + 1):
        count = 0
        i = 1
        j = s - i
        while(max(i, j) <= min(N, s - 1)):
            if board[i][N - j - 1]:
                count += 1
            i += 1
            j -= 1

        if count > 1:
            total += ((count + 1) * count) // 2
    return total

bishops = [(0, 0),
(1, 2),
(2, 2),
(4, 0),]
print(num_attacks(bishops, 5))