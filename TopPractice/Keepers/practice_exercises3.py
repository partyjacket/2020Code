#
# from pprint import pprint as pp
# from jsonrpclib import Server
#
# def q(x):
#     return f'http://admin:admin{x}/command-api'
#
# # mydict = {'big': 'boy'}
# dict1 = {1: 'one', 2: 'two'}
# dict2 = {}
# # #reverse the key value on dict1 using function called "swap" and assign to dict2
# def swap(x):
#     for k, v in x.items():
#         dict2[v] = k
# swap(dict1)
# print(dict2)
#
# # #reverse the key values back to dict1 original and assign to dict3 using dictionary comprehension
# dict3 = {k: v for v, k in dict2.items()}
# print(dict3)
#
#
#
#
# #reverse the key valuein dict2.items()}
# print({v: k for k, v in dict2.items()})
#
#
#
#
# # #remap the digit value of dict2 to increment by one using a function called "remap" and assign it to dict4
# #send dict2 as tuple to remap to add one to the digit in index[1] using "dict" method (this is not dict comprehension)
#
# def remap(x):
#     return x[0], x[1] + 1
#
# dict4 = dict(remap(x) for x in dict2.items())
# print(dict4)
#
#
#
#
# # # sort based on length of list object
# listoflens = ['dddd', 'bb', 'ccc', 'a']
#
# print(sorted(listoflens, key=lambda x: len(x)))
#
# listoflens.sort(key=lambda x: len(x))
# print(listoflens)
#
#
#
# # # create a url object using the list below with map, then do it again making object url2 with list comprehension
# ipadd = ['192.168.10.1', '192.168.10.2']
#
# url1 = list(map(lambda x: 'http{}'.format(x), ipadd))
# print(url1)
#
# url2 = ['http:{}'.format(x) for x in ipadd]
# url3 = list('http:{}'.format(x) for x in ipadd)
# print(url3)
# print(url2)
#
#
#
#
# # #print each of these sorting on last name
# namelist = ['Jason Zatterson', 'Zig Boy']
# namedict = {'Jason': 'Zatterson', 'Zig': 'Boy'}
# newtuple = [('Jason Zatterson'), ('Zig Boy')]
#
# print(sorted(namelist, key=lambda x: x.split()[1]))
# print(sorted(namedict.items(), key=lambda x: x[1]))
#
# #add one to each number and return list using a map
# numlist = [1, 2, 3]
# print(list(map(lambda x: x ** x, numlist)))
#
#
#
# # #sort ips based on last octet
# listofips = ['1.1.1.6', '4.2.2.4', '2.9.9.2', '3.3.3.3', '5.2.3.1', '10.234.2.5']
# print(sorted(listofips, key=lambda x: x[-1]))
# listofips.sort(key=lambda x: x[-1])
# print(listofips)
#
#
#
# # ###make a class called Buildit with IP attribute. Then a method that uses a command.
# # # Make a list of devices that will call the class###
#
# class Buildit():
#     def __init__(self, ipadd):
#         self.ipadd = ipadd
#         self.url = f'http://admin:admin@{self.ipadd}/command-api'
#         self.ss = Server(self.url)
#
#     def cmds(self, cmd):
#         response = self.ss.runCmds(1, [cmd])[0]['modelName']
#         return response
#
#
# devs = {'c1': '192.168.10.1', 'rfw': '192.168.10.49'}
# cmds = 'show version'
#
#
# #Create rundictcomp function to create a dictionary of the device called dictofdevs and eapi_call using dictionary compression
# def rundictcomp():
#     dictofdevs = {k: Buildit(v).cmds(cmds) for k, v in devs.items()}
#     return dictofdevs
#
#
# #Create runmaplambda1 function to create a dictionary of the devices called dictofdevs1 and eapi_call using map and lambda
# #by sending a tuple (.items()) to the map function.
# def runmaplambda1():
#     dictofdevs1 = dict(map(lambda x: (x[0], Buildit(x[1]).cmds(cmds)), devs.items()))
#     print(dictofdevs1)
# runmaplambda1()
#
# #Create runmaplambda2 function to create a dictionary of the devices called dictofdevs2 and eapi_call using map and lambda
# #by sending mapping the key and value variables seperately to k, v in the lambda
#
# def runmaplambda2():
#     dictofdevs2 = dict(map(lambda k, v: (k, Buildit(v).cmds(cmds)), devs.keys(), devs.values()))
#     print(dictofdevs2)
# runmaplambda2()
#
#
# # Create rundict_from_2list function to create a dictionary of the device and eapi_call by first splitting
# # devs into 2 lists (k,v) then create usedict object to create a dict comprehension of the 2 sets of lists
# def rundict_from_2list():
#     list1 = [k for k in devs.keys()]
#     list2 = [v for v in devs.values()]
#     returndict = {k: Buildit(v).cmds(cmds) for k in list1 for v in list2}
#     return returndict
#
# print(rundict_from_2list())
#
#
#
#
# # 1 step solution- Create rundict_tuple function to create a list comprehension of tuples of the device and eapi_call
# #by first packing devs into tuple
#
# def rundict_tuple():
#     list1 = [(x, Buildit(y).cmds(cmds)) for x, y in devs.items()]
#     return list1
# print(rundict_tuple())
#
#
#
# # 2 step solution - This will create a dict from a tuple that we first instantiate (this is ultimately the same as using
# # .items() but manually) Create rundict_from_tuple function to create a list of tuples of the device and eapi_call by
# # first packing devs into tuple (k,v) by creating from_tuple tuple that holds the key/value. Then create a dict of
# # device + eapi called tuple_map to map each tuple in from_tuple.
# def rundict_from_tuple():
#     from_tuple = [(k, v) for k, v in devs.items()]
#     tuple_map = dict(map(lambda x: (x[0], Buildit(x[1]).cmds(cmds)), from_tuple))
#     return tuple_map
#
# print(rundict_from_tuple())
#
# # use 3 different versions of execute function - execute1, execute2, and execute3
# #execute1 - create a list of ips using list comprehension and get value by using dict key reference (dict[key]).
# #Create a list of devs.
# #Cycle through the dictionary "devs" by using a range(len(devs)) and store them in another dict call "dict_of_objs"
#
# def execute1():
#     listofips = [x[1] for x in devs.items()]
#     listofips2 = [devs[key] for key in devs] #this will call the key, which will respond with value
#     listofdevs = [x for x in devs.keys()]
#     dictofobjs = {listofdevs[x]: Buildit(listofips[x]).cmds(cmds) for x in range(len(devs))}
#     print('nutz', dictofobjs)
# execute1()
#
# #execute2 - make an object "iterator_of_objs" with map calling the "devs.values()". This will hold the class objects in
# #an iterator. Then zip the "iterator_of_objs" with the "devs.keys()" to make a dict called "dict_of_kv) with "iterator_of_objs" dict.
# def execute2():
#     iterator_of_objs = map(lambda x: Buildit(x).cmds(cmds), devs.values())
#     dict_of_keys = dict(zip(devs.keys(), iterator_of_objs))
#     return dict_of_keys
# print(execute2())
#
#
# #execute3 - use a dictionary comprehension to create a dict of class objects using typical k, v in devs.items()
# def execute3():
#     mydict = {k: Buildit(v).cmds(cmds) for k, v in devs.items()}
#     return mydict
# execute3()
#
# #execute4 - make a dict called dict_of_lists by zipping 2 list comprehensions. - First list is keys, second is Buildit(values).
# def execute4():
#     dict_of_lists = dict(zip([key for key in devs.keys()], [Buildit(value).cmds(cmds) for value in devs.values()]))
#     return dict_of_lists
# print(execute4())
# print('\n' * 3)

