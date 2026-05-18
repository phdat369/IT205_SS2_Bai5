#Phân tích 
# Chúng ta cần tạo 6 biến để lấy dữ liệu đầu vào là:
# patient_name str
# patient_age	int
# spo2_level int
# heart_rate	int
# has_insurance str 
# Luồng ở đây là lấy giá trị của 6 biến sau đó check các điều kiện với câu điều kiện, nếu hợp lệ thì mới bắt đầu tính chi phí với mỗi loại bệnh nhân sao cho đúng và sau đó in ra thông báo 

# Viết code 

patient_name = input("Nhập họ và tên bệnh nhân: ")
patient_age = int(input("Nhập tuổi bệnh nhân: "))
spo2_level = int(input("Nhập chỉ số SpO2 (%) của bệnh nhân): "))
heart_rate = int(input("Nhập nhịp tim bệnh nhân (nhịp/phút): "))
has_insurance = input("Bệnh nhân có thẻ BHYT không? ")
if spo2_level < 90 or heart_rate > 120:
    triage_level = "BÁO ĐỘNG ĐỎ - CẤP CỨU KHẨN"
elif (90 <= spo2_level <= 95) or (100 <= heart_rate <= 120):
    triage_level = "BÁO ĐỘNG VÀNG - THEO DÕI SÁT"
else:
    triage_level = "XANH - KHÁM THƯỜNG"
    
basic_fee = 500000
if patient_age < 6 or patient_age >= 80:
    hospital_fee = 0
elif has_insurance == "yes":
    hospital_fee = basic_fee * 0.5
else:
    hospital_fee = basic_fee
