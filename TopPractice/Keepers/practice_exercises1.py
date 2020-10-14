
from pprint import pprint as pp
from jsonrpclib import Server


# mydict = {'big': 'boy'}
dict1 = {1: 'one', 2: 'two'}
dict2 = {}
# #reverse the key value on dict1 using function called swap and assign to dict2
def swap(x):
    for k, v in x.items():
        dict2[v] = k

swap(dict1)

print(dict2)


# #reverse the key values back to dict1 original and assign to dict3 using dictionary comprehension
dict3 = {v: k for k, v in dict2.items()}
print(dict3)



# #remap the digit value of dict1 to increment by one using a function called "remap" and assign it to dict4
# #send dict2 as tuple to remap to add one to the digit in index[1]
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
url = list(map(lambda x: f'http://admin:admin{x}/command-api', ipadd))
print(url)

url2 = [f'http://admin:admin{x}/command-api' for x in ipadd]
print(url2)

# #print each of these sorting on last name
namelist = ['Jason Zatterson', 'Zig Boy']
namedict = {'Jason': 'Zatterson', 'Zig': 'Boy'}
newtuple = [('Jason Zatterson'), ('Zig Boy')]
namelist.sort(key=lambda x: x.split()[1])
print(namelist)
newdict = dict(sorted(namedict.items(), key=lambda x: x[-1]))
print(newdict)
newtuple.sort(key=lambda x: x.split()[-1])
print(newtuple)

#add one to each number and return list using a map
numlist = [1, 2, 3]
newnum = list(map(lambda x: x + 1, numlist))
print(newnum)


# #sort ips based on last octet
listofips = ['1.1.1.6', '4.2.2.4', '2.9.9.2', '3.3.3.3', '5.2.3.1', '10.234.2.5']

print(sorted(listofips, key=lambda x: x.split('.')[-1]))


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
    v = [v for v in devs.values()]
    dict_comp = {mk: Buildit(mv).cmds(cmds) for mk in k for mv in v}
    return dict_comp
print(rundict_from_2list())


# 1 step solution- Create rundict_tuple function to create a list comprehension of tuples of the device and eapi_call by first packing devs into tuple###
def rundict_tuple():
    tuple1step = dict([(k, Buildit(v).cmds(cmds)) for k, v in devs.items()])
    return tuple1step
print(rundict_tuple())

# 2 step solution - Create rundict_from_tuple function to create a list of tuples of the device and eapi_call by first packing devs into tuple (k,v)
# by creating from_tuple tuple that holds the key/value. Then call from_tuple in a tuple_map to map###
def rundict_from_tuple():
    from_tuple = [(k, v) for k, v in devs.items()]
    run_tuple = dict(map(lambda x: (x[0], Buildit(x[1]).cmds(cmds)), from_tuple))
    return run_tuple
print(rundict_from_tuple())

# use 3 different versions of execute function - execute1, execute2, and execute3
#execute1 - create a list of ips using list comprehension and get value by using dict key reference (dict[key]).
#Cycle throug the dictionary "devs" by using a range(len(devs)) and store them in another dict call "dict_of_objs"

def execute_():
    list_of_devs = [key for key in devs]
    list_of_ips = [devs[key] for key in devs]
    list_of_ips2 = [value for value in devs.values()]
    dict_of_objs = {list_of_devs[x]: Buildit(list_of_ips[x]).cmd(cmds) for x in range(len(devs))}
    return dict_of_objs

#execute2 - make an object "iterator_of_objs" with map calling the "devs.values()". This will hold the class objects in
#an iterator. Then zip the "iterator_of_objs" with the "devs.keys{}" to make a dict with keys.objs dict.
def execute2():
    iterator_of_objs = map(lambda x: Buildit(x).cmd(cmds), devs.values())
    dict_of_objs = dict(zip(devs.keys(), iterator_of_objs))
    return dict_of_objs

#execute 3 - use a dictionary comprehension to create a dict of class objects using typical k, v in devs.items()
def execute3():
    dict_of_objs = {k: Buildit(v).cmd(cmds) for k, v in devs.items()}
    return dict_of_objs
