# Bài 4: Viết hàm tinh_trung_binh_cong(a, b, c) nhận vào ba số. Hàm sẽ tính và trả về
# giá trị trung bình cộng của chúng.

def tinh_trung_binh_cong(a, b, c):
    return (c+a+b)/3

a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ 3: "))

ds = tinh_trung_binh_cong(a, b, c)



