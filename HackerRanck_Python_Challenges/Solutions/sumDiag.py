"""author = Rockefeller"""



Given a square matrix, calculate the absolute difference between the sums of its diagonals.

def diagonalDifference(arr):
    a , b  = [] , []
    for i in range(len(arr[0])):
        a.append(arr[i][i])
        b.append(arr[i][-1-i])
    return abs(sum(a) - sum(b))
