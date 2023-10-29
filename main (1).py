Main

#3.set operations
A={1,2}
B={2,3,4,5}
print ("A set=",A)
print ("B set=",B)
print ("SET OPERATIONS")
print ("length of set A=",len(A))
print ("maximum value of set B:",max(B))
print ("minimum value of set A:",max(A))
print ("set A union B=", A.union(B))
print ("set A intersection B=", A.intersection(B))
print ("set A difference B=", A.difference(B))
print ("A symmetric difference B=", A.symmetric_difference (B))
print ("set A is subset of B:", A.issubset(B))
print ("A is superset of B:", A.issuperset(B))
newv=input ('Enter the new value to add=')
A.add(newv)
print ("After Adding new element to set A:", A)
B.remove(4)
print ("After Deleting 4 from set B",B)