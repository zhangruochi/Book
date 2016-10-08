#-*-coding:utf8-*-
import re
import feedparser
from collections import defaultdict
import csv
import socket

socket.setdefaulttimeout(5)

def get_word_counts(url):
    print(url)
    d= feedparser.parse(url)
    wc = defaultdict(int)

    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        words = get_words(e.title+' '+e.summary)

        for word in words:
            wc[word] += 1
          

    return getattr(d.feed, 'title', 'Unknown title'),wc

def get_words(html_text):
    text = re.compile(r"<[^>]+>").sub('',html_text)
    words_list = re.compile(r"[^A-Z^a-z]+").split(text)    
    return [word.lower() for word in words_list if word != ' ']


def get_frequent():
    blog_count = defaultdict(int)  #记录出现这些单词的博客的数目
    word_count = defaultdict(int)  #记录所有单词及其出现的数量

    file_url = [line for line in file("feedlist.txt")]

    for url in file_url:
        title,wc = get_word_counts(url)
        word_count[title] = wc

        for word in wc:
            blog_count[word] += 1

    return blog_count,word_count,file_url        

    
def filter_words(blog_count,file_url):
    words_list = []
    for word,count in blog_count.items():
        if float(count) / len(file_url) < 0.5  and  float(count) / len(file_url) > 0.1:
            words_list.append(word)
    print(words_list)        
    return words_list        


def main():
    
    blog_count,word_count,file_url = get_frequent()
    words_list = filter_words(blog_count,file_url)
 
    """
    import pickle
    with open("load.pkl","wb") as f:
        pickle.dump([words_list,blog_count,word_count],f)
    
    with open("load.pkl","rb") as f:
        words_list,blog_count,word_count = pickle.load(f)
    """

    with open("blogdataset.csv",'wb') as csvfile:
        writer = csv.writer(csvfile,delimiter=",")

        col = ["Blog"]
        row = []
        for word in words_list:
            col.append(word)

        writer.writerow(col)
        
        for title, wc in word_count.items():
            row.append(title)
            for word,count in wc.items():
                row.append(count)

            writer.writerow(row)
            row = []

#使用 sklearn 进行文本挖掘
def sklearn_main():
    from sklearn.feature_extraction.text import CounterVectorizer

    blog_list = []

    ile_url = [line for line in file("feedlist.txt")]

    for url in file_url:
        print(url)
        d= feedparser.parse(url)
        wc = defaultdict(int)

        for e in d.entries:
            if 'summary' in e:
                summary = e.summary
            else:
                summary = e.description

            words = get_words(e.title+' '+e.summary)
            blog_list.append(words)

    cl = CounterVectorizer()
    result = cl.fit_transform(input=blog_list,max_df=0.5,min_df=0.1)
    vocabulary =  cl.vocabulary_ 

    with open("blogdataset2.csv",'wb') as csvfile:
        writer = csv.writer(csvfile,delimiter=",")
        writer.writerow(vocabulary_)
        for line in result:
            writer.writerow(line)        
    
    return result        
            





if __name__ == '__main__':
    sklearn_main()
               












