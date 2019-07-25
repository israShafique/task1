str1=input("enter string: ")
countNum=0
countStr=0
for i in str1:
    if(i>='0'and i<='9'):
        countNum=countNum+1
    elif((i>='a'and i<='z')or (i>='A'and i<='Z')):
        countStr=countStr+1

print("numbers: "+str(countNum))
print("characters: "+ str(countStr))
