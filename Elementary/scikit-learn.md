- 매우 오랫동안 파이썬 기반 머신러닝으로 사용된 라이브러리

- 최근에는 " 탠서 플로 , 케라스 "등의 딥러닝 전문 라이브러리 강세로 관심이 줄고 있다. 그래도 아직까지 알기는 알아야 하는 대표적 파이썬 라이브러리


- sklearn.datasets : 사이킷런에서 자체적으로 제공하는 데이터 세트를 생성하는 모듈의 모임이 있음.
    - load_iris module 이 있다.
- sklearn.tree : 트리 기반의 ML알고리즘을 구현한 클래스의 모임.
    - DecisionTreeClassifier
- sklearn.model.selection : 학습/검증/예측 데이터로 데이터를 분리. 최적의 하이퍼 파라미터로 평가하기 위한 다양한 모듈의 모임(?)
    - train_test_split 



# Estimator
- 설명 : sklearn에서 지도학습의 모든 알고리즘의 통칭이다
    - Classifier
    - Regressor 을 포함한다,