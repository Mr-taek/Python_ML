# 넘파이는 매우 방대한 기능이 있어서 마스터하기엔 긴 시간과 코딩 경험이 필요함. 머신러닝 알고리즘이나 사이파이같은 과학,통계 패키지를 직접 만들지 않으면 상세히 알 필요는 없다
# 그러나 파이썬 기반의 머신러닝에 있어서 넘파이의 이해는 중요하다.


### [1,2,3] [[1,2,3]] [[1,2,3],[1,2,3]] -> 튜플 ,(3,) (1,3) (2,3) 1번은 명확하게 1차원
### 2,3, 번은 명확하게 2차원을 의미. 분명 데이터 값은 같은데 차원이 다른 경우가 있다.
### 이 때 연산이 안 됨. reshape()로 해결한다

from pickletools import float8
import numpy as np

a=np.array([1,2,3]).reshape(1,3) # 나중엔 1과3을 자동으로..또는 1,-1

b=np.array([[1,2,3]])


### ML에선 데이터 용량이 아주 크기 때문에 가능한 경우 데이터의 타입을 작은 타입으로 변환한다.
c=np.array([1,2,3]).astype(np.float16)
print(c,c.dtype)

### stack, concat. reshape(-1,1)이 자주 사용된대.

### reshape의 원리는 아마도 모든 행렬을 1차원으로 축소시키고 인자 값 만큼 할당하는 듯
### 3차원을 (-1,1)해서 2차원한 것을 참고한다.

### boolean indexing
k=np.random.randn(5,5)
mask=k<0.5
j=np.random.randint(0,10,(5,5))
j[mask]=0
print(j)

### 행렬정렬, np.sort() ndarray.sort(sotedThing) : 안에 들어오는 행렬 자체를 정렬한 형태로 변환.
ab=[2,3,5,1,2,61,2,32,124,23]
name=[]
k=np.argsort(ab)
print(k)


### 전치행렬 np.transpose(A)

