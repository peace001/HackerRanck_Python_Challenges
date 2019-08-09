"""author = Rockefeller"""


def compareTriplets(a, b):
    cA  , cB , cD =  0 , 0 , 0
    for i in range(len(a)):
        if a[i]> b[i]:
            cA+=1
        elif a[i]< b[i]:
            cB +=1
        else:
            cD+= 1  
    return [cA , cB]
