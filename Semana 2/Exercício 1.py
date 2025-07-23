# Exercise 1: Fibonnaci Sequence Sum od even-valued terms

seq = [1, 2]
while seq[-1] < 4_000_000:
    seq.append(seq[-1]+seq[-2])

a = 0
for i in seq:
    if i%2 == 0:
        a += i
print(a)