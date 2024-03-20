#분배법칙 확인
def addFirst(s,A,B):
  return s * (A + B)

def addSec(s, A, B):
  return s * A + s * B

def addTh(s, A, B):
  return A*s + B * s

s = np.random.randn()
N = np.random.randn(3,4)
M = np.random.randn(3,4)
print(addFirst(s,N,M))
print(addSec(s,N,M))
print(addTh(s,N,M))
