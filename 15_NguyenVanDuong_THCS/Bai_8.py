# Bài 8: Viết hàm tim_so_le_lon_nhat(a, b, c) nhận vào ba số nguyên. Hàm sẽ trả về
# số lẻ lớn nhất trong ba số đó. Nếu không có số lẻ nào, hàm trả về một giá trị đặc biệt
# (ví dụ: -1) để báo hiệu.

def tim_so_le_lon_nhat(a , b, c):
    L = []
    for i in (a, b, c):
        if i % 2 != 0:
            L.append(i)

    if not L:
        return -1
    L.sort()
    return L[len(L)-1]

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))

ds = tim_so_le_lon_nhat(a, b, c)
if ds == -1:
    print("Không có số lẻ")
else:
    print("Số lẻ lớn nhất trong các số vừa nhập: " + str(ds))






