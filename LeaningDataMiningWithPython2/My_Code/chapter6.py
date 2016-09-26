import os
import numpy as np
import pandas as pd
import json
import nltk

# 加载数据
def load_data():
    input_filename = os.path.join(os.getcwd(),"python_tweets.json")
    label_filename = os.path.join(os.getcwd(),"python_classes.json")

    tweets = []
    label = []

    with open(input_filename,"r") as input_file:
        for line in input_file:
            if len(line.strip())== 0:
                continue
            tweets.append(json.loads(line["text"])) 
    
    with open(label_filename,"r") as label_file:
        label = json.load(f)

    return tweets,label
    
#将文档转化为单词及其是否出现的词典 创造转换器 将接口与 sklearn 统一,方便后面的 pipeline
from sklearn.base import TransformerMixin
from nltk import word_tokenize
class NLKTBOW(TransformerMixin):
    def fit(self,X,y=None):
        return self

    def transform(self,X):
        return [{word: True for word in word_tokenize(document)} for document in X]


#将字典转化为向量矩阵
def dict_vertorizer(X):
    from sklearn.feature_extraction import DictVectorizer
    trans = DictVectorizer()
    trans_X = trans.fit_transform(X)
    print(trans_X)
    return trans_X



# 组装起来
def clf_and_predict(X,y):
    from sklearn.feature_extraction import DictVectorizer
    trans = DictVectorizer()
    from sklearn.naive_bayes import BernoulliNB
    clf = BernoulliNB()
    nltkbow = NLKTBOW()
    from sklearn.pipeline import Pipeline
    pipe = Pipeline([("nlkt",nltkbow),("vertorizer",trans),("naive_bayes",clf)])
    from sklearn.cross_validation import cross_val_score
    
    scores = cross_val_score(pipe,X,y,scoring="f1")
    print(np.mean(scores))

    




# 从模型中获取更多的有用信息
def get_feature():
    model = pipe.fit(X,y)
    
    nb = model.named_steps["naive_bayes"] #访问 第三步骤
    feature_probabilities = nb.feature_log_prob_ #得到每一个特征的概率 并排序
    top_feature = np.argsort(-feature_probabilities[1]) #排序  得到索引

    dv = model.named_steps["vertorizer"] #访问第二步 得到每一个特征的名字
    feature_name = dv.feature_names_

    for i,feature_index in enumerate(top_feature):
        name = feature_name[feature_index]
        print(i,name)

    """
    0 leaf
    1 the
    2 of
    3 to
    4 her
    5 Johnsy
    6 vine
    7 ,
    8 window
    9 is
    10 last
    11 room
    12 now
    """        


if __name__ == '__main__':
    nltkbow = NLKTBOW()



    X = ["A woman nick named Johnsy (her full name is Joanna) had come down with pneumonia","and is now close to death. Outside the window of her room, the leaves fall from a vine. Johnsy decides that when the last leaf drops",\
    "she too will die, while her roommate Sue, who stays with her, tries to tell to stop thinking so pessimistically","A woman nick named Johnsy had come down with pneumonia","and is now close to death","and is now close to death. \Outside the window of her room, the leaves fall from a vine. Johnsy decides  leaf drops",\
    "who is dying of pneumonia, has come to believe that she will die when the last leaf falls off of the vine outside her window"]
    y = np.array([0,1,0,1,0,1,1])
    X = nltkbow.fit_transform(X)
    dict_vertorizer(X)
    clf_and_predict(X,y)





