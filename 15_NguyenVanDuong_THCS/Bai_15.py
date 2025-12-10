# Bài 15: Nhập vào một số nguyên dương n, viết hàm kiểm tra xem n có phải là số
# nguyên tố hay không? Sau đó in ra các số nguyên tố trong khoảng [100, 500].

def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def in_snt():
    print("Các số nguyên tố trong khoảng [100-500]: ", end="")
    for i in range(100,500+1):
        if kiem_tra_so_nguyen_to(i):
            print(i, end=" ")


n = int(input("Nhập một số nguyên dương: "))
if kiem_tra_so_nguyen_to(n):
    print(str(n) + " là một số nguyên tố")
else:
    print(str(n) + " không là số nguyên tố")
in_snt()





