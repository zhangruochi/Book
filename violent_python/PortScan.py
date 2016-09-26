import optparse
from socket import * 

def optParse():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
    parser.add_option("-H",dest="tgtHost",type="string",help="specify target host")
    parser.add_option("-p",dest="tgtPort",type="string",help="specify target port")

    (options,args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(" ")

    if((tgtHost == None) | (tgtPorts[0] == None)):
        print(parser.usage)

    return tgtHost,tgtPorts   

def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send("Hi I am Doraemon!")
        results = connSkt.recv(100)
        print("[+]%d tcp open" % tgtPort)
        print("[+] " +str(results))
        connSkt.close()
    except:
        print("[-]%d tcp open" % tgtPort)    

def portScan(tgtHost,tgtPorts):
    try:
        tgtIp = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
        return 
    try:
        tgtName = gethostbyaddr(tgtIp)
        print("\n[+] Scan results for: " + tgtName[0])
    except:
        print('\n[+] Scan results for: ' + tgtIp)

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print("Scaning port " + tgtPort)
        connScan(tgtHost, int(tgtPort))

def main():
    tgtHost,tgtPorts = optParse()
    portScan(tgtHost,tgtPorts)

        
if __name__ == '__main__':
    main()
    