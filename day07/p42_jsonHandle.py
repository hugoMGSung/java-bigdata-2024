# file: p42_jsonHandle.py
# desc: json 읽고/쓰기

import json

## json 읽기
# file읽어서 쓸 객체변수 f, file, fp
# with문으로 작업하면 fp.close() 불필요
with open('./day07/p40_testData.json', mode='r', encoding='utf-8') as fp:
    data = json.load(fp)

# data로 출력->파이썬 딕셔너리 출력 / json.dumps(data)->json형태로 출력 / indent='\t'는 보기좋게 출력
print(json.dumps(data, indent='\t'))

# json 데이터 접근은 파이썬 딕셔너리, 리스트와 동일하게 사용가능
print(data['name'])
print(data['friends'][1])

## 쓰기
# 딕셔너리를 만들고 json dump 한뒤 저장
superCars = dict() # 딕셔너리 생성
audi = dict()
audi['price'] = 300_000_000 #3억
audi['year'] = '2020'
audi['type'] = 'electric'
superCars['audi'] = audi

car = dict()
car['price'] = 1_500_000_000 # 15억
car['year'] = '2019'
car['type'] = 'gasolin'
superCars['porsche'] = car

# json파일 저장
with open('./day07/superCars.json', mode='w', encoding='utf-8') as fp:
    json.dump(superCars, fp, indent='\t', ensure_ascii=True)