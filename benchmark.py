from introsort.core import introsort
import random
import timeit

sizes = [100, 1000, 5000]
random.seed(42)  

print("Benchmark Introsort vs Python's sorted()")
for n in sizes:
    data = [random.randint(1, n*10) for _ in range(n)]
    
    def introsort_test():
        arr = data.copy()
        introsort(arr, 0, len(arr)-1)
        return arr
    
    def sorted_test():
        arr = data.copy()
        return sorted(arr)
    
    t1 = timeit.timeit(introsort_test, number=10)
    t2 = timeit.timeit(sorted_test, number=10)
    
    print(f"n={n}: Introsort = {t1:.4f}s, sorted = {t2:.4f}s (ratio: {t1/t2:.2f}x)")

n = 1000
data_rev = list(range(n, 0, -1))
t1_rev = timeit.timeit(lambda: introsort(data_rev.copy(), 0, len(data_rev)-1), number=5)
t2_rev = timeit.timeit(lambda: sorted(data_rev.copy()), number=5)
print(f"\nWorst-case (reverse n={n}): Introsort = {t1_rev:.4f}s, sorted = {t2_rev:.4f}s (ratio: {t1_rev/t2_rev:.2f}x)")