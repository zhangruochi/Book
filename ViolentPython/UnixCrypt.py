import crypt

def testPass(cryptPass):
    salt = cryptPass[:2]

    with open("dictionary.txt","r") as dictFile:
        for word in dictFile.readlines():
            word = word.strip("\n")
            cryptWord = crypt.crypt(word,salt)
            if(cryptWord == cryptPass):
                print("[+]---founded the password---[+]" + word + "\n")
                return 

            else:
                print("--not found---")

def main():
    passFile = open('shadow.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.strip("\n").split(':')[0]
            cryptPass = line.strip("\n").split(':')[1].strip(' ')
            print('[*] Cracking Password For: ' + user)
            testPass(cryptPass)

if __name__ == '__main__':
    main()
