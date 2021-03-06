'''
#문제
알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

#입력
알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

#출력
입력으로 주어진 글자의 아스키 코드 값을 출력한다.

ex)
입력| A   0   z
출력| 65  48  122
'''

#code
N = input() 

if N.isalpha(): #isalpha(): 알파벳존재여부를 True, False로 반환
  print(ord(N)) #ord(): 문자열을 아스키로 변환
else:
  print(ord(str(N)))