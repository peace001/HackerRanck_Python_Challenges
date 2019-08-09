"""author = Rockefeller"""

import string
def unik(li):
    el = []
    for i in li:
        if i not in el:
            el.append(i)
    return el
def perm(x , y):

    al = string.ascii_lowercase
    ind = []
    ind2= []
    s_x =unik(x)
    s_y =unik(y)
    for i in range(min(len(s_x) , len(s_y))):
        ind.append(al.index(s_x[i]) - al.index(s_y[i]))
    for x_i , y_i in zip(x , y):
        ind2.append(al.index(x_i) - al.index(y_i))
        
    if  ind==unik(ind2):
        print ("same class")
    else:
        print("different class")
