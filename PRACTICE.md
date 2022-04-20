1. Kfold를 이용한 DecisionTree
```
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.datasets import load_iris

def acc(x,y):
    cnt=0
    for index,value in enumerate(x):
        if value==y[index]:
            cnt+=1
            
    return cnt/len(x)

iris=load_iris()
feat=iris['data']
label=iris['target']
kfold=KFold(n_splits=10)
dt=DecisionTreeClassifier()
for train_index,vali_index in kfold.split(feat):
    dt.fit(feat[train_index],label[train_index])
    prd=dt.predict(feat[vali_index])
    print("ACC IS : {0}".format(acc(prd,label[vali_index])))
```