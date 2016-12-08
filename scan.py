#_*_coding:utf-8_*_
import optparse
import socket
from socket  import  *
def connScan(tgtHost,tgtPort):
    try:
        connSkt=socket(AF_INET,SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('violenpython\r\n')
        results=connSkt.recv(100)
        print '[+]%d/tcp open'%tgtPort
        print'[+]  '+str(results)
    except:
        print '[-]%d/tcp closed' %tgtPort
def portScan(tgtHost,tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host"%tgtHost
        return
    try:
        tgtName=gethostbyaddr(tgtIP)
        print '\n[+] Scan  Result for : '  +tgtName[0]
    except:
        print '\n[+]  Scan Results for: '  +tgtIP
    setdefaulttimeout(1)
    for tgtPort  in tgtPorts:
        print 'Scanning port ' + tgtPort
        connScan(tgtHost,int(tgtPort))
def  main():
    parser=optparse.OptionParser("usage%prog "+  "-H  <target host>-p<targrt port>")
    parser.add_option('-H',dest='tgtHost',type='string',help='specify targt host')
    parser.add_option('-p',dest='tgtPort',type='string',help='specify targt port[s] seprated by comma')
    (options,args)=parser.parse_args()
    tgtHost=options.tgtHost
    tgtPorts=str(options.tgtPort).split(',')
    print tgtPorts
    if (tgtHost==None)| (tgtPorts[0]==None):
        print '[-] You must  specify   atarget host  and port[s]'
        exit(0)
    portScan(tgtHost,tgtPorts)
if __name__=='__main__':
    main()