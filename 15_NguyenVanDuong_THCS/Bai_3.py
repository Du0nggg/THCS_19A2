# Bài 3: Viết hàm kiem_tra_so_armstrong(n) nhận vào một số nguyên dương n. Hàm
# này sẽ trả về True nếu n là số Armstrong (tổng các lũy thừa bậc 3 của các chữ số của
# nó bằng chính nó, ví dụ: 153) và False nếu không.

def kiem_tra_so_armstrong(n):
    i = 0
    x = n
    y = n
    sum = 0

    while x != 0:
        i += 1
        x //= 10
    while y != 0:
        sum += ((y%10)**i)
        y //= 10
    if sum == n:
        return True
    else:
        return False
n = int(input("Nhập một số nguyên dương: "))
ds = kiem_tra_so_armstrong(n)

print(ds)
