'''
#문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

#입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

#출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

ex)
입력| 110 | 1 | 210

출력| 99  | 1 | 105
'''

#code
N = int(input())

count = 0
for i in range(1,N+1): # 1<=한수<=N
  if i < 100: #99까지는 모두 한수
    count+=1
  else:
    nums = list(map(int, str(i))) #세자리수를 각각 분리하여 list로
    if nums[1]- nums[0] == nums[2]-nums[1]: #등차수열이면
      count+=1

print(count)