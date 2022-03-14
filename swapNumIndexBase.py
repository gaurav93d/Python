def swapListValues(list1, pos1,pos2):
    list1[pos1], list1[pos2] = list1[pos2], list1[pos1]
    return list1

l = [10,20,30,40,50,60,70]
print("before swap",l)
pos1, pos2 = 2, 5

print("after swap",swapListValues(l, pos1,pos2))


# we can aslo use pop function

l = [10,20,30,40,50,60,70]
print("before swap", l)
a= l.pop(2)
b= l.pop(3)

l.insert(2,a)
l.insert(3,b)
print("after swap",l)

#output= before swap [10, 20, 30, 40, 50, 60, 70]
#after swap [10, 20, 30, 50, 40, 60, 70]
