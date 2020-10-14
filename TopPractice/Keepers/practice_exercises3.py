
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
dict3 = {k: v for v, k in dict2.items()}
print(dict3)




#reverse the key valuein dict2.items()}
print({v: k for k, v in dict2.items()})




# #remap the digit value of dict2 to increment by one using a function called "remap" and assign it to dict4
#send dict2 as tuple to remap to add one to the digit in index[1] using "dict" method (this is not dict comprehension)

def remap(x):
    return x[0], x[1] + 1

dict4 = dict(remap(x) for x in dict2.items())
print(dict4)




# # sort based on length of list object
listoflens = ['dddd', 'bb', 'ccc', 'a']

print(sorted(listoflens, key=lambda x: len(x)))



# # create a url object using the list below with map, then do it again making object url2 with list comprehension
ipadd = ['192.168.10.1', '192.168.10.2']







# #print each of these sorting on last name
namelist = ['Jason Zatterson', 'Zig Boy']
namedict = {'Jason': 'Zatterson', 'Zig': 'Boy'}
newtuple = [('Jason Zatterson'), ('Zig Boy')]



#add one to each number and return list using a map
numlist = [1, 2, 3]



# #sort ips based on last octet
listofips = ['1.1.1.6', '4.2.2.4', '2.9.9.2', '3.3.3.3', '5.2.3.1', '10.234.2.5']




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



#Create runmaplambda function to create a dictionary of the device and eapi_call using map and lambda



###
# Create rundict_from_2list function to create a dictionary of the device and eapi_call by first splitting devs into 2 lists (k,v)
# then create usedict object to create a dict comprehension of the 2 sets of lists###



# 1 step solution- Create rundict_tuple function to create a list comprehension of tuples of the device and eapi_call by first packing devs into tuple###



# 2 step solution - Create rundict_from_tuple function to create a list of tuples of the device and eapi_call by first packing devs into tuple (k,v)
# by creating from_tuple tuple that holds the key/value. Then call from_tuple in a tuple_map to map###




# use 3 different versions of execute function - execute1, execute2, and execute3
#execute1 - create a list of ips using list comprehension and get value by using dict key reference (dict[key]).
#Create a list of devs.
#Cycle through the dictionary "devs" by using a range(len(devs)) and store them in another dict call "dict_of_objs"





#execute2 - Use Zip! make an object "iterator_of_objs" with map calling the "devs.values()". This will hold the class objects in
#an iterator. Then zip the "iterator_of_objs" with the "devs.keys{}" to make a dict with keys.objs dict.



#execute 3 - use a dictionary comprehension to create a dict of class objects using typical k, v in devs.items()

print('\n' * 3)

# #have some fun with mac addresses
# macadd = '1234.5678.abcd'
# #these 2 examples below normalize the xxxx.xxxx.xxxx format into just 12 characters
# stripmac = macadd.replace('.', '')
# stripmac2 = ''.join(macadd.split('.'))
# print(stripmac)
# print(stripmac2)
#
# #format the xx:xx:xx:xx:xx:xx mac address using a join iterator
# newmac1 = ':'.join(stripmac[x:x+2] for x in range(0,len(stripmac),2))
# print(newmac1)
#
# newmac2 = ':'.join(stripmac[x] + stripmac[x + 1] for x in range(0, len(stripmac), 2))
# print(newmac2)
# #format the xx:xx:xx:xx:xx:xx mac address using a join iterator
#
# maclist2 = ':'.join(stripmac2[x] + stripmac2[x + 1] for x in range(0, len(stripmac2), 2))
# print('maclist2', maclist2)
# print(maclist2)
# numlist2 = [1,2,3,4,5,6]
# print(numlist2[:len(numlist2)])
#
# newmac3 = ':'.join(x + y for x, y in zip(stripmac[::2], stripmac[1::2]))
# print(newmac3)



