class Matrix:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix_1 = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]

        for el in range(len(self.list_1)):

            for elem in range(len(self.list_2[el])):
                matrix_1[el][elem] = self.list_1[el][elem] + self.list_2[el][elem]

        return str('\n'.join(['\t'.join([str(elem) for elem in el]) for el in matrix_1]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(elem) for elem in el]) for el in matrix_1]))


test_matrix = Matrix([[31, 32, 18],
                      [37, 43, 1],
                      [51, 86, 9]],
                     [[3, 5, 32],
                      [2, 4, 6],
                      [-1, 64, -8]])


print (test_matrix.__add__())

