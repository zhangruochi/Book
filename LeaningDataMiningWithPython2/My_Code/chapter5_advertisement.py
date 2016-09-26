import os
import numpy as np
import pandas as pd
from collections import defaultdict

def load_data():
    full_path_name = os.path.join(os.getcwd(),"ad-dataset","ad.data")
    
    """这里的defaultdict(function_factory)构建的是一个类似dictionary的对象，
    其中keys的值，自行确定赋值，但是values的类型，是function_factory的类实例，
    而且具有默认值
    """
    converters = defaultdict(convert_number)
    converters[1558] = lambda x:1 if x.strip() == "ad." else 0 
    ads = pd.read_csv(full_path_name,header=None,converters ={x:convert_number for x in range(1558)})
    print (ads)

    X = ads.drop(1558,axis=1).values  #标签和数据分开
    y = ads[1558]
    y=np.array([ convert_label(x) for x in y.values])

    return X,y

#字符串转数字函数
def convert_number(number_string):
    try:
        number = float(number_string)
        return number
    except ValueError:
        return 0        

#标签转换为数字
def convert_label(label):
    if label.strip() =="ad.":
        return 1
    if label.strip() =="nonad.":
        return 0

    raise ValueError("label error")    


# PCA 主成分分析
def pca_analysis(X):
    from sklearn.decomposition import PCA
    pca = PCA(n_components = 5)
    x_reduction = pca.fit_transform(X)
    np.set_printoptions(precision = 3,suppress = True)
    print(pca.explained_variance_ratio_)
    return x_reduction


#预测函数
def predict(X,y):
    from sklearn.cross_validation import cross_val_score
    from sklearn.tree import DecisionTreeClassifier
    clf = DecisionTreeClassifier()
    scores = cross_val_score(clf,X,y,scoring="accuracy")
    print("The accuracy is: {0}".format(np.mean(scores)))


#PCA 的另一大好处就是使数据可视化
def pca_vision(X,y):
    from matplotlib import pyplot as plt
    classes = set(y) #只有两个 0 或者 1
    colors = ['red','green']
    for cur_class,cur_color in zip(classes,colors):
        mask = (y == cur_class )
        plt.scatter(X[mask,0],X[mask,1],marker="o",color=cur_color,label=int(cur_class))
    plt.legend()
    plt.show()    




if __name__ == '__main__':
    load_data()
                        
