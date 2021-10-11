#str='Runoob'
#temp=(str[::-1])
#temp.join(reversed(str))
#print(temp)
#print(''.join(reversed(str)))


import sys
result=[]
#with open('in-proj0.txt','r') as f:
#    for line in f:
#        result.append(list(line.strip('\n').split(',')))
#print(result)


for line in open("in-proj0.txt"):
    result.append(line.strip('\n'))
print(result)


i=0
for ll in result:
    print("[%d],%s" % (i,ll))
    inp = ll
    i=i+1
print(i)