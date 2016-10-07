critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


from math import sqrt

#计算欧几里得距离
def sim_distance(prefs,person1,person2):
    #找到共同物品
    si= []
    for item in prefs[person1]:
        if item in prefs[person2]:
            si.append(item)

    if not si:
        print("no same item")
        return
   
    euclidean_distance = sqrt(sum([pow(prefs[person1][item] - prefs[person2][item],2) for item in si]))
    rate = 1 / (1 + euclidean_distance)
    #print(rate)
    return rate

#scipy 计算欧几里得距离
def  sim_distance_scipy(prefs,person1,person2):
    from scipy.spatial.distance import euclidean
    si= []
    for item in prefs[person1]:
        if item in prefs[person2]:
            si.append(item)
    if not si:
        print("no same item")
        return
                
    array_person1 = [prefs[person1][item] for item in si]    
    array_person2 = [prefs[person2][item] for item in si]

    euclidean_distance = euclidean(array_person1,array_person2)
    rate = 1 / (1+euclidean_distance)
    print(rate)
    return rate


#计算皮尔逊相关系数
def sim_pearson(prefs,person1,person2):
    si= []
    for item in prefs[person1]:
        if item in prefs[person2]:
            si.append(item)
    if not si:
        print("no same item")
        return

    person1_sum = sum([prefs[person1][item] for item in si])
    person2_sum = sum([prefs[person2][item] for item in si])

    person_1_2_product_sum = sum([prefs[person1][item] * prefs[person2][item] for item in si])

    person1_squre_sum = sum([pow(prefs[person1][item],2) for item in si])
    person2_squre_sum = sum([pow(prefs[person2][item],2) for item in si])

    numerator = person_1_2_product_sum - person1_sum * person2_sum/len(si)
    denominator = sqrt(person1_squre_sum - pow(person1_sum,2)/len(si)) * sqrt(person2_squre_sum - pow(person2_sum,2)/len(si) )

    if denominator == 0:
        return 0

    return numerator/denominator

#scipy 计算皮尔逊相关系数
def sim_pearson_scipy(prefs,person1,person2):
    from scipy.stats import pearsonr
    si= []
    for item in prefs[person1]:
        if item in prefs[person2]:
            si.append(item)
    if not si:
        print("no same item")
        return

    
    array_person1 = [prefs[person1][item] for item in si]    
    array_person2 = [prefs[person2][item] for item in si]

    r = pearsonr(array_person1,array_person2)
    #print(r)
    return r


#寻找与指定人员品味相近的人员列表
def top_matches(prefs,person,n=5,func=sim_distance):

    scores = [(func(prefs,person,other_person),other_person) for other_person in prefs if not other_person is person]
    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommendations(prefs,person,func=sim_pearson):
    from collections import defaultdict
    totals = defaultdict(int)
    sim = defaultdict(int)

    for other_person in prefs:
        if other_person is person:
            continue

        similarity = func(prefs,person,other_person)
        if similarity <= 0:
            continue

        for item in prefs[other_person]:
            totals[item] += prefs[other_person][item] * similarity
            sim[item] += similarity

    ranking = sorted([(totals[item]/sim[item],item) for item in sim],key=lambda x:x[0],reverse = True)
    return ranking             




if __name__ == '__main__':
    print(getRecommendations(critics,'Toby'))


