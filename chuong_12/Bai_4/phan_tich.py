from du_lieu import tu_dien, danh_sach

ljst = []
x = int(input("Số lượng danh sách: "))
for i in range(x):
    j = float(input())
    ljst.append(j)
print("Danh sách ban đầu: " + str(ljst))
print("Danh sách sau khi sắp xếp: " + str(danh_sach.sap_xep_tang_dan(ljst)))


td = {
        "ten" : "nguyen van duong",
        "tuoi" : 21,
        "truong" : "UNETI",
        "lop" : "DHKL19A2"
    }

val = input("Nhập dữ liệu tìm kiếm: ")
a = tu_dien.lay_gia_tri(td, val)
if a is None:
    print("Dữ liệu không có trong từ điển")
else:
    print("Gía trị bạn tìm: " + str(a))
