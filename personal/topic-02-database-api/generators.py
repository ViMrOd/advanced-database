def count_up():
   return [i + 1 for i in range(0, 10)]

print(count_up())

def count_up_gen(n):
    for i in range(0, n):
        yield i + 1

x = count_up_gen(17)

for i in x:
    print(i)