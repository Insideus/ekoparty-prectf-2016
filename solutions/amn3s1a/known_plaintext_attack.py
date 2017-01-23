flag = "\x17'_4&)E uhh<&hW?5/\x11:'r\x11\x16\x1f\x07Jc2qTkbq\x02c`z\x03kaz\x05e0|\x012g~Ujm-\x06bd|T2mz\x02ca*\x04."

def do_xor(text, key):
	r = ''
	lk = len(key)
	for i in range(len(text)):
		#print "'" + text[i] + "' ^ '" + key[i % lk] + "'"
		r += chr(ord(text[i]) ^ ord(key[i % lk]))
	return r

keys = []

for i in xrange(len(flag)):
	key = do_xor(flag[i:i+4], 'EKO{')
	if len(key) == 4:
		keys.append(key)

for k in keys[23:25]:
	for i in xrange(4):
		nk = k[i:]+k[:i]
		result = do_xor(flag, nk)
		if 'EKO{' in result:
			print nk, result
