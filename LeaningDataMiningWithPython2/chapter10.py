import requests
import os
import pickle
from lxml import etree
from lxml import html
import numpy as np

CLIENT_ID = "lwBnqcNX2i1n5Q"
CLIENT_SECRET = "S2-pYaIUSE5-VePO3bA1ZYLxQs0"
USERNAME = "zhangruochi"
PASSWORD = "lv23623600"
USER_AGENT = "python_practice of {}".format(USERNAME)

#获得令牌
def login():
    headers = {"User-Agent": USER_AGENT}
    #创建 HTTP 授权对象 
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID,CLIENT_SECRET)
    post_data = {"grant_type":"password","username":USERNAME,"password":PASSWORD}

    response = requests.post("https://www.reddit.com/api/v1/access_token",auth = client_auth, data = post_data, headers = headers)
    return response.json()


def get_link(token):
    subreddit = "worldnews"
    url = "https://oauth.reddit.com/r/{}".format(subreddit)
    headers = {"Authorization": "bearer {}".format(token["access_token"]),"User-Agent":USER_AGENT}

    response = requests.get(url,headers = headers)
    results = response.json()
    
    for story in results["data"]["children"]:
        print(story["data"]["title"])

def get_links(subreddit,token,n_pages = 5):
    from time import sleep
    headers = {"Authorization":"bearer {}".format(token["access_token"]),"User-Agent" : USER_AGENT}
    stories = []
    after = None

    for page in range(n_pages):
        url = "https://oauth.reddit.com/r/{}?limit=100".format(subreddit)
        
        if after:
            url += "&after={}".format(after)

        response = requests.get(url,headers = headers)
        result = response.json()

        after = result["data"]["after"]
        sleep(2)
        stories.extend([(story["data"]["title"],story["data"]["url"],story["data"]["score"]) for story in result["data"]["children"]])

    with open("stories.pkl","wb") as f:
        pickle.dump(stories,f)

    return stories    

def get_news(filename):
    import hashlib
    
    with open(filename,"rb") as f:
        stories = pickle.load(f)

    data_folder = os.path.join(os.getcwd(),"data","news")
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    num_errors = 0 # 如果所有网页都下载成功 计数器的值应该为0

    for title,url,score in stories:
        print("downloading text form {}".format(url))
        output_filename = hashlib.md5(url.encode()).hexdigest()
        full_path = os.path.join(data_folder,output_filename+".txt")

        try:
            #urlretrieve(url,full_path)
            response = requests.get(url,timeout=10)
            data = response.text
            with open(full_path,"w") as out_file:
                out_file.write(data)
        except Exception as e:
            num_errors += 1
            print(e)        

            if num_errors >100:
                raise e                            

    print("[+] *************downloading completed ! *******************")            


def get_texts():
    documets = []

    text_only_folder = os.path.join(os.getcwd(),"data","text_only")
    if not os.path.exists(text_only_folder):
        os.makedirs(text_only_folder)    

    news_filename = os.listdir(os.path.join(os.getcwd(),"data","news"))
    
    for filename in news_filename:
        full_news_filename = os.path.join(os.getcwd(),"data","news",filename)
        full_text_filename = os.path.join(text_only_folder,filename)
        text = get_text_from_file(full_news_filename)
        documets.append(text)
        with open(full_text_filename,"w") as f:
            f.write(text)

    return documets        
    
def get_text_from_file(filename):
    with open(filename,"r") as f:
        html_tree = html.parse(f)
    return get_text_from_node(html_tree.getroot())        


def get_text_from_node(node):

    skip_node_types = ["script","head","style",etree.Comment]
    if (len(node)) == 0:
        if node.text and len(node.text) > 100 :
            return node.text
        else:
            return ""

    results = [get_text_from_node(children) for children in node if children.tag not in skip_node_types]  
    return "\n".join([result for result in results if len(result) > 0])          


