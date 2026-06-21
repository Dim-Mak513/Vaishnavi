import numpy as nm


matrix=nm.array([[1,2,3],[4,5,6],[7,8,9]])
print(type(matrix))
print(matrix)
transpose=matrix.T
transpose1=nm.transpose(matrix)
print(transpose)
print(transpose1)

z=nm.zeros(5)
print(z)
o=nm.ones(6)
print(o)
r=nm.arange(1,6)
print(r)
x=nm.array([10,20,30])
print(x+5)
print(x*2)

m=nm.array([[1,2],[3,4]])
print(m)
print(m.T)
print(m.shape) # rows and columns
print(m.size) # elements of matrix

b=nm.array([1,2,3,4,5,6])
c=b.reshape(2,3)
print(c)
print(c.ndim)
print(nm.max(b))
print(nm.min(b))
print(nm.sum(b))
print(nm.mean(b))
print(b[0])
print(b[2])

# slicing
print(b[1:3])

# matrix multiplication
m1=nm.array([[1,2],[3,4]])
m2=nm.array([[5,6],[7,8]])
print(m1+m2)
print(m1 @ m2) # multiply
print(nm.dot(m1,m2))

p=nm.array([1,5,10,15])
print(p>5) # returns booloean expression 
print(p[p>5]) # filter values