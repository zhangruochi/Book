import hashlib,binascii

def testPass(sha512Pass):
    salt = sha512Pass[:2]

    with open("dictionary.txt","r") as dictFile:
        for word in dictFile.readlines():
            word = word.strip("\n")
            dk = hashlib.pbkdf2_hmac('sha512', b'word', b'salt' , 100000)
            if(binascii.hexlify(dk) == sha512Pass):
                print("[+]---founded the password---[+]" + word + "\n")
                return 

            else:
                print("--not found---")

def main():
    passFile = open('shadow.txt')
    for line in passFile.readlines():
        if ':' in line:
            user = line.strip("\n").split(':')[0]
            sha512Pass = line.strip("\n").split(':')[1].strip(' ')
            print('[*] Cracking Password For: ' + user)
            testPass(sha512Pass)

if __name__ == '__main__':
    main()