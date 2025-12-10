# Bài 14: Viết một hàm lambda để tính tổng của hai số.

n = float(input("Nhập số thứ nhất: "))
m = float(input("Nhập số thứ hai: "))
ds = lambda n, m: n + m
print("Tổng của hai số vừa nhập: " + str(round(ds(n, m),2)))