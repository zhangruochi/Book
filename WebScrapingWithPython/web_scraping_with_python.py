from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import re
import csv
import requests
import pickle


#抽取某个标签的内容
def getH1(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("can not find the page")
        return None
    try:
        bs4Obj = BeautifulSoup(html.read(),"html.parser")
        title = bs4Obj.body.h1
    except AttributeError as e:
        print("can not find the attribute")
        return None
    return title

#抽取某个标签的数量
def getAttributeNumber(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs4Obj = BeautifulSoup(html.read(),"html.parser")
        attributeList = bs4Obj.findAll(text = "the prince")
        number = len(attributeList)
    except AttributeError as e:
        return None
    return number        

#根据标签的名称和属性抽取多个标签的内容
def getAttributes(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs4Obj = BeautifulSoup(html.read(),"html.parser")
        attributes = bs4Obj.findAll("span",{"class":{"green","red"}})
    except AttributeError as e:
        return None
    return attributes 

#抽取某个标签的子标签
def getChildOfAttribute(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs4Obj = BeautifulSoup(html.read(),"html.parser")
        childs = bs4Obj.find("table",{"id":"giftList"}).children
    except AttributeError as e:
        return None
    return childs

#抽取某个标签的兄弟标签
def getSibingOfAttribute(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs4Obj = BeautifulSoup(html.read(),"html.parser")
        #print(bs4Obj.table)
        siblings = bs4Obj.find("table",{"id":"giftList"}).tr.next_siblings
    except AttributeError as e:
        print("2")
        return None
    return siblings    


#字符串匹配查找图片路径
def getImgAddr(url):
    pattern = re.compile("\.\.\/img\/gifts\/img.*\.jpg")
    try:
        html = urlopen(url)
    except HTTPError as error:
        return None
    try:
        bs4Obj = BeautifulSoup(html.read(),"html.parser")
        srcs = bs4Obj.findAll("img",{"src":pattern})
    except AttributeError as e:
        return None
    return srcs            
        

#遍历整个 wiki （去重）
def allWikiUrl(URL):
    global pages
    html = urlopen(url)
    bs4Obj = BeautifulSoup(html.read(),"html.parser")
    pattern = re.compile("^(/wiki/)")
    links = bs4Obj.find("a",{"href":pattern})
    for link in links:
        if href in link.attrs:
            if link not in pages:
                newPages = link.attrs["href"]
                pages.add(link)
                allWikiUrl(link)

#下载图片文件
def downloadImg(url):
    html = urlopen(url)
    bs4Obj = BeautifulSoup(html.read(),"html.parser")
    logo = bs4Obj.find("a",{"id":"logo"}).find("img")
    urlretrieve(logo["src"],"logo.jpg")


#把数据存储到 CSV
def saveCsvFile():
    csvFile = open("myFile.csv","w+")
    try:
        csvWriter = csv.writer(csvFile)
        csvWriter.writerow(("number","number+2","number+4"))
        for i in range(5):
            csvWriter.writerow((i,i+2,i+4))
    finally:
        csvFile.close()        


#把表格存储到 CSV
def saveTable2Csv(url):
    csvFile = open("table.csv","w+",encoding="utf8")
    
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("can not find the page")
        return None
    try:
        bs4Obj = BeautifulSoup(html.read(),"html.parser")
        table = bs4Obj.find("table",{"id":"giftList"}).findAll("tr")
    except AttributeError as e:
        return None

    try:
        csvWriter = csv.writer(csvFile)
        for item in table:
            csvRows = []
            contents = item.findAll(["td","th"])
            for item in contents:
                csvRows.append(item.get_text().strip())
            csvWriter.writerow(csvRows)               
    finally:
        csvFile.close()    

#提交文章表单
def postTextForm(url):
    password = {"firstname":"ruochi","lastname":"zhang"}
    r = requests.post(url,data=password)
    print(r.text)

#提交图片表单
def postImgForm(url):
    file = {"uploadFile":open("1.jpg","rb")}
    r = requests.post(url,files = file)
    print(r.text)

#保存登录网站的 cookies
def saveCokies(url):
    password = {"username":"zhangruochi","password":"password"}
    r = requests.post(url,password)
    with open("cookies.pkl","wb") as f:
        pickle.dump(r.cookies,f)

#使用 cookies 登录
def loginUsingCookies(url,file):
    with open(file,"rb") as f:
        cookies = pickle.load(f)
        r = requests.get(url,cookies = cookies)
    print(r.text)

#使用 session 进行持续跟踪
def useSession(url):
    session = requests.Session()
    password = {"username":"zhangruochi","password":"password"}
    s = session.post(url,password)
    s = session.get(url)
    print(s.text)

#使用 HTTP 认证
def httpLogin(url):
    from requests.auth import AuthBase
    from requests.auth import HTTPBasicAuth

    auth = HTTPBasicAuth("zhangruochi","password")
    r = requests.post(url,auth = auth)
    print(r.text) 
 

#使用请求头 headers
def headerlogin(url):
    headers ={"user-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/601.6.17 (KHTML, like Gecko) Version/9.1.1 Safari/601.6.17",
              "Accept-Encoding":   "gzip, deflate",
              "Accept-Language":  "en-ch",
              "Accept":    "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
              "Referer":  "http://uims.jlu.edu.cn/ntms/userLogin.jsp?reason=logout",
              "Origin":   "http://uims.jlu.edu.cn"
             }

    payload =  {"j_username":"53140620",
             "pwdPlain": "lv23623600"
            }        
    
    req = requests.post(url, data = payload,headers = headers)
    print(req.text)



if __name__ == '__main__':

    url = "http://uims.jlu.edu.cn/ntms/index.do;jsessionid=2017971DA638809D068E3C2799DDA2EC.s9#f=perInfo.stu_infor_table&p=fix"
    headerlogin(url)





    