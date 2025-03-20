import numpy as np

# 1️⃣ Création du tableau A (3 lignes, 4 colonnes)
A = np.arange(1, 13).reshape(3, 4)
print("Matrice A :\n", A)

# 2️⃣ Accès aux éléments
print("Élément ligne 2, colonne 3 :", A[1, 2])  # Index (1,2) en NumPy
print("Dernière colonne :\n", A[:, -1])  # Toutes les lignes, dernière colonne
print("Deuxième ligne :\n", A[1, :])  # Ligne 2 entière
print("Éléments pairs de A :\n", A[A % 2 == 0])  # Filtrer les éléments pairs

# 3️⃣ Opérations mathématiques
A_mult = A * 2
print("A multiplié par 2 :\n", A_mult)

print("Moyenne de A :", A.mean())
print("Écart-type de A :", A.std())

# Remplacement des nombres impairs par -1
A[A % 2 == 1] = -1
print("A après remplacement des nombres impairs :\n", A)

# 4️⃣ Manipulations avancées
I = np.eye(4)  # Matrice identité 4x4
print("Matrice Identité 4x4 :\n", I)

# Concaténation avec un vecteur colonne
B = np.array([100, 200, 300]).reshape(3, 1)  # Transformer B en colonne
A_extended = np.hstack((A, B))  # Concaténation horizontale
print("A après ajout de B :\n", A_extended)

# Exercice : Ajout d'une nouvelle ligne à A_extended contenant [500, 600, 700, 800, 900] avec np.vstack().

# Matrice A_extended existante (3 lignes, 5 colonnes)
A_extended = np.array([
    [-1,  2, -1,  4, 100],
    [-1,  6, -1,  8, 200],
    [-1, 10, -1, 12, 300]
])

# Nouvelle ligne à ajouter
new_row = np.array([500, 600, 700, 800, 900])

# Ajout de la nouvelle ligne avec np.vstack()
A_extended = np.vstack((A_extended, new_row))

# Affichage du résultat
print("Matrice A_extended après ajout de la nouvelle ligne :\n", A_extended)

# np.vstack((A_extended, new_row)) : empile new_row sous A_extended.
# new_row doit avoir le même nombre de colonnes que A_extended, sinon une erreur sera levée.
# La matrice résultante a maintenant 4 lignes et 5 colonnes.