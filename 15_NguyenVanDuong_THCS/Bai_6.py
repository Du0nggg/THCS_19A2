# Bài 6: Viết hàm la_so_nguyen_to(n) nhận vào một số nguyên n và trả về True nếu n
# là số nguyên tố, ngược lại trả về False. Viết hàm in_so_nguyen_to_trong_khoang(a,
# b) nhận vào hai số nguyên a và b. Sử dụng hàm la_so_nguyen_to để in ra tất cả các
# số nguyên tố trong khoảng từ a đến b.

def la_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True    

def in_so_nguyen_to_trong_khoang(a, b):
    print("Các số nguyên tố từ {0} tới {1}: ".format(a, b), end="")
    for i in range(a, b+1):
        if la_so_nguyen_to(i):
            print(i, end=" ")

while True:
    a = int(input("Nhập vào số nguyên thứ nhất: "))
    b = int(input("Nhập vào số nguyên thứ hai: "))
    if a <= b:
        break
    print("Nhập lại a <= b")
in_so_nguyen_to_trong_khoang(a, b)