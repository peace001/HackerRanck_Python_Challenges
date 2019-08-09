"""author = Rockefeller"""


def miniMaxSum(arr):
    Max = sum(sorted(arr , reverse = True)[:-1])
    Min = sum(sorted(arr)[:-1])
    return print(Min , Max)
