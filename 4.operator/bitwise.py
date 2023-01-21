# Bitwise operator examples

# Bitwise AND
x = 5   # 0101
y = 3   # 0011
print(x & y)   # 0001 (1)

# Bitwise OR
x = 5   # 0101
y = 3   # 0011
print(x | y)   # 0111 (7)

# Bitwise XOR
x = 5   # 0101
y = 3   # 0011
print(x ^ y)   # 0110 (6)

# Bitwise NOT
x = 5   # 0101
print(~x)   # -6 (in two's complement representation)

# Bitwise left shift
x = 5   # 0101
print(x << 2)   # 10100 (20)

# Bitwise right shift
x = 20  # 10100
print(x >> 2)   # 101 (5)
