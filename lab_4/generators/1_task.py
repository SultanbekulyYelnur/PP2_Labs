def generator(N):
    for i in range(N):
        yield i ** 2

N = 10
for j in generator(N):
    print(j)