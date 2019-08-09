
"""author = Rockefeller"""


def staircase(n):
    a = []
    #x = "{:>4}\n" * n
    for i in range(1 , n+1):
        a.append(('#' * i))
    max_length = max(len(i) for i in a )
    for item in a:
        print('{0:>{1}}'.format(item, max_length))
