import os
import random
import time
import ConfigParser
from time import gmtime, strftime, sleep
import socket
import sys

installDir=os.path.dirname(os.path.abspath(__file__)) + '/'
configFile=installDir + "/scanner.conf"
config = ConfigParser.RawConfigParser()
continuePrompt = "\nClick [Return] to continue"
config.read(configFile)
toolDir = installDir + 'toolDir = tools/'
#logDir = installDir + config.get('fsociety', 'logDir')
print(installDir)
class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'


def clearScr():
    os.system('clear')


def yesOrNo():
    return (raw_input("Continue Y / N: ") in yes)

color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]
random.shuffle(color_random)
fsocietyPrompt = "scanner ~# "
class fsociety:
    def __init__(self):
        clearScr()
        self.createFolders()
        print (fsocietylogo + color.RED + '''
       }--------------{+} Coded By h4r15h {+}--------------}
    ''' + color.END + '''
       #{1}--Information Gathering
     ''')
        #choice = raw_input(fsocietyPrompt)
        clearScr()
        #if choice == "1":
        informationGatheringMenu()

class informationGatheringMenu:
    menuLogo = '''
    88 88b 88 888888  dP"Yb
    88 88Yb88 88__   dP   Yb
    88 88 Y88 88""   Yb   dP
    88 88  Y8 88      YbodP
    '''

    def __init__(self):
        clearScr()
        print(self.menuLogo)

        print("  {1}--Nmap - Network Mapper")
        print("  {2}--Host To IP")
        print("  {3}--WPScan")
        print("  {99}-Quit \n")
        choice2 = raw_input(fsocietyPrompt)
        clearScr()
        if choice2 == "1":
            nmap()
        elif choice2 == "2":
            host2ip()
        elif choice2 == "3":
            wpscan()
        elif choice2 == "99":
            sys.exit()
        else:
            self.__init__()
        self.completed()

    def completed(self):
        raw_input("Completed, click return to go back")
        self.__init__()
class nmap:
    nmapLogo = '''
    88b 88 8b    d8    db    88""Yb
    88Yb88 88b  d88   dPYb   88__dP
    88 Y88 88YbdP88  dP__Yb  88"""
    88  Y8 88 YY 88 dP""""Yb 88
    '''

    def __init__(self):
        self.installDir = toolDir + "nmap"
        self.gitRepo = "https://github.com/nmap/nmap.git"

        self.targetPrompt = "   Enter Target IP/Subnet/Range/Host: "

        if not self.installed():
            self.install()
            self.run()
        else:
            self.run()

    def installed(self):
        return (os.path.isfile("/usr/bin/nmap") or os.path.isfile("/usr/local/bin/nmap"))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))
        os.system("cd %s && ./configure && make && make install" %
                  self.installDir)

    def run(self):
        clearScr()
        print(self.nmapLogo)
        target = raw_input(self.targetPrompt)
        self.menu(target)

    def menu(self, target):
        clearScr()
        print(self.nmapLogo)
        print("   Nmap scan for: %s\n" % target)
        print("   {1}--Simple Scan [-sV]")
        print("   {2}--Port Scan [-Pn]")
        print("   {3}--Operating System Detection [-A]\n")
        print("   {4}--bannergrabbing [-A]\n")
        print("   {5}--Complete Scan [Os detection,open ports,bannergrabbing with -Pn] \n")
        print("   {99}-Return to information gathering menu \n")
        response = raw_input("nmap ~# ")
        clearScr()
        logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())
        try:
            if response == "1":
                os.system("nmap -sV -oN %s %s" % (logPath, target))
                response = raw_input(continuePrompt)
            elif response == "2":
                os.system("nmap -Pn -oN %s %s" % (logPath, target))
                response = raw_input(continuePrompt)
            elif response == "3":
                os.system("nmap -A -oN %s %s" % (logPath, target))
                response = raw_input(continuePrompt)
            elif response == "4":
                os.system("nmap -sV %s --script=banner -vv %s" % (logPath, target))
                response = raw_input(continuePrompt)
            
            elif response == "5":
            	os.system("nmap -sO %s --script=banner -Pn -vv %s" % (target,logPath))
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)
class wpscan:
    wpscanLogo = '''
    Yb        dP 88""Yb .dP"Y8  dP""b8    db    88b 88
     Yb  db  dP  88__dP `Ybo." dP   `"   dPYb   88Yb88
      YbdPYbdP   88"""  o.`Y8b Yb       dP__Yb  88 Y88
       YP  YP    88     8bodP'  YboodP dP""""Yb 88  Y8
    '''

    def __init__(self):
        self.installDir = toolDir + "wpscan"
        self.gitRepo = "https://github.com/wpscanteam/wpscan.git"

        if not self.installed():
            self.install()
        clearScr()
        print(self.wpscanLogo)
        target = raw_input("   Enter a Target: ")
        self.menu(target)

    def installed(self):
        return (os.path.isdir(self.installDir))

    def install(self):
        os.system("git clone --depth=1 %s %s" %
                  (self.gitRepo, self.installDir))

    def menu(self, target):
        clearScr()
        print(self.wpscanLogo)
        print("   WPScan for: %s\n" % target)
        print("   {1}--Username Enumeration [--enumerate u]")
        print("   {2}--Plugin Enumeration [--enumerate p]")
        print("   {3}--All Enumeration Tools [--enumerate]\n")
        print("   {99}-Return to information gathering menu \n")
        response = raw_input("wpscan ~# ")
        clearScr()
        logPath = "../../logs/wpscan-" + \
            strftime("%Y-%m-%d_%H:%M:%S", gmtime()) + ".txt"
        wpscanOptions = "--no-banner "
        try:
            if response == "1":
                os.system(
                    "wpscan --url %s --enumerate u --wp-content-dir wp-content" % (target))

                response = raw_input(continuePrompt)
            elif response == "2":
                os.system(
                    "wpscan --url %s --enumerate p --wp-content-dir wp-content " % (target))
                response = raw_input(continuePrompt)
            elif response == "3":
                os.system(
                    "wpscan --url %s --enumerate --wp-content-dir wp-content %s --random-user-agent" % (target,wpscanOptions))
                response = raw_input(continuePrompt)
            elif response == "99":
                pass
            else:
                self.menu(target)
        except KeyboardInterrupt:
            self.menu(target)
class host2ip:
	host2ipLogo = '''
    88  88  dP"Yb  .dP"Y8 888888 oP"Yb. 88 88""Yb
    88  88 dP   Yb `Ybo."   88   "' dP' 88 88__dP
    888888 Yb   dP o.`Y8b   88     dP'  88 88"""
    88  88  YbodP  8bodP'   88   .d8888 88 88
    '''
	def __init__(self):
		clearScr()
		print(self.host2ipLogo)
		host=raw_input("	 Enter the host: ")
		ip=socket.gethostbyname(host)
		print("		%s has the IP %s"%(host,ip))
		response=raw_input(continuePrompt)



ob=informationGatheringMenu()