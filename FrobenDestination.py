#1)프로베니우스 거리 구하기

import numpy as np

#프로베니우스 거리 구하기
def Frobenius(M1,M2):
  D = M1 - M2
  return np.sqrt(np.sum(D**2))

#두 개의 난수 만들기
N = 10
s = 1
cnt = 0
randomMatrix1 = np.random.randn(N,N)
randomMatrix2 = np.random.randn(N,N)

#프로베니우스 거리가 1 이상일 경우에만 하기
while Frobenius(s * randomMatrix1, s * randomMatrix2) >= 1:
  s = s * 0.9
  cnt = cnt + 1

#스칼라를 곱한 횟수와 스칼라 그리고 최종 프로베니우스 거리 출력
print(f'reps of num = {cnt}, scalar = {s/0.9: .3f}')
print(f'final Frobenius is {Frobenius(s/0.9 * randomMatrix1, s/0.9 * randomMatrix2): .3f}')
