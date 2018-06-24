import socket
def retBanner(ip,socket):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket()
        s.connect((ip,connect))
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
def main():
    portlist = [21,22,25,80,110,443]
    for x in range(1,255):
        ip = '192.168.95'+str(x)
        for port in portlist:
            banner = retBanner(ip.port)
            if banner:
                print '[+]'+ip+':'+banner
                checkVulns(banner)
if __name__ == '__main__':
    main()