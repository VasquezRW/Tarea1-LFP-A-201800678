import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)],int).reshape(N, M)
print(numpy.max(numpy.min(A, axis=1), axis=0))
