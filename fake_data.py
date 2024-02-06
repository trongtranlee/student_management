from faker import Faker
import random
import pandas as pd

fake = Faker()

def generate_student_id():
    return f"2000{random.randint(0, 999):04d}"


def generate_student_phone_number():
    # Số điện thoại bắt đầu bằng chữ số 0
    phone_number = "0"

    # Tạo 9 chữ số ngẫu nhiên từ 0 đến 9 và thêm vào số điện thoại
    for _ in range(9):
        phone_number += str(random.randint(0, 9))

    return phone_number

def generate_student_email():
    return fake.email(domain='hus.edu.vn')

def generate_student_age():
    return random.randint(17, 25)

def generate_student_city():
    return fake.city()

def generate_student_gender():
    return random.choice(['Nam', 'Nữ', 'Khác'])

def generate_student_score():
    return random.randint(0, 10)

# Tạo dữ liệu cho 1000 sinh viên
data = []
for _ in range(1000):
    student = {
        'student_name': fake.name(),
        'student_id': generate_student_id(),
        'student_phoneNumber': generate_student_phone_number(),
        'student_email': generate_student_email(),
        'student_age': generate_student_age(),
        'student_city': generate_student_city(),
        'student_gender': generate_student_gender(),
        'student_mathScore': generate_student_score(),
        'student_chemScore': generate_student_score(),
        'student_phyScore': generate_student_score(),
        'student_engScore': generate_student_score(),
        'student_litScore': generate_student_score()
    }
    data.append(student)

df = pd.DataFrame(data)

# Xuất DataFrame ra file CSV
df.to_csv('fake_data.csv', index=False)

print(df.to_string())

print("Dữ liệu đã được xuất ra file data.csv")


