# Exercise 1: Fibonnaci Sequence Sum of even-valued terms

fn1,fn2 = 1, 2
even_terms = 0
limit = 4_000_000

while fn2 < limit:
    if fn2%2 == 0:
        even_terms += fn2
    fn3 = fn1 + fn2
    fn1 = fn2
    fn2 = fn3

print(valued_terms)