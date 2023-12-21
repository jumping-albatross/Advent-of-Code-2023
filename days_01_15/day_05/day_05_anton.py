a = open('input.txt').read().split('\n\n')
seeds = a[0][7:].split()
good = list()
a = a[1:]

for i in range(len(a)):
    a[i] = a[i].split('\n')[1:]
    a[i] = [j.split() for j in a[i]]


def findMin(seed):
    for j in a:
        for k in j:
            if int(k[1]) <= seed < int(k[1]) + int(k[2]):
                seed = seed + int(k[0]) - int(k[1])
                break

    return seed


def crazy(a, b):
    i = a
    num = findMin(i)
    inc = 1
    while i < a + b:
        i += inc
        nxt = findMin(i)
        if nxt - num != inc:
            if inc == 1:
                good.append(nxt)
                num = nxt
                continue
            else:
                i -= inc
                inc = 1
                num = findMin(i)
        else:
            num = nxt
            inc *= 3


for i in range(0, len(seeds), 2):
    crazy(int(seeds[i]), int(seeds[i + 1]))
print(min(good))
