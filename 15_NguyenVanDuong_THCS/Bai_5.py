# Bài 5: Viết hàm kiem_tra_so_doi_xung(n) nhận vào một số nguyên dương n. Hàm sẽ
# trả về True nếu n là số đối xứng (khi đọc xuôi hay ngược đều giống nhau, ví dụ: 121,
# 353) và False nếu không.

def kiem_tra_so_doi_xung(n):
    x = n
    sn = 0
    while x != 0:
        sn = (sn * 10) + (x % 10)
        x //= 10
    if (sn - n) == 0:
        return True
    else:
        return False
    
n = int(input("Nhập một số nguyên: "))
ds = kiem_tra_so_doi_xung(n)

print(ds)





