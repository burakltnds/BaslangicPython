import numpy as np
#matris toplama - çıkarma
matrixList = [[1,5,7],[4,7,9],[10,13,8]]
matrix2List = [[2,6,9],[7,9,11],[13,18,10]]
matrix=np.array(matrixList)
matrix2=np.array(matrix2List)
print(matrix2+matrix)
#matris elelman çağırma
print(matrix[0,1])
#şeklini göster
print(matrix.shape)