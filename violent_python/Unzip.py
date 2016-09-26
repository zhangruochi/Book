import zipfile
from threading import Thread

def test(ZipFile,password):
    try:
        ZipFile.extractall(pwd=password)
        print ("[+]-----password is:" + password.decode("utf8") + "-----[+]\n")

    except Exception as e:
        print (e)
    


def UnzipFile(file):
    ZipFile = zipfile.ZipFile(file)
    with open("dictionary.txt") as dic:
        passwords = dic.readlines();
        for password in passwords:
            password = password.strip("\n").encode("utf8")
            guess = test(ZipFile,password)
            t = Thread(target = test, args=(ZipFile,password))
            t.start()

if __name__ == '__main__':
    UnzipFile("zhang.zip")         

                    


            
            
                    

