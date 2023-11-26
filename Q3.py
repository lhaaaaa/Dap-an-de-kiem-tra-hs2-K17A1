#Viết chương trình bằng ngôn ngữ python

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:  # Số nhỏ hơn hoặc bằng 1 không phải là số nguyên tố
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # Nếu n chia hết cho i, n không là số nguyên tố
            return False
    return True  # Nếu không tìm thấy ước số nào, n là số nguyên tố

# Để nhập vào giá trị của một số, chúng ta sử dụng lệnh input và ép kiểu giá trị số cho biến vừa nhập
n = int(input("Nhập vào số n: "))

# Gọi hàm kiểm tra số nguyên tố và in kết quả
if is_prime(n):
    print("Số vừa nhập là số nguyên tố.")
else:
    print("Số đã nhập không phải là số nguyên tố.")