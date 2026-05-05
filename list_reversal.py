#Code to reverse the list in-place without using slicing or reversed()

l=[1,2,3,4,5,6,7,8,9]
a,b=0,len(l)-1
while a<b:
     l[a],l[b]=l[b],l[a] #swapping
     a+=1
     b-=1
print(l)


#Code to reverse the list in-place using slicing

l=[1,2,3,4,5,6,7,8,9]
print(l[::-1])


#Code to reverse the list in-place using reversed()

l=[1,2,3,4,5,6,7,8,9]
a=list(reversed(l))
print(a)
