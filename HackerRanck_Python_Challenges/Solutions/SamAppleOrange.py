"""author = Rockefeller"""



def countApplesAndOranges(s, t, a, b, apples, oranges):
    sam = list(range(s , t+1))
    FruitsCount = [len(apples) ,  len(oranges)]
    l1 = [a + apple for apple in apples]
    l2 = [b + orange for orange in oranges]
    f1 = [i for i in l1 if i in sam]
    f2 = [j for j in l2 if j in sam]
    return print( len(f1)), print(  len(f2))
