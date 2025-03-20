import numpy as np

ar = np.array([[1, 2, 3 , 0, 4, 5, 6]])
ar1 = np.array([
    [1, 2, 3 , 8, 115, 6, 0],
    [1, 0, 1 , 7, 11, 1, 1],
    [1, 2, 4 , 14, 5, 6, 223],
    [1, 2, 0 , 255, 5, 1, 455]
    ])
print("size du tab 1 ", ar.size, "shape du tab 1 ", ar.shape, "moyenne de tab 1", ar.mean(), "max de tab 1 ", ar.max())     
print("size du tab 2 ", ar1.size, "shape du tab 2 ", ar1.shape)
print(" --  Elements  -- ")
print(ar1[2][3])
print(ar[-1]) # recupère dernière ligne, ar a 1 seule ligne
print(ar1[3:6])