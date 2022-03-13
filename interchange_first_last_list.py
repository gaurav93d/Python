

def swapNum(newlist):
    print(newlist)
    a=newlist.pop()
    b=newlist.pop(0)
    newlist.append(b)
    newlist.insert(0,a)
    print(newlist)
    return newlist
    
my = [1,2,3,4,5]
swapNum(my)

#2nd approch:


def swapNum(newlist):
    print(newlist)
    get  = newlist[0],newlist[-1]
    newlist[-1],newlist[0] = get
    print(newlist)

    
my = [1,2,3,4,5]
swapNum(my)

