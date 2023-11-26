#Viết chương trình bằng ngôn ngữ Python dựa trên lưu đồ

#Để nhập vào giá trị của một số cần sử dụng lệnh input và ép kiểu giá trị số cho biến vừa nhập
n = eval(input("Nhập vào số n: "))

#Sử dụng điều kiện if dể kiểm tra số vừa nhập lớn hơn hay nhỏ hơn 0
if n > 0: #Nếu số nhập vào là số lớn hơn 0
    i = 0 #Khai báo và gán giá trị i = 0
    while i < n: #Chạy vòng lặp while, khi i < n thì thực thi câu lệnh
        print(i) #In ra giá trị i
        i+=1  #Tăng biến i lên 1 đơn vị
else: #Nếu số nhập vào không là số lớn hơn 0
    print('Số nhập vào phải lớn hơn 0')