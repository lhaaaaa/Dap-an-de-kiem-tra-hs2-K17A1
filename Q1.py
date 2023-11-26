#Viết chương trình bằng ngôn ngữ Python dựa trên lưu đồ

#Để nhập vào giá trị của một số cần sử dụng lệnh input và ép kiểu giá trị số cho biến vừa nhập
n = eval(input("Nhập vào số n:"))

#Sử dụng điều kiện if dể kiểm tra số vừa nhập lớn hơn hay nhỏ hơn 0
if n > 0: #Nếu số nhập vào là số lớn hơn 0
    #Khai báo biến total và gấn cho biến bằng 0
    total = 0
    #Chạy vòng lặp for từ 0 tới n
    for i in range(n+1):
        #ở mỗi vòng lặp
        total = total + i #Cộng thêm giá trị i vào total
        i+=1 #Tăng biến i lên 1 đơn vị
    #Sau khi kết thúc vòng lặp
    print("Tổng của", n, "số bắt đầu từ 0 là:", total)
else: #Nếu số nhập vào lá số nhỏ hơn 0
    #In ra dòng lệnh nhập giá trị lớn hơn 0
    print("Giá trị nhập vào phải lớn hơn 0")