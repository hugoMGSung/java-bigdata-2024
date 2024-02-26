# file: p25_usingModule.py
# desc: 모듈 사용

#import calc as c # 나는 calc.py를 사용할래
from calc import mul as mult # mul() 함수명만 쓰면 됨

from Math import Math # from Math는 모듈(파일이름) import Math는 클래스이름

from day03.p22_carClass import Car # 디렉토리(모듈묶음:패키지).모듈명

if __name__ == '__main__': ## java void main()과 동일
    result = mult(10, 7)
    print(result) 

    print(__name__) # __main__ = 나는 메인엔트리야

    myMath = Math()
    print(myMath.solv(10))