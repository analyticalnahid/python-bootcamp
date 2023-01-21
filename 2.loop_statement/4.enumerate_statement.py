

fruits = ['apple', 'banana', 'mango']

for i, fruit in enumerate(fruits):
    print(i, fruit)

    
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
    
    
fruits = ['apple', 'banana', 'mango']
fruit_list = [(i, fruit) for i, fruit in enumerate(fruits)]
print(fruit_list)
    
