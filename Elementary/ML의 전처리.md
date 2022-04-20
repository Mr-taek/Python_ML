1. 데이터의 불균형이 있는 지 체크한다 : pandas의 Series객체.value_counts()를 사용하면 해당 객체의 도메인 범위에 해당하는 각 값의 개수를 리턴한다(객체는 Label객체와 kfold한 이후의 x_train과 x_test간의 label 분류 두가지를 진행해야 한다.). 일반적으로 분류에선 Stratified K 분류가 사용되어야 한다. 회귀에는 Stratified K가 없다.
    ```
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import KFold
    from sklearn.datasets import load_iris
    kfold=KFold(3,shuffle=True)

    iris=load_iris()
    import pandas as pd
    df=pd.DataFrame(iris['data'],columns=iris.feature_names)
    df['label']=iris['target']

    for x_train,x_test in kfold.split(df):
        print("실험 데이터 분포 :\n {0}\n".format(df['label'].iloc[x_train].value_counts()))
        print("테스트 데이터 분포 :\n {0}\n".format(df['label'].iloc[x_test].value_counts()))
    ```

