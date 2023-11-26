# Hàm kiểm tra số chính phương
def is_perfect_square(a):
  if a < 0:  # Kiểm tra nếu số nhập vào là số âm
    return False
  sqrt = int(a ** 0.5)
  return sqrt * sqrt == a

# Để nhập vào giá trị của một số, chúng ta sử dụng lệnh input và ép kiểu giá trị số cho biến vừa nhập
n = int(input("Nhập vào số n: "))

# Kiểm tra nếu số nhập vào là số lớn hơn 0
if n > 0:
    m = n  # Gán giá trị m bằng n
    while True: #while True được sử dụng để tạo một vòng lặp vô hạn. 
    #Khi chúng ta sử dụng while True, điều kiện lặp luôn đúng
    #do đó vòng lặp sẽ tiếp tục chạy cho đến khi gặp một câu lệnh break hoặc khi có một điều kiện khác để kết thúc vòng lặp
    
    #Chúng ta tăng giá trị của m lên 1 cho đến khi tìm được số chính phương và thỏa mãn điều kiện
       m += 1 
       if is_perfect_square(m) and m - n >= 20: 
          break
    print("Số chính phương thỏa mãn điều kiện là:", m)
else:  # Nếu số nhập vào không là số lớn hơn 0
    print('Số nhập vào phải lớn hơn 0')

