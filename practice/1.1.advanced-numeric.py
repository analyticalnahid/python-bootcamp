# Using the decimal module to perform decimal arithmetic
import decimal
x = decimal.Decimal(5)
y = decimal.Decimal(2)
print(x / y) # Output: 2.5

# Using the fractions module to perform fraction arithmetic
import fractions
x = fractions.Fraction(5, 2)
y = fractions.Fraction(3, 4)
print(x + y) # Output: 17/4

# Using the numpy module to perform numerical operations on arrays of integers
import numpy as np
x = np.array([1, 2, 3, 4, 5])
print(np.mean(x)) # Output: 3.0
print(np.median(x)) # Output: 3.0
print(np.std(x)) # Output: 1.5811388300841898

# Using the statistics module to perform statistical operations on a list of integers
import statistics
x = [1, 2, 3, 4, 5]
print(statistics.mean(x)) # Output: 3
print(statistics.median(x)) # Output: 3
print(statistics.stdev(x)) # Output: 1.5811388300841898

# Using the itertools module to perform operations on iterators of integers
import itertools
x = [1, 2, 3, 4, 5]
print(list(itertools.permutations(x, 2))) # Output: [(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]

# Using the math module to perform mathematical operations
import math
x = 5
print(math.sqrt(x)) # Output: 2.23606797749979
print(math.factorial(x)) # Output: 120

# Using the cmath module to perform complex number mathematical operations
import cmath
x = 5
print(cmath.sqrt(x)) # Output: (2.23606797749979+0j)

# Using the gmpy2 module for large precision integers and rational numbers
import gmpy2
x = gmpy2.mpz(5)
y = gmpy2.mpz(2)
print(x / y) # Output: mpz(2)

# Using the sympy module for symbolic mathematics
import sympy
x = sympy.Symbol('x')
y = sympy.Symbol('y')
print(sympy.solve(x + y - 3, x)) # Output: [-y + 3]

# Using the array module to create arrays of integers
import array
x = array.array("i", [1, 2, 3, 4, 5])
print(x) # Output: array('i', [1, 2, 3, 4, 5])

# Using the bitarray module to create arrays of bits
import bitarray
x = bitarray.bitarray([True, False, True, True])
print(x) # Output: bitarray('1011')

# Using the collections module to create Counter, defaultdict and ordereddict of integers
import collections
x = collections.Counter([1, 1, 2, 3, 4, 5])
print(x) # Output: Counter({1: 2, 2: 1, 3: 1, 4: 1, 5: 1})

x = collections.defaultdict(int)
x[1] += 1
x[2] += 1
print(x) # Output: defaultdict(<class 'int'>, {1: 1, 2: 1})

x = collections.OrderedDict()
x[1] = 'one'
x[2] = 'two'
print(x) # Output: OrderedDict([(1, 'one'), (2, 'two')])

# Using the heapq module to perform heap operations on a list of integers
import heapq
x = [1, 2, 3, 4, 5]
print(heapq.nlargest(2, x)) # Output: [5, 4]
print(heapq.nsmallest(2, x)) # Output: [1, 2]

