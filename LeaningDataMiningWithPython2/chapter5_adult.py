import os
import pandas as pd
import numpy as np

def loadData():
    full_path_name = os.path.join(os.getcwd(),"adult.data.txt")
    adult = pd.read_csv(full_path_name,header=None)
    adult.columns = ["Age","Workclass","fnlwgt","Education","Education-Num","Marital-Status",\
    "Occupation","Relationship","Race","Sex","Capital-gain","Capital-loss","Hours-per-week",\
    "Native-Country","Earnings-Raw"]
    #print(adult.ix[:5])
    return adult

#利用 sklean 模块 去掉方差达不到最低标准的第二行
def del_feature():
    X = np.arange(30).reshape((10,3))
    X[:,1] = 1
    print(X)
    print(" ")

    from sklearn.feature_selection import VarianceThreshold
    vt = VarianceThreshold()
    Xt = vt.fit_transform(X)
    print(Xt)
    print(" ")
    print(vt.variances_)  #输出每一列的方差

#使用卡方检验打分  用SelectKBest返回k个最佳特征
def return_k_feature_chi2():
    adult = loadData()
    X = adult[["Age","Education-Num","Capital-gain","Capital-loss","Hours-per-week"]].values
    print (X)
    y = ( adult["Earnings-Raw"] == " >50K" ).values
    from sklearn.feature_selection import SelectKBest
    from sklearn.feature_selection import chi2
    selector = SelectKBest(score_func = chi2, k = 3)
    Xt_chi2 = selector.fit_transform(X,y) # 生成的矩阵只包含三个特征
    print(Xt_chi2)
    print(selector.scores_)  #相关性打分情况


#使用 SciPy 库   使用皮尔逊相关系数打分  用 SelectKBest 返回 k 个最佳特征
def return_k_feature_p():
    adult = loadData()
    X = adult[["Age","Education-Num","Capital-gain","Capital-loss","Hours-per-week"]].values
    y = (adult["Earnings-Raw"] == " >50K").values
    from sklearn.feature_selection import SelectKBest
    selector = SelectKBest(score_func = multivariate_pearsonr, k = 3)
    Xt_pearson = selector.fit_transform(X,y)
    print(selector.scores_)


def multivariate_pearsonr(X,y): 
    from scipy.stats import pearsonr   
    socres = []
    pValues = []
    for columns in range(X.shape[1]):
        # pearsonr   函数的参数为两个一维数组 
        cur_score,cur_p = pearsonr(X[:,columns],y)
        socres.append(cur_score)
        pValues.append(cur_p)

    return (np.array(socres),np.array(pValues))    

#利用 卡方检验 算出的三个特征进行预测 
def predict():
    adult = loadData()
    X = adult[["Age","Capital-gain","Hours-per-week"]].values
    y = (adult["Earnings-Raw"] == " >50K").values
    from sklearn.cross_validation import cross_val_score
    from sklearn.tree import DecisionTreeClassifier
    clf = DecisionTreeClassifier()
    scores = cross_val_score(clf,X,y,scoring="accuracy")
    print("The accuracy is {0}".format(np.mean(scores)))


#自己定义转换器  返回 X 中大于均值的数据
from sklearn.base import TransformerMixin
from sklearn.utils import as_float_array
class MeanDiscrete(TransformerMixin):
    def fit(self,X):
        X = as_float_array(X)
        self.mean = X.mean(axis=0)
        return self

    def transform(self,X):
        X = as_float_array(X)
        assert X.shape[1] == self.mean.shape[0]  #检查输入数据的列数和均值的列数是否相等  
        return  X > self.mean  






if __name__ == '__main__':
    return_k_feature_chi2()
    
    
