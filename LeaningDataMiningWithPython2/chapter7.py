import random
import networkx as nx 
from matplotlib import pyplot as plt


# 假设生成150民核心用户
def generate_relationship():
    random.seed(10)
    friends = {x :[random.randint(0,250) for i in range(100)] for x in range(150) }
    friends = {x :list(set(friends[x])) for x in friends } 
    return friends

# 绘制150名核心用户的链接关系
def create_graph(friends):
    G = nx.DiGraph()
    main_users = friends.keys() 
    G.add_nodes_from(main_users)
    for main_user in main_users:
        for friend in friends[main_user]:
            if friend in main_users:
                G.add_edge(main_user,friend)

    
    plt.figure(3,figsize=(20,20))
    nx.draw(G,alpha=0.1,edge_color='b')
    plt.show()

# 创建用户相似度
def create_similarity_graph(friends,threshold):
    G = nx.DiGraph()
    friends = {user: set(friends[user]) for user in friends}
    for user1 in friends.keys():
        for user2 in friends.keys():
            if user1 == user2:
                continue
            weight = compute_similarity(friends[user1],friends[user2])
            #print(weight)
            if weight > threshold:
                G.add_node(user1)
                G.add_node(user2)
                G.add_edge(user1,user2,weight=weight)
    return  G


#使用 spring_layput布局方法
def spring_layout_graph(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G,pos)
    edgewidth = [d["weight"] for (u,v,d) in G.edges(data=True)]
    plt.figure(figsize=(10,10))
    nx.draw_networkx_edges(G,pos,width = edgewidth)
    plt.show()



#相似度计算
def compute_similarity(friend_set1,friend_set2):
    return len(friend_set1 & friend_set2) / len( friend_set1 | friend_set2)



#寻找连通分支
def create_connected_component(friends,threshold):
    G = create_similarity_graph(friends,threshold)
    sub_graphs = nx.connected_component_subgraphs(G)
    
    for i,sub_graph in enumerate(sub_graphs):
        n_nodes = len(sub_graph.nodes())
        print("Subgraphs {0} has {1} nodes".format(i,n_nodes))
    


#参数最优化 采用轮廓系数
def compute_silhoutte(threshold,friends):
    G = create_similarity_graph(friends,threshold)
    if len(G.nodes()) < 2:  #计算轮廓系数要求至少有两个顶点
        return -99

    sub_graphs = nx.connected_component_subgraphs(G)

    if not (2 <= nx.number_connected_components() < len(G.nodes()) - 1） : #轮廓系数要求至少有两个连通分支  且其中一个连通分支有两个顶点
        return -99

    # 给每个顶点标记所属的连通分支类别
    label_dict = dict()
    for i, sub_graph in sub_graphs:
        for node in sub_graph.nodes():
            label_dict[node] = i
    label = [label_dict[node] for node in G.nodes]

    #轮廓系数接收的是距离矩阵 而不是图
    X = nx.to_scipy_sparse_matrix(G).todense()
    X = 1-X    #边的距离是权重的倒数

    from sklearn.metrics import silhouette_score

    return  silhouette_score(X,laebl,metrics="precomputed")

#scipy 的 optimize 函数计算的值是越小越好
def inverted_silhoutte(threshold,friends):
    return -compute_silhoutte(threshold.friends)

#优化
def get_result(friends,threshold):
    from scipy.optimize import minimize 
    result = minimize(inverted_silhoutte,args=(friends,threshold))




            
if __name__ == '__main__':
    friends = generate_relationship()
    create_connected_component(friends,0)
    