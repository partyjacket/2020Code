from jsonrpclib import Server
from pprint import pprint as pp
import signal
import yaml
import os


def yload(data):
    safeload = yaml.load(data, Loader=yaml.FullLoader)
    return safeload



class TimeExceededError(object):
    pass


def timeout(signum, frame):
    raise TimeExceededError


signal.signal(signal.SIGALRM, timeout)

numdevs = int(input("Yo sancheeze, how many ips you want me to get after? "))
baseip = '192.168.10.31'

def url(x):
    myurl = f'http://admin:admin@{x}/command-api'
    return myurl

def runcmds(z):
    base = int(baseip.split('.')[-1])
    print(base)
    x = 0
    while x < z:
        print(x, z)
        try:
            signal.alarm(5)
            ip = '.'.join(baseip.split('.')[:-1]) + '.' + str(x + base)
            print(ip)
            switch = Server(url(ip))
            hostname = (switch.runCmds(1, ['show hostname'])[0]['hostname'])
            savecfg = os.system('sshpass -p "admin" scp admin@{}:/mnt/flash/startup-config /Users/jpatterson/Documents/rockies_configs/{}.cfg'.format(ip, hostname))
            print('config saved!')

        except:
            print('Not Arista!')
        x += 1



runcmds(numdevs)





