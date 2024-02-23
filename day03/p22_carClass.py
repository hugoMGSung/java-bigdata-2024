# file : p22_carClass.py
# desc : 객체지향 클래스 학습

class Car:
    __carNum = '' # __변수를 지정하면 private, 그냥쓰면 public
    company = ''
    releaseYear = 1960
    color = '흰색'
    carType = ''
    fuelType = '가솔린'

    def __init__(self, carNum) -> None: # 생성자 -> None: 리턴할게 없음 뜻
        self.__carNum = carNum
        print(f'{self.__carNum} 객체를 생성합니다.')

    def __str__(self) -> str: # 객체변수를 print()할때 출력 커스터마이징 함수
        return f'내차는 {self.company}, {self.__carNum} 입니다!!'

    def setCarNum(self, carNum) -> None:
        self.__carNum = carNum

    def getCarNum(self) -> str:
        return self.__carNum

    def getCarColor(self):
        print(f'{self.__carNum}은(는) {self.color}입니다.')

    def start(self): 
        print(f'{self.__carNum}, 시동을 겁니다')

    def accel(self):
        print(f'{self.__carNum}, 엑셀을 밟습니다')

    def brake(self):
        print(f'{self.__carNum}, 브레이크를 밟습니다')

    def turnLeft(self):
        print(f'{self.__carNum}, 좌회전합니다')
    
    def turnRight(self):
        print(f'{self.__carNum}, 우회전합니다')
