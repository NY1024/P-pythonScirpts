import socket
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect(ip,port)
        banner = s.recv(1024)
        return banner
    except:
        return
def checkVulns(banner):
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print '[+]FreeFloat FTP Server is vulnerable'
    elif '3Com 3CDermon FTP Server Version 2.0' in banner:
        print '[+]3CDermon FTp Server is vulnerable'
    elif 'Sami FTP Server 2.0.2' in banner:
        print '[+]Sami FTP Server is vulnerable'
    else:
        print '[-]Ftp Server is not vulnerable'
    return
def  main():
    ip1='192.x.x.x'
    ip2='192.168.x.x'
    ip3='192.168.21.x'
    port = 21
    banner1 = retBanner(ip1,port)
    if banner1:
        print '[+]' +ip1 +':'+banner1.strip('\n')
        checkVulns(banner1)
    banner2 = retBanner(ip2,port)
    if banner2:
        print '[+]' +ip2 +':'+banner2.strip('\n')
        checkVulns(banner2)
    banner3 = retBanner(ip3,port)
    if banner3:
        print '[+]' +ip3 +':'+banner3.strip('\n')
        checkVulns(banner3)
if __name__ == '__main__':
    main()