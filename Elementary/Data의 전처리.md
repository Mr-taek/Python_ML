## README의 내용참고해서 대충 데이터전처리는 ML알고리즘 이상으로 중요하다.

## 가장 힘든 결정 부분 NULL. NULL 값이 차지하는 비중이 일정 수준 이상인데 수준의 기준이 없다. 해당 FEATURE가 중요도가 높은 피처이고 NULL을 단순히 피처의 평균 값으로 대체하면 "예측 왜곡"이 심해지다고 하면 머리 아프다.

## SIKETLEARN의 모든 ML 알고리즘은 문자열 값을 입력 값으로 허용하지 않는다. 그래서 모든 문자여 값은 인코딩돼서 "숫자 형" 으로 변환되어야 한다. 예를드어 주민번호,아이디는 행을 식별하는 식별자일뿐임으로 예측에 중요 요소가 될 수 없음으로 삭제가 낫다.


# 데이터 인코딩
1. LABEL INCODING : 정수형 1부터 label의 개수만큼 라벨을 할당하는 방법. 선형회귀에서는 문제가 된다고 한다.
    - 나의 예시
        ```
        def incoder(data):
        dic={}
        index=1
        for i in data:
            dic[i]=index
            index+=1
            
        return list(dic.keys()),list(dic.values())
        ```
    - sikit 예시 : 그런데 이렇게 하면 문자열값이 어떤 값으로 코딩됐는 지 직관적으로 알 수 없다고 한다. 그래서 차라리 내 예시가 오히려 좋은 것같다.
        ```
        from sklearn.preprocessing import LabelEncoder
        encoder=LabelEncoder()
        encoder.fit(items)
        labels=encoder.transform(items)
        print(labels)
        ```
2. ONE-HOT INCODIG : 
    - 나의 생각 : 먼저 전체 도메인의 개수를 구하고, zeros행렬을 전체 데이터 행만큼 도메인개수만큼 만들고 도메인들을 인코딩해서 zoers인덱스와 비교해서 같은 곳을 1로 만들기.

    - sikit 예시 :
        ```
        from sklearn.preprocessing import OneHotEncoder
        import numpy as np
        oh=OneHotEncoder()
        oh.fit(labels)\oh=oh.transform(labels) # end
        ```
    - get_dummies() : 파이썬에서 원핫코딩방법
        ```
        pd.get_dummis(df)
        ```

# feature scailing , standardization
1. 표준화 : (원래값-평균)/표준편차
2. 정규화 : (xi-min(x))/(max(x)-min(x))

- StandardScaler : 표준화를 쉽게 하기 위한 클래스. 가우시안 정규분포를 가질 수 있도록 데이터를 변환한다.
    - 사용 :칼럼값의 평균이 0은 아니고 0에 근접하고 분산도 1에 근접하게 뜬다
        ```
        from sklearn.preprocessing import StandardScaler
        scaler=StandardScaler()
        scaler.fit(iris_df)
        iris_sca=scaler.transform(iris.df)
        ```
- MinMaxScaler : 데이터 값을 0~1 사이 값으로 변환하고 음수값이 있으면 -1~~1 까지변환한다. 가우시안분포가 아닐 경우 Min Max Scale을 적용할 수 있다. 
    ```
    from sklearn.preprocessing import MinMaxScaler

    scaler=MinMaxscaler()
    scaler.fit(iris_df)
    irit=scaler.transform(iris_df)
    ```