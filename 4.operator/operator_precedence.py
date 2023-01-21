
# Without parentheses, the multiplication has higher precedence than the addition
print(4 + 5 * 6)   # 34

# With parentheses, the addition has higher precedence than the multiplication
print((4 + 5) * 6)   # 54

# Exponentiation has higher precedence than the unary minus operator
print(-3 ** 2)   # -9

# The unary minus operator has higher precedence than the multiplication
print(-3 * 2)   # -6

# The comparison operator has higher precedence than the boolean OR operator
print(True or False == False)   # True

# The boolean AND operator has higher precedence than the boolean OR operator
print(True or False and False)   # True
