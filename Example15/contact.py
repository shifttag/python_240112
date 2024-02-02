'''
주소록 프로젝트
1. 연락처 입력 (이름, 핸드폰번호, 이메일, 닉네임)
2. 연락처 출력
3. 연락처 삭제
4. 연락처 수정
5. 종료
'''

class Contact:
    def __init__(self, name, phone_numeber, email, nickname):
        self.name = name
        self.phone_number = phone_numeber
        self.email = email
        self.nickname = nickname

    def info(self):
        print("=============================")
        print("이름 : ", self.name)
        print("핸드폰 번호 : ", self.phone_number)
        print("이메일 : ", self.email)
        print("닉네임 : ", self.nickname)

# 입력 함수
def set_contact():
    name = input("이름 입력 >> ")
    phone_number = input("휴대폰 번호 입력 >> ")
    email = input("이메일 입력 >> ")
    nickname = input("닉네임 입력 >> ")
    contact = Contact(name, phone_number, email, nickname)
    return contact

# 정보 출력
def print_countact(contact_list):
    for item in contact_list:
        item.info()

# 연락처 삭제
def delete_contact(contact_list, name):
    for i, contact in enumerate(contact_list):
        if contact_list == name:
            del contact_list[i]

# 연락처 수정
def update_contact(contact_list, phoneNumber):
    for i, contact in enumerate(contact_list):
        if contact.phone_number == phoneNumber:
            contact_list[i] = set_contact()

contact_list = []

while True:
    print("1. 연락처 입력, 2. 연락처 출력, 3. 연락처 삭제, 4. 연락처 수정, 5. 종료")
    menu = int(input())

    if menu == 1:
        contact = set_contact()
        contact_list.append(contact)
    elif menu == 2:
        print_countact(contact_list)
    elif menu == 3:
        name = input("삭제할 이름 입력 >> ")
        delete_contact(contact_list, name)
    elif menu == 4:
        phoneNumber = input("수정할 전화번호를 입력해 주세요 >> ")
        update_contact(contact_list, phoneNumber)
    elif menu == 5:
        break
