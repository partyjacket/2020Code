import signal
import os


class TimeExceededError(object):
    pass


def timeout(signum, frame):
    raise TimeExceededError


signal.signal(signal.SIGALRM, timeout)


num_of_devs = int(input("Yo sancheeze, how many ips you want me to get after? "))
baseip = '192.168.10.31'


def runcmds(z):
    base = int(baseip.split('.')[-1])
    print(base)
    x = 0
    while x < z:
        try:
            signal.alarm(5)
            ip = '.'.join(baseip.split('.')[:-1]) + '.' + str(x + base)
            print('Starting to SCP to ' + ip)
            send_scp = os.system('sshpass -p "admin" scp /Users/jpatterson/Downloads/vEOS-lab-4.24.2.3F.swi admin@{}:/mnt/flash/'.format(ip))

        except:
            print('')
        x += 1


runcmds(num_of_devs)





