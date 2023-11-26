#Viết chương trình bằng ngôn ngữ python

def kiem_tra_so_doi_xung(n): #Hàm kiểm tra số đối xứng
    reversed_num = 0 #Khởi tạo biến đối xứng ban đầu bằng 0
    temp = n #Gán biến temp bằng số cần kiểm tra tính đối xứng

    while temp > 0: #Chạy vòng lặp khi số đó bàng 0
        #Trong vòng lặp đầu tiên, chúng ta lấy temp % 10 để lấy chữ số cuối cùng của temp
        #sau đó cộng vào reversed_num (ban đầu là 0)
        reversed_num = reversed_num * 10 + temp % 10
        #Chia temp cho 10 (temp // 10) để loại bỏ chữ số cuối cùng
        temp = temp // 10
        #sau mỗi vòng lặp, chúng ta lấy chữ số cuối cùng của temp và cộng vào reversed_num, 
        #đồng thời giảm giá trị của temp đi một chữ số bằng cách chia cho 10.

        #Vòng lặp kết thúc khi temp sẽ trở thành 0 và reversed_num sẽ là số đảo ngược của số ban đầu
    return n == reversed_num 

def tinh_tong_chu_so(n): #Hàm tính tổng các chữ số trong một số
    total = 0 #Khởi tạo biến tổng ban đầu bằng 0
    temp = n #Gán biến temp bằng số cần kiểm tra tính đối xứng

    while temp > 0: #Chạy vòng lặp khi số đó bàng 0
        #chúng ta lấy temp % 10 để lấy chữ số cuối cùng của temp
        #sau đó cộng vào total
        total += temp % 10 
        #Chia temp cho 10 (temp // 10) để loại bỏ chữ số cuối cùng
        temp = temp // 10
        #Vòng lặp kết thúc khi temp sẽ trở thành 0 và reversed_num sẽ là số đảo ngược của số ban đầu
    return total

# Để nhập vào giá trị của một số, chúng ta sử dụng lệnh input và ép kiểu giá trị số cho biến vừa nhập
n = int(input("Nhập vào số n: "))

if kiem_tra_so_doi_xung(n):
    print(f"{n} là số đối xứng")
    #Tính tổng các chữ số trong số đó
    total = tinh_tong_chu_so(n)
    print("Tổng các chữ số của số đối xứng là:", total)
else:
    print(f"{n} không là số đối xứng")
