# Hàm tính ước số chung lớn nhất (GCD) của hai số
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Nhập vào tử số a và mẫu số b của phân số
a = int(input("Nhập tử số: "))
b = int(input("Nhập mẫu số: "))

# Sử dụng điều kiện if đế kiểm tra mẫu số có khác 0 không?
if b==0:
    print("Không tồn tại phân số")
else:
    uoc_chung_lon_nhat = gcd(a,b) #Tính ước chung lớn nhất của tử số và mẫu số
    #Sử dụng điều kiện if để kiểm tra phân số đã tối giản hay chưa?
    if uoc_chung_lon_nhat == 1:
        print("Phân số sau khi rút gọn là", f"{a}/{b}")
    else:
        print("Phân số sau khi rút gọn là", f"{int(a/uoc_chung_lon_nhat)}/{int(b/uoc_chung_lon_nhat)}")
