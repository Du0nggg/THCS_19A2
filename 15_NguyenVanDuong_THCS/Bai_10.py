# Bài 10: Viết hàm đệ quy tim_so_fibonacci(n) để tìm số Fibonacci thứ n trong dãy số.

def tim_so_fibonacci(n):
    if n <= 1:
        return n
    return tim_so_fibonacci(n-1) + tim_so_fibonacci(n-2)

n = int(input("Tìm số fibonacci thứ: "))
print("Số fibonacci thứ {}: {}".format(n, tim_so_fibonacci(n)))