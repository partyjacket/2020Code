from jsonrpclib import Server

ip = '192.168.10.5'

iplist = ['192.168.10.31', '192.168.10.32']
hostname = 'leaf1'
hostname2 = 'leaf2'

get_seed_vtep = hostname[-2]
get_seed_mlag = hostname[-1]

print(get_seed_vtep)
print(get_seed_mlag)


ipsplit = ip.split('.')

baseip = ipsplit[:-1]

loopbackip = '.'.join(baseip) + "." + get_seed_mlag

print(loopbackip)

url = "http://admin:admin@%s/command-api"


for x in range(len(iplist)):
    print(Server(url % iplist[x]).runCmds(1, ['show version']))