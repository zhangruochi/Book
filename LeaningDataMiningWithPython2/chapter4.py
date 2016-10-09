import os
import pandas as pd
import numpy as np
from itertools import groupby
from collections import defaultdict
import pickle


def loadData():
    fullPathName = os.path.join(os.getcwd(),"ml-100k","u.data")
    print("The full path is:{0} ".format(fullPathName))
    all_ratings = pd.read_csv(fullPathName,delimiter = "\t",names=["UserID","MovieID","Rating","Timestamp"])
    print("loading data successful!\n")
    #print(all_ratings[:5])
    return all_ratings

def prepare():
    all_ratings = loadData()
    all_ratings["Favorite"] = all_ratings["Rating"] > 3

    ratings = all_ratings[all_ratings["UserID"].isin(range(201))] #选取前200名数据
    favorite_ratings = ratings[ratings["Favorite"]] #选取用户关于喜欢电影的数据
    print(favorite_ratings[:5])
    # 我们需要知道每个用户各喜欢哪些电影 按照 UserID 进行分组 
    favorite_reviews_by_users = dict((k,frozenset(v.values)) for k,v in favorite_ratings.groupby("UserID")["MovieID"])
    #print(favorite_reviews_by_users)
    # 创建一个数据框  了解每部电影影迷的数量
    num_favorite_by_movie = ratings[["MovieID","Favorite"]].groupby("MovieID").sum()  #******** 重点 *******     
    #print(dict([(k,list(group)) for k,group in num_favorite_by_movie["Favorite"]]))
    #print(num_favorite_by_movie.sort(columns = "Favorite",ascending=False)[:5])
    return favorite_reviews_by_users,num_favorite_by_movie


# Apriori 算法 用于查找数据集项中的频繁集项
#参数 favorite_reviews_by_users： 各用户评价过的喜欢的电影集合    num_favorite_by_movie：各电影被标记的喜欢的次数
def Apriori(favorite_reviews_by_users,num_favorite_by_movie):
    frequent_itemsets = {}  #将发现的频繁集项保存到以项集长度为键的字典中
    min_support = 50 #最小支持度
    
    #第一步 为每一部电影生成只包含它自己的项集 并检测它是否够频繁
    frequent_itemsets[1] = dict((frozenset((movie_id,)),row["Favorite"] ) for movie_id,\
        row in num_favorite_by_movie.iterrows() if row["Favorite"] > min_support)
    
    #开始迭代
    for k in range(2,20):
        cur_frequent_itemsets = find_frequent_itemsets(favorite_reviews_by_users, \
            frequent_itemsets[k-1], min_support)
        frequent_itemsets[k] = cur_frequent_itemsets
        if len(cur_frequent_itemsets) == 0:
            print("[-] can not find any frequent itemsets of length {0}".format(k))
            break
        else:
            print("[+] I find {0} frequent itemset of length {1}".format(len(cur_frequent_itemsets),k))
    del frequent_itemsets[1] # 只有一项没有意义  不具有关联规则        
    
    # 运行时间比较长  采用 pickle 保存数据
    
    try:
        with open("frequent_itemsets.pkl","wb") as f:
            pickle.dump(frequent_itemsets,f)
    except pickle.PickleError as e:
        print("pickling error " + str(e))

    return  frequent_itemsets   

#接受新发现的频繁集 创建超集 检测频繁程度
def find_frequent_itemsets(favorite_reviews_by_users,k_i_itemsets,min_support):
    counts = defaultdict(int)  
    for user, reviews in favorite_reviews_by_users.items():
        for itemset in k_i_itemsets:
            if itemset.issubset(reviews):
                for other_reviews_movie in reviews - itemset:
                    current_superset = itemset | frozenset((other_reviews_movie,))
                    counts[current_superset] += 1

    return dict([(itemset,frequency) for itemset,frequency in counts.items() if frequency > min_support])                

