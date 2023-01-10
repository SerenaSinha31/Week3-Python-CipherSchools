# generators
# generators are iterators

# iterator , iterable

l = [1,2,3] # iterable

# for i in l:
    # print(i)

# i = iter(l)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# next(l)


# for num in map(lambda a :a**2, l):
    # print(num)

# l= [1,4,9,16]
# memory ----- [..................................] , list
# memory ---- (5)# Create your first generator with generator function
# 1.) generator function

# 10 , 1 to 10

def nums(n):
    for i in range(1,n+1):
        yield(i)

numbers = nums(10)

for num in numbers:
    print(num)

for num in numbers:
    print(num)


# memory -------> [..............] lists


