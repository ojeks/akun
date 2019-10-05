import json , sys , hashlib , os , time , marshal, getpass , random
def ojeks(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)
ojeks('Masukkan username terserah anda\nNickname paling bagus yang anda sukai\nDan masukkan password nya :)')
if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
        G = '\033[32;1m'
        R = '\033[36;1m'
else:
	W = ''
	G = ''
	R = ''
try:
	import requests
except ImportError:
	print R + '_     _'.center(50)
	print "o' \.=./ `o".center(50)
	print '(o o)'.center(50)
	print 'ooO--(_)--Ooo'.center(50)
	print G + ' '
	print ('Created by : ojeks').center(50)
	print ' '
	sys.exit()