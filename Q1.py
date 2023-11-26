#Viết chương trình bằng ngôn ngữ Python dựa trên lưu đồ

#Để nhập vào giá trị của một số cần sử dụng lệnh input và ép kiểu giá trị số cho biến vừa nhập
n = eval(input("Nhập vào số n:"))

#Sử dụng vòng lặp if dể kiểm tra số vừa nhập lớn hơn hay nhỏ hơn 0
if n > 0: #Nếu số nhập vào là số lớn hơn 0
    #Thực hiện phép chia lấy phần nguyên (đề bài chỉ yêu cầu lấy thương, không lấy số dư)
    a = n//5 
    #In kết quả vừa thực hiện phép chia
    print("Thương khi chia cho 5 được:", a) 
else: #Nếu số nhập vào lá số nhỏ hơn 0
    #In ra dòng lệnh nhập giá trị lớn hơn 0
    print("Giá trị nhập vào phải lớn hơn 0")