#抽取关联规则           
def getRules():
    try:
        with open("frequent_itemsets.pkl","rb") as f:
            frequent_itemsets = pickle.load(f)
    except pickle.PickleError as e:
        print("picking error "+ str(e))                

    candidate_rules = []

    for itemset_length, itemsets_counts in frequent_itemsets.items():
        for itemset in itemsets_counts.keys():
            #遍历项集中每一部电影 把他们作为结论  项集中的其他电影作为前提  形成备选规则
            for conclusion in itemset:
                premise = itemset - set((conclusion,))
                candidate_rules.append((premise,conclusion))
    """
    #查看不同程度的关联规则
    for itemset_length, itemsets in frequent_itemsets.items():
        print("[+]the rule length is {0}".format(itemset_length))
        sorted_itemsets = sorted(itemsets.items(), key = lambda x:x[1],reverse = False)
        print(sorted_itemsets[:5])
        print("\n")
    """          
    return candidate_rules


#计算规则的置信度 并排序
def confidence(candidate_rules):
    correct_counts = defaultdict(int)
    incorrect_counts = defaultdict(int)
    favorite_reviews_by_users,num_favorite_by_movie = prepare()

    for user,reviews in favorite_reviews_by_users.items():
        for rules in candidate_rules:
            premise,conclusion = rules
            if premise.issubset(reviews):
                if conclusion in reviews:
                    correct_counts[rules] += 1
                else:
                    incorrect_counts[rules] += 1    
    #规则应验的次数除以前提出现的总次数等与置信度
    rule_confidence = {rules: correct_counts[rules] / float(correct_counts[rules]+incorrect_counts[rules]) for rules in candidate_rules }   
    #对置信度字典进行排序后选出前五条规则
    from operator import itemgetter
    sorted_rule_confidence = sorted(rule_confidence.items(),key = itemgetter(1),reverse = True)
    # 数据格式[((frozenset({56, 258, 172, 181, 7}), 50), 1.0), ((frozenset({1, 172, 79, 50, 181, 222}), 174), 1.0).........
    
    """
    for index in range(5):
        print("Rule #{0}".format(index+1))
        (premise,conclusion) = sorted_rule_confidence[index][0]
        premise_name = ",".join([getName(movie_id) for movie_id in premise])
        conclusion_name = getName(conclusion)
        print("if a person likes {0}, they will always likes {1}".format(premise_name,conclusion_name))
        print("- rule_confidence:{0:3f} %".format(sorted_rule_confidence[index][1] * 100))            
    """

    return sorted_rule_confidence


#加载包含电影名称的数据
def loadNameData():
    movie_name_filename = os.path.join(os.getcwd(),"u.item")
    movie_name_data = pd.read_csv(movie_name_filename,header=None,delimiter = "|",encoding="mac-roman" )
    movie_name_data.columns = ["MovieID","Title","Release Date","Video Release","IMDB","<UNK>",
                                "Action","Adventure","Animation","Children's","Comedy","Crime",\
                                "Documentary","Drama","Fantasy","Film-Noir","Horror","Musical",\
                                "Mystery","Romance","Sci-Fi","Thriller","War","Western"]
    
    print(movie_name_data.ix[:5])
    return movie_name_data


#根据电影的编号读取电影的名字
def getName(movie_id):
    movie_name_data = loadNameData()
    title = movie_name_data[movie_name_data["MovieID"] == movie_id]["Title"].values[0]
    return title

#根据电影名字得到电影编号
def getId(movie_name):
    movie_id_data = loadNameData()
    id = movie_id_data[movie_id_data["Title"] == movie_name]["MovieID"].values[0]
    return id

def recommander(movie_name):
    movie_id = getId(movie_name)
    candidate_rules = getRules()
    sorted_rule_confidence = confidence(candidate_rules)

    movies = []

    for rule_confidence in sorted_rule_confidence:
        premise,conclusion = rule_confidence[0]
        if movie_id in premise:
            movies.append(conclusion)

    recommand_movies = movies[:5]
    recommand_movies_name = ",".join([getName(id) for id in recommand_movies])
    print("if you like the {0}, you probably like {1}".format(movie_name,recommand_movies_name))

                







if __name__ == '__main__':
    prepare()
   
    
    


