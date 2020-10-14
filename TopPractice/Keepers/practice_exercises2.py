
from pprint import pprint as pp
from jsonrpclib import Server

def q(x):
    return f'http://admin:admin{x}/command-api'

# mydict = {'big': 'boy'}
dict1 = {1: 'one', 2: 'two'}
dict2 = {}
# #reverse the key value on dict1 using function called "swap" and assign to dict2
def swap(x):
    for k, v in x.items():
        dict2[v] = k
swap(dict1)
print(dict2)




# #reverse the key values back to dict1 original and assign to dict3 using dictionary comprehension
dict3 = {v: k for k, v in dict2.items()}
print(dict3)



# #remap the digit value of dict2 to increment by one using a function called "remap" and assign it to dict4
# #send dict2 as tuple to remap to add one to the digit in index[1] using "dict" method (this is not comprehension)
def remap(x):
    return x[0], x[1] + 1

dict4 = dict(remap(x) for x in dict2.items())
print(dict4)


# # sort based on length of list object
listoflens = ['dddd', 'bb', 'ccc', 'a']
listoflens.sort(key=lambda x: len(x))
print(listoflens)


# # create a url object using the list below with map, then do it again making object url2 with list comprehension
ipadd = ['192.168.10.1', '192.168.10.2']
url = list(map(lambda x: q(x), ipadd))
print(url)
url2 = [q(x) for x in ipadd]
print(url2)



# #print each of these sorting on last name
namelist = ['Jason Zatterson', 'Zig Boy']
namedict = {'Jason': 'Zatterson', 'Zig': 'Boy'}
newtuple = [('Jason Zatterson'), ('Zig Boy')]




#add one to each number and return list using a map
numlist = [1, 2, 3]
numlist = map(lambda x: x + 1, numlist)
print(list(numlist))


# #sort ips based on last octet
listofips = ['1.1.1.6', '4.2.2.4', '2.9.9.2', '3.3.3.3', '5.2.3.1', '10.234.2.5']
listofips.sort(key=lambda x: x.split('.')[-1])
print(listofips)



# ###make a class called Buildit with IP attribute. Then a method that uses a command.
# # Make a list of devices that will call the class###

class Buildit():
    def __init__(self, ipadd):
        self.ipadd = ipadd
        self.url = f'http://admin:admin@{self.ipadd}/command-api'
        self.ss = Server(self.url)

    def cmds(self, cmd):
        response = self.ss.runCmds(1, [cmd])
        return response


devs = {'c1': '192.168.10.1'}
cmds = 'show version'


#Create rundictcomp function to create a dictionary of the device and eapi_call using dictionary compression
def rundictcomp():
    dict_comp = {k: Buildit(v).cmds(cmds) for k, v in devs.items()}
    return dict_comp
print(rundictcomp())


#Create runmaplambda function to create a dictionary of the device and eapi_call using map and lambda
def runmaplambda():
    map_lambda = dict(map(lambda x: (x[0], Buildit(x[1]).cmds(cmds)), devs.items()))
    return map_lambda
print(runmaplambda())


###
# Create rundict_from_2list function to create a dictionary of the device and eapi_call by first splitting devs into 2 lists (k,v)
# then create usedict object to create a dict comprehension of the 2 sets of lists###
def rundict_from_2list():
    k = [k for k in devs]
    v = [devs[k] for k in devs]
    dict_comp = {mk: Buildit(mv).cmds(cmds) for mk in k for mv in v}
    return dict_comp
print(rundict_from_2list())


# 1 step solution- Create rundict_tuple function to create a list comprehension of tuples of the device and eapi_call by first packing devs into tuple###
def rundict_tuple():
    mytuple = dict((k, Buildit(v).cmds(cmds)) for k, v in devs.items())
    return mytuple
print(rundict_tuple())


# 2 step solution - Create rundict_from_tuple function to create a list of tuples of the device and eapi_call by first packing devs into tuple (k,v)
# by creating from_tuple tuple that holds the key/value. Then call from_tuple in a tuple_map to map###
def rundict_from_tuple():
    from_tuple = tuple((k, v) for k, v in devs.items())
    tuple_map = dict(map(lambda x: (x[0], Buildit(x[1]).cmds(cmds)), from_tuple))
    return tuple_map
print(rundict_from_tuple())



# use 3 different versions of execute function - execute1, execute2, and execute3
#execute1 - create a list of ips using list comprehension and get value by using dict key reference (dict[key]).
#Create a list of devs.
#Cycle through the dictionary "devs" by using a range(len(devs)) and store them in another dict call "dict_of_objs"
def execute1():
    ips = [devs[key] for key in devs]
    mydevs = [dev for dev in devs]
    dict_of_objs = dict((mydevs[x], Buildit(ips[x]).cmds(cmds)) for x in range(len(devs)))
    return dict_of_objs
print(execute1())




#execute2 - Use Zip! make an object "iterator_of_objs" with map calling the "devs.values()". This will hold the class objects in
#an iterator. Then zip the "iterator_of_objs" with the "devs.keys{}" to make a dict with keys.objs dict.



#execute 3 - use a dictionary comprehension to create a dict of class objects using typical k, v in devs.items()
#have some fun with mac addresses
macadd = '1234.5678.abcd'
#these 2 examples below normalize the xxxx.xxxx.xxxx format into just 12 characters
stripmac = macadd.replace('.', '')
stripmac2 = ''.join(macadd.split('.'))
print(stripmac)
print(stripmac2)

#format the xx:xx:xx:xx:xx:xx mac address using a join iterator
maclist = ':'.join(stripmac2[x: x + 2] for x in range(0, len(stripmac2), 2))
print('maclist1', maclist)

#format the xx:xx:xx:xx:xx:xx mac address using a join iterator
maclist2 = ':'.join(stripmac[x] + stripmac[x + 1] for x in range(0, len(stripmac) - 1, 2))
print('maclist2', maclist2)



print(':'.join(a+b for a, b in zip(stripmac[::2], stripmac[1::2])))

newsbi = ''.join(list(map(lambda y, z: y + z + ':', stripmac[::2], stripmac[1::2])))[:-1]
print(newsbi)


# nutz = [(stripmac[x] + stripmac[x + 1] for x in range(0, len(stripmac) - 1, 2))]
# print(type(nutz))

print(list(zip(stripmac[::2], stripmac[1::2])))

b, w = stripmac[::2], stripmac[1::2]
print(b, w)




maclist3 = ':'.join(stripmac[x] + stripmac[x + 1] for x in range(0, len(stripmac) -1, 2))
print(maclist3)