# Bài 7: Viết hàm tinh_tong_so_hoan_hao(a, b) nhận vào hai số nguyên dương a và b
# (với a <= b). Hàm sẽ tính và trả về tổng của tất cả các số hoàn hảo trong khoảng từ a
# đến b.

def tong_so_hoan_hao(a, b):
    sum_a = 0
    for i in range(a, b+1):
        sum = 0
        for j in range(1, i):
            if i % j == 0:
                sum += j
        if i == 1 or sum == i:
            sum_a += i
    return sum_a

while True:
    a = int(input("Nhập số nguyên dương thứ nhất: "))
    b = int(input("Nhập số nguyên dương thứ hai: "))
    if a <= b:
        break
    print("Nhập sai điều kiện (a <= b)")

print("Tổng các số hoàn hảo từ {} tới {}: {}".format(a, b, tong_so_hoan_hao(a, b)))






