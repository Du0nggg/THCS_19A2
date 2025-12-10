# Bài 11: Viết một hàm lambda để tính tích của ba số bất kỳ.

a = int(input("Nhập số thứ 1: "))
b = int(input("Nhập số thứ 2: "))
c = int(input("Nhập số thứ 3: "))

mul = lambda a, b, c: a * b * c
print("Tích của các số vừa nhập: " + str(mul(a, b, c)))
