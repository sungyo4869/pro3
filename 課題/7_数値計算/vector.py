import numpy

def ex1():
    O = numpy.array([0., 0., 0.])
    P = numpy.array([1., 4., -3.])
    Q = numpy.array([-1., 3., 2.])
        
    OP = numpy.sqrt(numpy.sum((O - P)**2))
    PQ = numpy.sqrt(numpy.sum((P - Q)**2))

    print("---(1-1)---")
    print(OP)

    print("---(1-2)---")
    print(PQ)
    print()

def ex2():
    vector_a = numpy.array([1, 2, 3])
    vector_b = numpy.array([2, 3, 1])
    vector_c = numpy.array([3, 1, 2])

    print("---(2-1)---")
    print(numpy.sqrt(numpy.sum(vector_c ** 2)))

    print("---(2-2)---")
    print(vector_a + vector_b)

    print("---(2-3)---")
    print(vector_a + vector_b + vector_c)

    print("---(2-4)---")
    print(vector_a + 2 * vector_b - 3 * vector_c)

    print("---(2-5)---")
    a_sub_b = vector_a - vector_b
    c_sub_b = vector_c - vector_b
    vector_d = vector_b + a_sub_b + c_sub_b
    print(vector_d)
    print()

def ex3():
    vector_a = numpy.array([1, 1, 0])
    vector_b = numpy.array([2, 0, 2])

    print("---(3-1)---")
    absolute_value_a = numpy.sqrt(numpy.sum(vector_a ** 2))
    print(absolute_value_a)

    print("---(3-2)---")
    absolute_value_b = numpy.sqrt(numpy.sum(vector_b ** 2))
    print(absolute_value_b)

    print("---(3-3)---")
    print(numpy.dot(vector_a, vector_b))

    print("---(3-4)---")
    dot_a_b_cos = numpy.sum(vector_a*vector_b) / (absolute_value_a*absolute_value_b)
    print(numpy.rad2deg(numpy.arccos(dot_a_b_cos)))

    print("---(3-5)---")
    cross_a_b = numpy.cross(vector_a, vector_b)
    absolute_value_cross_a_b = numpy.sqrt(numpy.sum(cross_a_b ** 2))

    vector_c = cross_a_b / absolute_value_cross_a_b
    print(vector_c)
    print(-1 * vector_c)

ex1()
ex2()
ex3()

  