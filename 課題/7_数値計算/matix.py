import numpy

def ex4():
    A = numpy.array([[1, 2], [3, 4]])
    B = numpy.array([[3, 2], [0, -1]])
    
    print("---(4-1)---")
    print(3 * B)
    print("---(4-2)---")
    print(2 * A - B)
    print("---(4-3)---")
    print(A + B)

    print("---(4-4)---")
    E = numpy.eye(2, dtype="int")
    O = numpy.zeros((2, 2), dtype="int")
    print(E)
    print(O)

def ex5():
    A = numpy.array([[1, 2], [2, 1]])
    B = numpy.array([[1, 1], [2, -1]])
    E = numpy.array([[1, 0], [0, 1]])

    print("---(5-1)---")
    print(numpy.matmul(A, B))
    print("---(5-2)---")
    print(numpy.matmul(A, E))

    A = numpy.array([[1, 2], [0, 1], [1, 0]])
    B = numpy.array([[0, 0, 1], [1, 0, 1], [1, 0, 0]])
    C = numpy.array([[1], [3], [0]])
    D = numpy.array([[0, 1, 0]])

    # エラーハンドリング
    def try_matmul(A, B):
        try:
            print(numpy.matmul(A, B))
        except ValueError:
            print("ValueError")

    print("---(5-3)---")
    try_matmul(B, A)

    print("---(5-4)---")
    try_matmul(D, C)

    print("---(5-5)---")
    try_matmul(A, B)
    
    print("---(5-6)---")
    try_matmul(B, C)

def ex6():
    A = numpy.array([[2, 3], [5, -2]])

    print("---(6-1)---")
    print(A)
    print("---(6-2)---")
    print(numpy.linalg.inv(A))
    print("---(6-3)---")
    left = A
    right = [31, 30]
    print(numpy.linalg.solve(left, right))

ex4()
ex5()
ex6()