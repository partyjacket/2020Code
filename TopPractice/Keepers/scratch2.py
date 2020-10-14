from jsonrpclib import Server

list_of_eapi_calls = []

user = 'admin'
passwd = 'admin'
ip = '192.168.10.1'

url = 'http://%s:%s@%s/command-api' % (user, passwd, ip)

url2 = 'http://{}:{}@{}/command-api'.format(user, passwd, ip)

url3 = f'http://{user}:{passwd}@{ip}/command-api'

# print(url, url2, url3, sep='\n')


listofips = ['192.168.10.1', '192.168.10.2']


bwq = ".".join(ip)
print(bwq)