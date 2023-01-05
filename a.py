import numpy as np

A=np.array([[2,3,4],[4,5,7],[8,4,2]])
B=np.array([[2,6,4],[2,5,7],[8,6,2]])
print("\nFirst Array\n")
print(A)
print("\nSecond  Array\n")
print(B)
Atrans=np.transpose(A)
Btrans=np.transpose(B)

Af=np.matmul(A,Atrans)
B2=2*B
BB=np.matmul(B2,Btrans)
final=Af-BB
print("\n\nResult \n")
print(final)