#Viết chương trình bằng ngôn ngữ Python dựa trên lưu đồ

#Để nhập vào giá trị của một nhiệt độ (theo độ C) cần sử dụng lệnh input và ép kiểu giá trị số cho biến vừa nhập
do_C = eval(input("Nhập vào số n:"))

#Để chuyển từ độ C sang độ K, ta cộng vào độ C thêm 273 đơn vị
do_K = do_C + 273

#In ra giá trị theo độ K
print("Nhiệt độ", do_C, "độ C được chuyển thành nhiệt độ K là:", do_K, "độ K.")