l1=[12,13,14,15]
l2=list(l1)
print(type(l2))
l2[2]=67
l1=tuple(l2)
print(l1)