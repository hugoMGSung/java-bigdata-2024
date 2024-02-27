# file : p34_addrBook.py
# desc : 콘솔 주소록 프로그램
import os 

class Contact: # 주소록 클래스
    # 생성자
    def __init__(self, name, phoneNumber, eMail, addr) -> None:
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__eMail = eMail
        self.__addr = addr

    # 사용자가 원하는 형태로 출력
    def __str__(self) -> str: # 원래출력 <__main__.Contact object at 0x0000024500772150> 
        res = (f'이  름 : {self.__name}\n'
               f'핸드폰 : {self.__phoneNumber}\n'
               f'이메일 : {self.__eMail}\n'
               f'주  소 : {self.__addr}')
        return res
    
    # 연락처 여부확인
    def isNameExist(self, name):
        if self.__name == name: # 찾는 이름 존재
            return True
        else:
            return False
        
    def getInfo(self):
        return self.__name, self.__phoneNumber, self.__eMail, self.__addr

def setContact(): # 사용자 입력으로 주소록 받기함수
    (name, phoneNumber, eMail, addr) = input('입력(이름,핸드폰,이메일,주소[/])> ').split('/')
    name = name.strip() # 사용자실수로 들어간 스페이스 제거
    phoneNumber = phoneNumber.strip()
    eMail = eMail.strip()
    addr = addr.strip()
    # print(f'"{name}", "{phoneNumber}", "{eMail}", "{addr}"')
    contact = Contact(name, phoneNumber, eMail, addr) # 매개변수명과 동일하게 로컬변수 이름 지정
    return contact

def delContact(lst, name): # 연락처 삭제함수
    for i in range(len(lst)-1, -1, -1): # 리스트를 내림차순으로 뒤에서부터 삭제
        item = lst[i]
        if item.isNameExist(name):
            del lst[i]

def saveContact(lst): # 연락처 저장함수
    with open('./contacts.txt', mode='w', encoding='utf-8') as fp:
        for item in lst:
            name, phoneNumber, eMail, addr = item.getInfo()
            fp.write(f'{name}/{phoneNumber}/{eMail}/{addr}\n')

def loadContact(lst): # 처음 실행시 연락처 로드함수
    try:
        with open('./contacts.txt', mode='r', encoding='utf-8') as fp:
            while True:
                line = fp.readline() # str
                if not line: break

                lines = line.replace('\n', '').split('/') # list
                contact = Contact(name=lines[0], phoneNumber=lines[1], eMail=lines[2], addr=lines[3])
                lst.append(contact)
    except: # 연락처 파일이 없으면 새로 만들어줌
        f = open('./contacts.txt', mode='w', encoding='utf-8')
        f.close()

def displayMenu():
    menu = ('주소록 프로그램\n'
            '1. 연락처 추가\n'
            '2. 연락처 출력\n'
            '3. 연락처 삭제\n'
            '4. 종료\n')
    print(menu)
    try:
        sel = int(input('메뉴입력 : '))
    except: # 1~4가 아닌 잘못된 문자 입력할때 예외처리
        sel = 0

    return sel

def clearConsole():
    cmd = 'clear' # macOS, Linux, Unix 명령어
    if os.name in ('nt', 'dos'): # window
        cmd = 'cls' # window 명령어

    os.system(cmd) # 명령어 실행

def getContacts(lst): # 리스트를 받아서 출력함수
    for i, item in enumerate(lst):
        print(f'{i+1} ==========>')
        print(item)

def run():
    # 연락처담을 주소록 리스트
    lstContact = []
    loadContact(lstContact) # 연락처 로드

    clearConsole() # 화면을 클리어
    while True:
        selMenu = displayMenu()

        if selMenu == 1: # 연락처 추가라면
            clearConsole()
            try:    
                contact = setContact()
            except: # 입력을 시킨대로 안하면 
                contact = None

            if contact != None:
                lstContact.append(contact)
                input('입력 성공!')
            else:
                input('입력 실패')

            clearConsole() # 엔터 입력유도            
        elif selMenu == 2: # 연락처 출력
            clearConsole()
            getContacts(lstContact)
            input('출력 성공!'); clearConsole()
        elif selMenu == 3: # 연락처 삭제
            clearConsole()
            name = input('삭제할 이름 입력 : ')
            delContact(lstContact, name)
            input('삭제 성공'); clearConsole()
        elif selMenu == 4:
            saveContact(lstContact)
            break
        else:
            clearConsole() 

if __name__ == '__main__': # 메인엔트리
    print('프로그램 시작')
    run() # 메인함수 실행

print('프로그램 종료')