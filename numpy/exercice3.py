import numpy as np

# Définition de 2 matrices compatibles pour la multiplication
A = np.array([[1, 2], [3, 4]])  # Matrice 2x2
B = np.array([[5, 6], [7, 8]])  # Matrice 2x2

# Multiplication Matrice x Matrice
C = np.dot(A, B)  # Ou A @ B
print("Multiplication de A et B :\n", C)

# Définition d'une matrice et d'un vecteur

A = np.array([[1, 2], [3, 4]])  # Matrice 2x2
v = np.array([5, 6])  # Vecteur 1D

# Multiplication Matrice x Vecteur
result = np.dot(A, v)  # Ou A @ v
print("Multiplication de A par le vecteur v :\n", result)

# Définition d'une matrice carrée inversible
A = np.array([[4, 7], [2, 6]])

# Calcul de l'inverse de A
A_inv = np.linalg.inv(A)
print("Inverse de A :\n", A_inv)

# Vérification : A * A_inv doit donner l'identité
I = np.dot(A, A_inv)
print("Vérification A * A_inv :\n", I)


A = np.array([[4, 7], [2, 6]])
det_A = np.linalg.det(A)
print("Déterminant de A :", det_A)
# Rmrq: Si la matrice n'est pas inversible (déterminant = 0)
# np.linalg.inv(A) lève une erreur.

# Transposée d’une matrice
A = np.array([[1, 2, 3], [4, 5, 6]])
A_T = A.T  # Ou np.transpose(A)
print("Transposée de A :\n", A_T)

#  Valeurs et vecteurs propres: sont utilisés en algèbre linéaire, par exemple en PCA (réduction de dimension).
A = np.array([[2, -1], [-1, 2]])
valeurs_propres, vecteurs_propres = np.linalg.eig(A)

print("Valeurs propres :\n", valeurs_propres)
print("Vecteurs propres :\n", vecteurs_propres)

# Produit de Kronecker : est un produit spécial qui duplique les structures des matrices.
A = np.array([[1, 2], [3, 4]])
B = np.array([[0, 5], [6, 7]])
kronecker = np.kron(A, B)
print("Produit de Kronecker de A et B :\n", kronecker)

# Pseudo-inverse (Matrice Moore-Penrose) : pour les matrices non inversibles ou rectangulaires.
A = np.array([[1, 2, 3], [4, 5, 6]])
A_pinv = np.linalg.pinv(A)
print("Pseudo-inverse de A :\n", A_pinv)
