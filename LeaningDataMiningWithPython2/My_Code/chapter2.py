import numpy as np
import csv
import os

#读数据
data_filename = os.path.join(os.getcwd(),"ionosphere.data.csv")
x = np.zeros((351,34),dtype = "float")
y = np.zeros(351,dtype = "int")

with open(data_filename,"r") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        data = [float(x) for x in row[:-1]]
        x[i] = data      #注意 numpy 中 每一行的矩阵可以这样赋值
        if row[-1] == 'g':
            y[i] = 1
        if row[-1] == 'b':
            y[i] = 0     


#标准流程
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(x,y,random_state = 14) #交叉验证

from sklearn.neighbors import KNeighborsClassifier
estimator = KNeighborsClassifier()
estimator.fit(X_train,y_train)
y_predicted = estimator.predict(X_test)
accuracy = np.mean(y_test == y_predicted) * 100   # 注意 numpy 比较的特殊用法
print("The accuray is {0:.1f} %".format(accuracy))

score = estimator.score(X_test,y_test)
print(score)


# 采用交叉验证
from sklearn.cross_validation import cross_val_score
scores = cross_val_score(estimator,x,y,scoring="accuracy") #这种切分方法大体保证了切分后的数据集中类别分布相同 以避免子数据集出现类别失衡的情况
print("The accuracy is: {0:1f} %".format(np.mean(scores)* 100))


#参数调优
avg_scores = []
all_socres = []
parameters = list(range(1,21)) 
for parameter in parameters:
    estimator = KNeighborsClassifier(n_neighbors = parameter)
    scores = cross_val_score(estimator,x,y,scoring="accuracy")
    avg_scores.append(np.mean(scores))
    all_socres.append(scores)
"""
#图像显示
from matplotlib import pyplot as plt
plt.plot(parameters,avg_scores,"-o")
plt.show()
"""



# 修改数据transformer为预处理做准备
x_broken  = np.array(x) #python 中对象之间的赋值都是传递引用   如果需要拷贝对象 需要用 copy 模块
x_broken[:,::2] /= 10
estimator = KNeighborsClassifier()
original_socre = cross_val_score(estimator,x_broken,y,scoring="accuracy")
really_score = cross_val_score(estimator,x,y,scoring="accuracy")
print("The original score is: {0:1f}".format(np.mean(original_socre)))
print("The really score is: {0:1f}".format(np.mean(really_score)))


#标准预处理
#将所有数据放缩到 0 -1 之间
from sklearn.preprocessing import MinMaxScaler
X_transformed = MinMaxScaler().fit_transform(x_broken)
estimator = KNeighborsClassifier()
score = cross_val_score(estimator,X_transformed,y,scoring="accuracy")
print("The accuracy is : {0:1f}".format(np.mean(score)))

# sklean.processing.Normalizer 使每条数据数据各特征值的和为一
# sklean.processing.StandardScaler 各特征均为为0 方差为1
# sklean.processing.Binarizer 大于阙值为1 小于为0


"""流水线的使用"""
from sklearn.pipeline import Pipeline
step = [("scalar",MinMaxScaler()),("predict",KNeighborsClassifier())]
pip = Pipeline(step)
score = cross_val_score(pip,x_broken,y,scoring="accuracy")
print("The accuracy is : {0:1f}".format(np.mean(score)))




