def minNum(list):
    min = list[0]
    for i in list:
        if (i < min):
            min = i
    return min
list=[2,24,1,-3,-1]
min=minNum(list)
secMin = list[0]
for i in list:
    if (i > min and i<secMin):
        secMin = i
print(secMin)
