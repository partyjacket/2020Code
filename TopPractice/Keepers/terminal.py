import os

from jsonrpclib import Server

ip = '192.168.10.31'
user = 'admin'
passwd = 'admin'

url = f'http://admin:admin@{ip}/command-api'

ss = Server(url)

hostname = (ss.runCmds(1, ['show hostname'])[0]['hostname'])


os.system('sshpass -p "admin" scp rl11:/mnt/flash/startup-config /Users/jpatterson/Documents/{}.cfg'.format(hostname))