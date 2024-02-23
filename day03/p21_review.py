## Q7
## readlines() 썼을때
f = open('./day03/test.txt', mode='r', encoding='utf-8')
body = f.readlines() # 결과 리스트로 리턴
f.close()

body = [body[0], body[1].replace('java', 'python')]
# print(body)
f = open('./day03/test.txt', mode='w', encoding='utf-8')
f.write(body[0] + body[1])
f.close()

## read() 를 썼을때
f = open('./day03/test.txt', mode='r', encoding='utf-8')
body = f.read()  # 문자열로 리턴. 단, read()는 텍스트가 길면 문장이 잘려나온다.
f.close()

body = body.replace('java', 'python')
# print(body)
f = open('./day03/test.txt', mode='w', encoding='utf-8')
f.write(body)
f.close()

