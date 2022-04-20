- 매우 오랫동안 파이썬 기반 머신러닝으로 사용된 라이브러리

- 최근에는 " 탠서 플로 , 케라스 "등의 딥러닝 전문 라이브러리 강세로 관심이 줄고 있다. 그래도 아직까지 알기는 알아야 하는 대표적 파이썬 라이브러리


- sklearn.datasets : 사이킷런에서 자체적으로 제공하는 데이터 세트를 생성하는 모듈의 모임이 있음.
    - load_iris module 이 있다.
- sklearn.tree : 트리 기반의 ML알고리즘을 구현한 클래스의 모임.
    - DecisionTreeClassifier
- sklearn.model.selection : 학습/검증/예측 데이터로 데이터를 분리. 최적의 하이퍼 파라미터로 평가하기 위한 다양한 모듈의 모임(?)
    - train_test_split 

# 일반적 머신러닝 모델 구축 process
1. Feature 처리 : 피처의 가공, 변경, 추출
2. ML 알고리즘 학습/예측 수행
3. 모델 평가
4. 반복


# Estimator 
- Estimator : sklearn에서 지도학습의 모든 알고리즘의 통칭이다, 내부에 fit() , predict() 함수를 내포하고 있다.
    - fit() : 학습을 의미
    - Classifier
        1. DecisionTreeClassifier
        2. RandomForestClassifier
        3. GradientBoostingClassifier
        4. GaussianNB
        5. SVC
    - Regressor
        1. LinearRegression
        2. Ridge?
        3. Lasso?
        4. RandomForestRegressor
        5. GradientBoostingRegressor


# 라이브러리

1. from sklearn.tree import DecisionTreeClassifier
    ```
    from sklearn.tree import DecisionTreeClassifier
    dt=DecisionTreeClassifier()
    df.fit(x_train,y_train)
    pred=df.predict(x_test)
    ```
2. from sklearn.model_selection import train_test_split
    1. test_size : default 25%
    2. train_size : test size파라미터가 통상 쓰이기 때문에 잘 사용하지 않음.
    3. shuffle : default True, 데이터 분리 전 섞을 지를 결정. 데이터를 분산시켜서 더 효율적이게 과적합 방지 제고.
    4. random_state : 매번 호출할 때마다 랜덤값을 같은 걸로 출력.
    ```
    data=np.random.rand(30,10)
    targ=np.random.randint(0,2,(30,1))
    x_train,x_test,y_train,y_test=train_test_split(rst,targ,test_size=0.1)
    ```
3. from sklearn.model.selection import KFold ML 전처리의 일종-> PRACTICE 1번
    - KFold parameter
        1. n_splits : default 는 아무튼 있음
    - KFold.splot parameter
        1. x : feature데이터, 필수
        2. y : label 데이터, 생략가능
    1. n_splits : k 의 개수 지정 
    ```
    iris=load_iris()
    feat=iris['data']
    label=iris['target']
    kfold=KFold(n_splits=5)
    dt=Decision~
    for train_index,vali_index in kfold.split(feat):
        dt.fit(train_index)
    ```

4. Stratified K 폴드 : 데이터 LABEL의 분포가 균형적이지 못할 때 사용. 가령 1억개중 9억개는 참이고 1억갠 거짓. ML 전처리의 일종
    - pandas의 Series객체.value_counts()를 사용하면 해당 객체의 도메인 범위에 해당하는 각 값의 개수를 리턴한다(객체는 Label객체와 kfold한 이후의 x_train과 x_test간의 label 분류 두가지를 진행해야 한다.)
    
    - 대용으로 KFold에 shuffle 기능을 사용해도 되기도 하다.

    - parameter : KFold와 비슷하고 딱, split에서 라벨데이터를 꼭 명시해야한다. df안에 라벨이 있던 없던 신경 안스고 알아서 걸러주나 보다~
        ```
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.model_selection import KFold
        from sklearn.datasets import load_iris
        kfold=KFold(3,shuffle=True)

        iris=load_iris()
        import pandas as pd
        df=pd.DataFrame(iris['data'],columns=iris.feature_names)
        df['label']=iris['target']


        from sklearn.model_selection import StratifiedKFold
        skf=StratifiedKFold(n_splits=3)
        c=df.drop('label',axis=1)
        print(df)
        print(c)
        for x_train,x_test in skf.split(c,df['label']):
            print("실험 데이터 분포 :\n {0}\n".format(df['label'].iloc[x_train].value_counts()))
            print("테스트 데이터 분포 :\n {0}\n".format(df['label'].iloc[x_test].value_counts()))
        ```

5. cross_val_score : 3,4번에서 for문까지 써줘야 하는 수고를 덜 더록 한 번에 해주는 함수. 일반적으로 결과를 평균해서 평가 수치로 본다.
    - parameter
        1. estimator : fit을 포함하고있는 객체. 위에 Estimator을 참고하면 ㅇㅋ. ESTIMATOR안에는 FIT PREDICT EVALUATION이 있음.
        2. X : 실제 데이터
        3. Y : 라벨,TARGET
        4. SCORING : 함수(estimator)도 올수 있다 하는데 , 그냥 없이 두면 1번에서 알아서 정해짐.
        5. cv : cross validation 개수.
        ```
        from sklearn.model_selection import cross_val_score
        score=cross_val_score(dt,feat,label,cv=3)
        ```
    - Return : cv의 개수만큼 훈련,검증의 결과를 반환

    + 유사 함수 " cross_validate " , 인자도 같은데 차이는 시간 훈련시간과 성능평가지표,수행시간등을 모두 반환한다.
# 예제 데이터 세트 종류
- 설명 : sklear.datasets의 타입은 Bunch class 타입임. dictionary 형태와 아주 비슷하다고 하는데 같다고 봄.
- 회귀 용도
    1. datasets.load_boston()
    2. datasets.load_diabetes()
- 분류 용도
    1. datasets.load_breast_cancer()
    2. datasets.load_digits()
    3. datasets.load_iris()