def kmeans_analysis(documets):
    from sklearn.cluster import KMeans
    from sklearn.pipeline import Pipeline
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.grid_search import GridSearchCV


    """
    print("find the best cluster")
    inertia_s = []
    n_clusters = range(2,20)
    for cluster in n_clusters:
        cur_inertia_values = []
        X = TfidfVectorizer(max_df = 0.4).fit_transform(documets)
        # 每个 cluster 算法运行十次
        for i in range(10):
            km = KMeans(n_clusters = cluster).fit(X)
            cur_inertia_values.append(km.inertia_)
        inertia_s.append(cur_inertia_values)

    print(inertia_s)   

    inertia_s = [[364.762648868374, 364.26708631946076, 364.3285449626131, 364.27706153405813, 365.8807214536832, 364.3285449626131, 364.3281891360521, 364.3285449626131, 364.9209934946651, 364.26708631946076], 
    [361.79637985273075, 361.43208472287836, 361.14290181961275, 361.1203197135783, 360.9791992073971, 361.2931398510021, 360.892443941139, 360.9752471025266, 361.7853778699753, 361.12450686836496], 
    [358.99374251710464, 361.3487664478186, 358.71883229651456, 359.52364914921384, 357.47820051563497, 358.4451930083393, 358.22842524414085, 358.84391943567067, 356.06087438382144, 358.55220835717273], 
    [356.17382397454077, 352.6042820271323, 354.25370349332525, 354.59434690335576, 355.60648069970483, 356.00649762935325, 356.21948133792006, 354.9279884647385, 356.3028302396451, 355.6965140987678], 
    [354.32751729146645, 353.2118925696389, 351.11514158143547, 351.76827568768175, 354.3551655413432, 352.2618576936696, 351.9310587456312, 353.6248182279811, 353.3883525490841, 354.6936769758882], 
    [351.42281423706527, 351.78399652581135, 349.3664294359723, 350.55979980424917, 351.9455852600661, 350.62296479919246, 351.16781314432, 350.7094984521188, 351.9218669687004, 349.05327174977515], 
    [350.0618677502329, 347.6481905204669, 349.42057478993075, 349.37726617993127, 348.94879895263864, 349.2867552070841, 348.6148871737493, 348.4912493818705, 346.4929983889673, 348.2820553628324], 
    [347.0616021453253, 346.30424517782177, 344.93191796565736, 345.1067825932356, 346.11244127437647, 344.96660788902295, 346.71172529228164, 346.03291269988125, 347.3604075905083, 348.0457899596928], 
    [345.04874594333586, 344.3335947422679, 345.6481172721348, 344.6756782510634, 342.09193200683, 343.78075060762427, 345.16058710325336, 344.11859107925096, 344.48075031054344, 344.26906295837176],
    [340.42225729437337, 340.99222485261583, 343.73666605177976, 342.74305039166586, 341.61003726622204, 341.97743288796215, 341.45856090768996, 339.735936772623, 341.47102510796026, 341.20152193787357], 
    [341.00615376204365, 342.3346469508683, 336.5547504910347, 339.6683277086436, 339.8944162013256, 339.54832591938185, 343.1686407904863, 341.01059380950136, 337.8501510150431, 339.49547229676375], 
    [338.7392636723574, 338.4893026744616, 338.7073341751628, 338.9895220808968, 341.30632124885193, 334.0165265494053, 337.6907464552258, 337.4776281328628, 340.2016814994333, 339.6173793048041], 
    [333.6858272787883, 337.5183446870793, 335.2271992198759, 334.97575648533194, 334.82218560100387, 336.7007040030289, 338.6350795805228, 338.1402152993126, 336.13566275313445, 337.28947547515565], 
    [336.80468347579233, 339.4521343993808, 338.4199897142796, 334.30454062198845, 335.4605185145177, 331.4183944981725, 333.10855545286626, 330.7622519818422, 332.0455866923502, 333.4018723300752], 
    [331.330319935459, 332.2833489860891, 332.48812954455707, 331.7457631351492, 332.26759539102017, 332.31864753574706, 336.82276453829166, 332.6559140296126, 331.6541567484462, 330.99336334786045], 
    [333.62831864594455, 330.0646577431975, 330.8540199205754, 331.41415265143456, 334.5567361415297, 331.765646985996, 327.9982661644406, 332.33570925640214, 330.96170946142666, 330.2737405764021], 
    [327.5243863538424, 324.9191852237415, 332.737133371412, 328.38106639553376, 330.0060940596061, 327.7230137608319, 328.65499493054574, 327.59525153025226, 328.40631354207267, 329.1446832703496], 
    [326.8241367409064, 328.77588406490963, 325.49073904765663, 327.81039002416577, 328.84158497289064, 326.9335285245928, 324.9414923228598, 323.8299376437848, 325.1771920622977, 327.36074875388437]] 
    
    inertia_s = np.mean(np.array(inertia_s),1)
    print(inertia_s)  #n_cluster = 6 拐点
    
    [ 364.5689422   361.25416009  358.61938114  355.23859489  353.06777569
      350.85540404  348.66246437  346.26344326  344.36078103  341.53487135
      340.05314789  338.52357058  336.31304504  334.51785277  332.45600032
      331.38529575  328.50921224  326.59856342]
    """
    
    n_clusters = 6
    clf = KMeans(n_clusters = n_clusters)
    pipe = Pipeline([("feature_extraction",TfidfVectorizer(max_df = 0.4)),("KMeans",clf)])
    pipe.fit(documets)
    labels = pipe.predict(documets)

    #从簇中抽取主题信息
    from collections import Counter
    terms = pipe.named_steps['feature_extraction'].get_feature_names() #取得特征列表
    c = Counter(labels)
    for cluster_number in range(n_clusters):
        print("cluster {} contains {} samples".format(cluster_number,c[cluster_number]))
        print("The most important terms are: ")
        centroid = pipe.named_steps['KMeans'].cluster_centers_[cluster_number]
        most_important = centroid.argsort()  #argsort函数返回的是数组值从小到大的索引值
        for i in range(5):
            term_index = most_important[-(i+1)]
            print(" {0} {1} score: {2}".format(i+1,terms[term_index],centroid[term_index]))          
        print("\n")        




    print("The distance is : {}".format(pipe.named_steps['KMeans'].inertia_))    

    """
   cluster 0 contains 63 samples
The most important terms are: 
 1 sinai score: 0.05596009704283625
 2 group score: 0.05385869338640432
 3 isis score: 0.05373325395734329
 4 al score: 0.04973017883444858
 5 hamas score: 0.04843572034462471


cluster 1 contains 42 samples
The most important terms are: 
 1 rio score: 0.16188633378482556
 2 olympic score: 0.12142088638879033
 3 athletes score: 0.1076329383553131
 4 russian score: 0.09528716585203793
 5 games score: 0.0761861479448246


cluster 2 contains 15 samples
The most important terms are: 
 1 airport score: 0.15524011525574571
 2 plane score: 0.11990455117432733
 3 road score: 0.09584511738152944
 4 upi score: 0.09158781034167437
 5 runway score: 0.0803638744140956


cluster 3 contains 51 samples
The most important terms are: 
 1 her score: 0.11349225292773361
 2 she score: 0.0991512541704502
 3 his score: 0.05666792746669032
 4 turkey score: 0.05521479337616077
 5 police score: 0.05482270349759372


cluster 4 contains 194 samples
The most important terms are: 
 1 you score: 0.021608790376445634
 2 china score: 0.017724840061873366
 3 his score: 0.016463881958298714
 4 can score: 0.015000694167856503
 5 our score: 0.014551632549237638


cluster 5 contains 38 samples
The most important terms are: 
 1 police score: 0.062397612582447165
 2 attack score: 0.05474331227353553
 3 kokrajhar score: 0.047924066591741345
 4 group score: 0.0459050151029516
 5 assam score: 0.040054922516567226

"""



    
    

    

if __name__ == '__main__':
    documets = get_texts()
    kmeans_analysis(documets)

    
    
    
    
































    
