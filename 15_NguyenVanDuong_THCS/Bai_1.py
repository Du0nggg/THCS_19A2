#Bài 1: Viết hàm chuyen_doi_nhiet_do(do_c) nhận vào nhiệt độ tính bằng độ C và trả
#về nhiệt độ tương ứng bằng độ F.

def chuyen_doi_nhiet_do(do_c):
    return (do_c * 1.8) + 32

do_c = float(input("Nhập nhiệt độ C: "))
print("Nhiệt độ F: " + str(chuyen_doi_nhiet_do(do_c)))