def read_file(filename):
    lines = [line for line in open(filename).readlines()]
    colnames =[]
    rownames = []
    data = []

    colnames = lines[0].strip().split("\t")
    for other_line in lines[1:]:
        line_data = other_line.strip().split("\t")
        rownames.append(line_data[0])
        data.append(list(map(float,line_data[1:])))
    return rownames,colnames,data  

def sim_pearson(v1,v2):
    from scipy.stats import pearsonr
    p,h = pearsonr(v1,v2)
    return 1.0 - p  #相似度越大的物体距离越小



class Bicluster:
    def __init__(self,vec,left=None,right=None,distance=0.0,id=None):
        self.vec = vec
        self.right = right
        self.left = left
        self.distance = distance
        self.id = id


def hcluster(data,distance=sim_pearson):
    current_cluster_id = -1
    distances = {}
    clusters = [Bicluster(line,id = id) for id,line in enumerate(data)]  #每一个 Blog 生成一个类   是层次树的叶子节点

    while len(clusters) > 1:
        lowest_pairs = (0,1)
        closest = 2
        for i in range(len(clusters)):
            for j in range(i+1,len(clusters)):
                if not (clusters[i].id,clusters[j].id) in distances:  
                    distances[(clusters[i].id,clusters[j].id)] = distance(clusters[i].vec,clusters[j].vec)
                d = distances[(clusters[i].id,clusters[j].id)]    
                if d < closest:
                    closest = d
                    lowest_pairs = (i,j)
        merge_vec = [(clusters[lowest_pairs[0]].vec[i] + clusters[lowest_pairs[1]].vec[i]) / 2.0 for i in range(len(clusters[lowest_pairs[0]].vec))]
        new_cluster = Bicluster(merge_vec,left = clusters[lowest_pairs[0]],right = clusters[lowest_pairs[1]],id = current_cluster_id)
        current_cluster_id -= 1
        del clusters[lowest_pairs[1]]
        del clusters[lowest_pairs[0]]
        clusters.append(new_cluster)
 
    return clusters[0]

    








if __name__ == '__main__':
    rownames,colnames,data = read_file("blogdata.txt") 
    print(len(rownames))
    hcluster(data,distance=sim_pearson)  
