from itertools import groupby

s = raw_input()
slist=[]
for i in range(len(s)):
    slist.append(s[i])


for key,group in groupby(slist,lambda x:x):
    group=list(group)
    print "(%s, %s)"%(len(group) ,key),