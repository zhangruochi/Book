import re
import reprlib
from collections import abc

RE_WORD = re.compile("\w+")


#第一个版本
class Sentence:

    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self,index):
        return self.words[index]

    
    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.txt) 




s = Sentence("Pig and Pepper")
iter_s = iter(s)

print(isinstance(iter_s,abc.Iterator))

print(next(iter_s))
print(next(iter_s))
print(list(iter_s))




#第二个版本, 可迭代对象
class Sentence_two:

    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.txt) 

    #返回一个迭代器
    def __iter__(self):
        return SentenceIterator(self.words)   


#迭代器
class SentenceIterator:
    def __init__(self,words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[index]
        except IndexError:
            raise StopIteration() 
        self.index += 1
        return word

    def __iter__(self):
        return self                        



#第三个版本， 可迭代对象
class Sentence_three:
    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.txt)

    #生成器，用于构造迭代器
    def __iter__(self):
        for word in self.words:
            yield word
        return     



#-----for语句的作用-------
for word in Sentence_three("Pig and Pepper"):
    print(word)

print("---------") 
g = iter(Sentence_three("Pig and Pepper"))  #返回迭代器
while True:
    try:
        print(next(g))
    except StopIteration:
        del g
        break    



#第四版  惰性实现
class Sentence_four:
    def __init__(self,text):
        self.text = text

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.txt)

    #生成器，用于构造迭代器
    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()
   



class ArithmeticProgression:
    def __init__(self,start,step,end = None):
        self.start = start
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.start + start.step)(self.start)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.start + self.step * index
            



