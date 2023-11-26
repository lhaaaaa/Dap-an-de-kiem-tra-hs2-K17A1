#Viết chương trình bằng ngôn ngữ python

#Để nhập vào giá trị của một số cần sử dụng lệnh input và ép kiểu giá trị số cho biến vừa nhập
n = int(input("Nhập vào số n: "))

#Sử dụng vòng lặp if dể kiểm tra số nguyên vừa nhập có là số nguyên dương hay không?
if n <= 0: #Nếu số vừa nhập không là số nguyên dương
    print("Nhập lại giá trị số nguyên dương")
else: #Nếu số vừa nhập là số nguyên dương
    #Kiểm tra số nguyên dương có nhỏ hơn bằng 1 không
    if n <= 1: 
        print("Số đã nhập không phải số nguyên tố")
    else:
        #Thêm biến is_prime để lưu trạng thái của số nguyên vừa nhập. Ban đầu, ta giả định số đó là số nguyên tố
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
        #Ta lặp qua các giá trị i từ 2 đến căn bậc hai của n.
        #Lý do ta chỉ cần lặp đến căn bậc hai là vì một số nguyên tố lớn nhất có thể là căn bậc hai của chính nó.
        #Trong mỗi lần lặp, ta kiểm tra xem n có chia hết cho i hay không
            if n % i == 0:
                #Trong vòng lặp, nếu ta tìm thấy một số i mà n chia hết 
                #ta gán is_prime = False, kết thúc vòng lặp bằng câu lệnh break.
                if n % i == 0:
                    is_prime = False
                    break
        #Sau khi kết thúc vòng lặp, ta kiểm tra giá trị của is_prime để xác định xem số vừa nhập có là số nguyên tố hay không 
        #in ra kết quả tương ứng.
        if is_prime:
            print("Số vừa nhập là số nguyên tố.")
        else:
            print("Số đã nhập không phải là số nguyên tố")