# #have some fun with mac addresses
macadd = '1234.5678.abcd'
#these 2 examples below normalize the xxxx.xxxx.xxxx format into just 12 characters
stripmac = macadd.replace('.', '')
stripmac2 = ''.join(macadd.split('.'))

print(stripmac)
print(stripmac2)
# #format the xx:xx:xx:xx:xx:xx mac address using a join iterator
newmac1 = ':'.join(stripmac[x:x+2] for x in range(0, len(stripmac), 2))
print(newmac1)



# #format the xx:xx:xx:xx:xx:xx mac address using a join iterator
newmac2 = ':'.join(stripmac[x] + stripmac[x + 1] for x in range(0, len(stripmac), 2))
print(newmac2)

# print('maclist2', maclist2)
# print(maclist2)
numlist2 = [1,2,3,4,5,6]
print(numlist2[:len(numlist2)])
for i in range(len(numlist2)):
    print(i)
newmac3 = ':'.join(x + y for x, y in zip(stripmac[::2], stripmac[1::2]))
print(newmac3)
# newmac3 = ':'.join(x + y for x, y in zip(stripmac[::2], stripmac[1::2]))
# print(newmac3)
mynum = '11,22,33,44,55,66'

testings = ':'.join(x + y for x, y in zip(mynum.replace(',', '')[::2], ''.join(mynum.split(','))[1::2]))
print(testings)
print(mynum.replace(',', '')[::2])
print(''.join(mynum.split(',')))


rats = 'aa,bb,cc,dd,ee,ff'
newrat = ':'.join(x + y for x, y in zip(rats.replace(',', '')[::2], rats.replace(',', '')[1::2]))
print(newrat)
blue = zip(rats.replace(',', '')[::2], rats.replace(',', '')[1::2])
print(type(blue))