import pandas as pd 
import numpy as np
from copy import copy
import os
from collections import defaultdict

#简单的数据清洗
def loadData(filename):
    i = range(1,1231)
    dataset = pd.read_csv(filename,header=None)
    dataset.columns = ["Date","Start","Score Type","Visitor Team","VisitorPts","Home Team","HomePts","OT?","Notes"]
    print(dataset.ix[:5])
    return dataset

#找出主场获胜的球队
def findHomeWinTeam(dataset):
    dataset["HomeWin"] = dataset["VisitorPts"] < dataset["HomePts"]  # 给 dataFrame 添加新的数据列
    y_true = dataset["HomeWin"].values
    homeWinTeamlabel = np.zeros((1230,))
    for i,v in enumerate(y_true):
        if v == True:
            homeWinTeamlabel[i] = 1       
    return homeWinTeamlabel,dataset        

#找出每行数据的两支球队在各自的上一场比赛有没有获胜的 增加两个特征
def findLastWonTeam(dataset):
    from collections import defaultdict
    wonLast = defaultdict(bool) #字典的 key 为球队  value 为是否赢得上一场比赛
    for index,row in dataset.iterrows():
        homeTeam = row["Home Team"]
        visitorTeam = row["Visitor Team"]
        #row["HomeLastWin"] = wonLast[homeTeam]  # 第一次遍历时默认为0
        #row["VisitorLastWin"] = wonLast[visitorTeam] # 每更新一行，为其增加两个特征值 
        dataset.loc[index,"HomeLastWin"] = wonLast[homeTeam]
        dataset.loc[index,"VisitorLastWin"] = wonLast[visitorTeam]
        wonLast[homeTeam] = row["HomeWin"] # 记录 homeTeam 有没有赢  作为下次遍历的上场比赛的数据
        wonLast[visitorTeam] = not row["HomeWin"]
        
    return dataset

#使用决策树进行预测
def prediction(dataset,label,feature):
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.cross_validation import cross_val_score
    clf = DecisionTreeClassifier(random_state = 14)
    scores = cross_val_score(clf,dataset[feature].values,label,scoring="accuracy")
    print("The accuracy is: {0:1f} %".format(np.mean(scores) * 100))



# 创建一个新特征 “主场队是否通常比对手水平高 “ 使用2015年赛季排名为数据来源  
def loadData2015(filename):
    fullPathName = os.path.join(os.getcwd(),filename)
    standing = pd.read_csv(fullPathName,skiprows=[0]) #跳过第0行
    return standing
    #print(dataset)

# 为元数据集增加新特征  HomeTeamRanksHigher
def addNewFeature1(dataset):
    filename = "2015.csv"
    standing = loadData2015(filename)
    dataset["HomeTeamRanksHigher"] = 0
    for index,row in dataset.iterrows():
        homeTeam = row["Home Team"]
        visitorTeam = row["Visitor Team"]
        homeRank = standing[standing["Team"] == homeTeam]["Rk"].values[0]
        visitorRnak = standing[standing["Team"] == visitorTeam]["Rk"].values[0]
        dataset.loc[index,"HomeTeamRanksHigher"] =  int(homeRank <  visitorRnak)    
    return dataset

# 为元数据集增加新特征  上一次两只球队交手的情况
def addNewFeature2(dataset):
    last_match_winner = defaultdict(bool)
    dataset["HomeTeamWonLast"] = 0
    for index, row in dataset.iterrows():
        homeTeam = row["Home Team"]
        visitorTeam = row["Visitor Team"]
        teams = tuple(sorted([homeTeam,visitorTeam]))
        dataset.loc[index,"HomeTeamWonLast"] = 1 if last_match_winner[teams] == \
        row["Home Team"] else 0
        winner = row["Home Team"] if row["HomeWin"] else row["Visitor Team"]
        last_match_winner[teams] = winner

    return dataset

#队名转换并预测  
def TeamNameComvert():
    from sklearn.preprocessing import LabelEncoder
    filename = "2016.csv"
    dataset = loadData(filename)
    homeWinTeamlabel,dataset = findHomeWinTeam(dataset)
    
    encoding = LabelEncoder() #LabelEncoder 可以将字符串类型转换为整型 ["zhang","ruochi","zhang","li","xiao","yue"] -> [4 1 4 0 2 3] <type 'numpy.ndarray'>
    encoding.fit(dataset["Home Team"].values)
    homeTeam = encoding.transform(dataset["Home Team"].values)
    visitorTeam = encoding.transform(dataset["Visitor Team"].values)
    x_teams = np.vstack([homeTeam,visitorTeam]).T # 将visitorTeam 矩阵添加到 homeTeam 矩阵后面组成新矩阵

    from sklearn.preprocessing import OneHotEncoder #对于分类类型的特征  将数据转换成独热编码
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.cross_validation import cross_val_score 
    onehot = OneHotEncoder()
    x_teams_expanded = onehot.fit_transform(x_teams).todense()
    clf = DecisionTreeClassifier(random_state = 14)
    scores = cross_val_score(clf,x_teams_expanded,homeWinTeamlabel,scoring="accuracy")
    print("The accuracy is : {0:1f} %".format(np.mean(scores) * 100 ))

#使用随机森林进行预测
def prediction2(dataset,homeWinTeamlabel,feature):
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.grid_search import GridSearchCV
    parameters = {
        "max_features": [2,10,"auto"],
        "n_estimators":[100,200],
        "criterion":["gini","entropy"],
        "min_samples_leaf":[2,4,6],
    }
    clf = RandomForestClassifier(random_state = 14)
    grid = GridSearchCV(clf,parameters)
    grid.fit(dataset[feature].values,homeWinTeamlabel)
    print("accuracy is: {0:1f}".format(grid.best_score_ * 100))

    print("the parameters is: {0}".format(grid.best_estimator_))





if __name__ == '__main__':
    loadData("2016.csv")
    
   




