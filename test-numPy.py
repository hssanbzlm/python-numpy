import numpy as np

"L = [1, 2, 3]"

"A = np.array([1, 2, 3])"
"for e in L:"
"    print(e)"
"for e in A:"
"    print(e)"

"L.append(4)"
"print(L)"

"print(A + np.array([4, 5,6]))"
"print(np.exp(A))"

a = np.array([1, 2])
b = np.array([3, 4])
dot = 0

for e, f in zip(a, b):
    dot += e * f

    print(dot)

print(np.dot(a,b))
print(a.dot(b))
"these two are the same : longueur d'un vecteur"
print(np.sqrt(a.dot(a)))
print(np.linalg.norm(a))

cosangle=a.dot(b) / (np.linalg.norm(a)* np.linalg.norm(b))
print(cosangle)
angle=np.arccos(cosangle)
print(angle)


"matrices"
L=[[1,2],[3,4]]
print(L)

A=np.array([[1,2],[3,4]])
print(A)
print(A[:,0])
print(A.T)
print(np.exp(A))
B=np.array([[1,2,3],[4,5,6]])
print(A.dot(B))
"determinant"
print(np.linalg.det(A))
"Inverse"
print(np.linalg.inv(A))
"solving linear systems"
A=np.array([[1,1],[1.5,4]])
B=np.array([2200,5050])
print(np.linalg.solve(A,B))
A=np.zeros((2,3))
print(A)
A=np.ones((2,3))*10
print(A)

"identity matrix"
print(np.eye(3))
"random number"
print(np.random.random())
"random matrices"
print(np.random.random((2,3)))

R=np.random.randn(1000)
print(R.mean())

"variance"
print(R.var())

"standard variation"
print(R.std())

R=np.random.rand(1000,3)
print(R.mean(axis=0))
print(np.cov(R))

print(np.random.randint(20,500,size=(3,3)))