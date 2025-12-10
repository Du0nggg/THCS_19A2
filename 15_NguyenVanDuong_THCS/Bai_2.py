#Bài 2: Viết hàm giai_phuong_trinh_bac_nhat(a, b) nhận vào hai hệ số a và b của
#phương trình ax+b=0. Hàm sẽ in ra nghiệm của phương trình hoặc thông báo vô
#nghiệm/vô số nghiệm.

def giai_phuong_trinh_bac_nhat(a, b):
    if a == 0:
        if b != 0:
            print("Hàm số ax + b = 0 vô nghiệm")
        else:
            print("Hàm số ax + b = 0 vô số nghiệm")
    else:
        print("Nghiệm của phương trinh {0}x + {1} = 0 là x = {2}".format(a,b,-b/a))            
    
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
giai_phuong_trinh_bac_nhat(a, b)
