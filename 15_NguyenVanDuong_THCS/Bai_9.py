# Bài 9: Viết hàm đệ quy tinh_tong_chu_so(n) nhận vào một số nguyên dương n và trả
# về tổng các chữ số của nó.

def tinh_tong_chu_so(n):
    if n == 0:
        return 0
    return ((n % 10) + tinh_tong_chu_so(n//10))

n = int(input("Nhập một số nguyên: "))
print("Tổng các chữ số của {}: {}".format(n, tinh_tong_chu_so(n)))










